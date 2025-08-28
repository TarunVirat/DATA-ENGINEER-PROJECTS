from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
import json

# Define the DAG
with DAG(
    dag_id="nasa_apod_postgres",
    start_date=days_ago(1),
    schedule_interval="@daily",   # ✅ old syntax for 3.0-8
    catchup=False,
    tags=["nasa", "etl"]
) as dag:

    # Step 1: Create the table if it doesn't exist
    @task
    def create_table():
        postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")
        create_table_query = """
        CREATE TABLE IF NOT EXISTS apod_data (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE,
            media_type VARCHAR(50)
        );
        """
        postgres_hook.run(create_table_query)

    # Step 2: Extract data from NASA API
    extract_apod = SimpleHttpOperator(
        task_id="extract_apod",
        http_conn_id="nasa_api",   # must be configured in Airflow Connections
        endpoint="planetary/apod",
        method="GET",
        data={"api_key": "{{ conn.nasa_api.extra_dejson.api_key }}"},
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

    # Step 3: Transform the data
    @task
    def transform_apod_data(response):
        return {
            "title": response.get("title", ""),
            "explanation": response.get("explanation", ""),
            "url": response.get("url", ""),
            "date": response.get("date", ""),
            "media_type": response.get("media_type", "")
        }

    # Step 4: Load into Postgres
    @task
    def load_data_to_postgres(apod_data: dict):
        postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")
        insert_query = """
        INSERT INTO apod_data (title, explanation, url, date, media_type)
        VALUES (%s, %s, %s, %s, %s);
        """
        postgres_hook.run(
            insert_query,
            parameters=(
                apod_data["title"],
                apod_data["explanation"],
                apod_data["url"],
                apod_data["date"],
                apod_data["media_type"]
            )
        )

    # Dependencies
    create_table() >> extract_apod
    transformed_data = transform_apod_data(extract_apod.output)
    load_data_to_postgres(transformed_data)
