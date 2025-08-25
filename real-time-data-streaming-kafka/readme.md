# ⚡ Confluent Kafka Producer & Consumer (Python)  
This project demonstrates how to use Apache Kafka on Confluent Cloud with Python clients for producing and consuming messages.  

## 📂 Project Structure  
- producer_confluentKafka.ipynb → Kafka Producer notebook  
- consumer_confluentKafka.ipynb → Kafka Consumer notebook  
- architecture.png → Data flow diagram (Producer → Kafka → Consumer)  
- README.md → Documentation  

## 🛠️ Tech Stack  
- Apache Kafka (Confluent Cloud) – Managed Kafka service  
- Python – Producer & Consumer clients  
- confluent-kafka-python – Kafka client library  

## 🚀 How to Run  
1️⃣ Install Dependencies: run `pip install confluent-kafka`  
2️⃣ Update Credentials: inside both notebooks, set `sasl.username = "<YOUR_API_KEY>"` and `sasl.password = "<YOUR_API_SECRET>"`  
3️⃣ Run Producer: open `producer_confluentKafka.ipynb` → sends customer data messages into Kafka topic `ecommerce`  
4️⃣ Run Consumer: open `consumer_confluentKafka.ipynb` → consumes messages from Kafka topic `ecommerce` under group `customer_group`  

## 📊 Architecture  
Producer Notebook → Confluent Kafka Topic: ecommerce → Consumer Notebook (group: customer_group)  

## ✅ Output Example  
Producer: `Message delivered to ecommerce [0] at offset 12`  
Consumer: `Received message : Key = 101 , Value = {"customer_id":101, "name":"Alice", "country":"US"}`  

## 👨‍💻 Author  
**Tarun Peela**  
📍 Tampa, FL 
📧 tarunpeela0@gmail.com  
🔗 GitHub: https://github.com/TarunVirat  
