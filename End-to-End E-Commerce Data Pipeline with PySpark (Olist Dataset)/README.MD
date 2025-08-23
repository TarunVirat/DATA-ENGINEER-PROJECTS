# 📦 End-to-End E-Commerce Data Pipeline with PySpark (Olist Dataset)

This project implements a full **end-to-end data pipeline** on the [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), covering **data ingestion, cleaning, transformation, integration, optimization, and serving**. The goal is to demonstrate how a real-world retail dataset can be processed using **PySpark** and prepared for advanced analytics such as customer retention, seller performance, and payment trends.

## 📊 Dataset Overview
The dataset contains **100k+ orders** made at Olist Store, an e-commerce platform in Brazil. It links **customers, sellers, products, payments, reviews, and geolocation** into a relational schema.

![Dataset Schema](13285472-59db-43ae-95a8-f00762563128.png)

**Main tables:**
- `olist_orders_dataset` → orders metadata (status, timestamps).  
- `olist_order_items_dataset` → product items per order.  
- `olist_order_payments_dataset` → payment method & value.  
- `olist_order_reviews_dataset` → customer reviews & scores.  
- `olist_products_dataset` → product catalog.  
- `olist_sellers_dataset` → sellers’ info.  
- `olist_customers_dataset` → customer info.  
- `olist_geolocation_dataset` → geolocation (lat/lon by ZIP).  

## ⚙️ Project Workflow
This repo is structured into **5 modules**, each represented by a Jupyter Notebook (`.ipynb`).

### Module 1 – Data Ingestion & Exploration
- Ingest raw CSVs into **HDFS/Spark DataFrames**.  
- Validate schema and datatypes.  
- Initial exploratory analysis (row counts, missing values, distributions).  

### Module 2 – Data Cleaning & Transformation
- Handle nulls, duplicates, and inconsistent records.  
- Convert columns (e.g., timestamps to proper `timestamp`).  
- Apply business logic transformations (e.g., order status normalization).  

### Module 3 – Data Integration & Aggregation
- Join across multiple datasets (orders ↔ items ↔ payments ↔ reviews).  
- Aggregate metrics:  
  - First & last purchase dates per customer.  
  - Average Order Value (AOV).  
  - Seller performance by review score.  

### Module 4 – Property Optimization
- Optimize storage with **Parquet** format.  
- Apply **partitioning/bucketing** for faster queries.  
- Cache frequently used tables.  

### Module 5 – Data Serving
- Store final curated datasets back into HDFS (`/processed`).  
- Make datasets query-ready for BI tools and ML pipelines.  
- Example queries:  
  - Customer retention analysis.  
  - Weekend vs weekday purchase behavior.  
  - Payment trends by installment count.  

## 📂 Repository Structure

## 🛠️ Tech Stack
- **Apache Spark (PySpark)** – distributed ETL & analytics  
- **HDFS (Hadoop Distributed File System)** – storage  
- **Jupyter Notebooks** – development & visualization  
- **Parquet** – optimized columnar storage  
-

## 👨‍💻 Author
**Tarun Peela**  
📍 Tampa, FL  
📞 813-613-8906  
📧 tarunpeela0@gmail.com  
 

## 🚀 How to Run
1. Clone this repo & download the [Kaggle dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).  
2. Upload the CSVs to HDFS path `/user/<username>/olist/`.  
3. Launch Jupyter Notebook inside your Spark cluster (GCP, AWS EMR, or local).  
4. Run notebooks in order (`Module 1 → Module 5`).  
5. Processed Parquet files will be available under `/user/<username>/olist/processed/`.

## 📈 Example Analysis
- Customer Retention (first vs last order per unique customer).  
- Seller Performance by review score & revenue.  
- Payment method popularity & installment analysis.  
- Geographical spread of orders across Brazil.  

## 📌 References
- [Kaggle – Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)  
- Olist Official Documentation  
