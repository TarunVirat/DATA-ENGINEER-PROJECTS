# 🛒 Brazilian E-Commerce Data Pipeline with Azure & Databricks  

This project builds an **end-to-end big data pipeline** using the **Olist Brazilian E-Commerce dataset**.  
The goal is to design, transform, and analyze large-scale e-commerce data using modern cloud tools, enabling actionable business insights.  

---

## 📊 Architecture  

![Architecture Diagram](Architecture%20Diagram.png)

**Flow:**  
1. **Data Sources**: Olist datasets (customers, orders, payments, reviews, products, sellers, geolocation).  
2. **Ingestion**: Data loaded into **Azure Data Lake Storage (ADLS Gen2)** via **Azure Data Factory**.  
3. **Transformation**: Processing and enrichment with **Azure Databricks** (PySpark).  
4. **Storage**: Curated datasets stored back in ADLS Gen2.  
5. **Analytics & Visualization**: Data loaded into **Azure Synapse** and visualized in **Power BI/Tableau/Fabric**.  
6. **External Enrichment**: Additional tables from **MongoDB** integrated for business context.  

---

## 📂 Project Structure  

```
Brazilian-Ecommerce-BigData/
│── Data/                         # Olist dataset CSV files
│── Codes/                        # PySpark / SQL scripts
│── DataIngestionToDB.ipynb       # Notebook for ingestion
│── ForEachInput.json             # Config for ADF pipeline
│── sql code/                     # SQL transformation scripts
│── notes.txt                     # Handwritten study notes
│── Architecture Diagram.png      # Final pipeline diagram
│── Architecture Diagram.excalidraw # Editable source diagram
│── README.md
```

---

## 📚 Dataset  

We use the [Olist Brazilian E-Commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).  
It contains multiple linked tables:  

- `olist_customers_dataset.csv` → Customer details  
- `olist_orders_dataset.csv` → Orders & timestamps  
- `olist_order_items_dataset.csv` → Products in each order  
- `olist_order_payments_dataset.csv` → Payment methods & values  
- `olist_order_reviews_dataset.csv` → Customer reviews & ratings  
- `olist_products_dataset.csv` → Product catalog  
- `olist_sellers_dataset.csv` → Seller information  
- `olist_geolocation_dataset.csv` → Customer & seller locations  
- `product_category_name_translation.csv` → English mapping for product categories  

---

## ⚙️ Tech Stack  

- **Data Lake**: Azure Data Lake Storage Gen2  
- **Orchestration**: Azure Data Factory  
- **Processing**: Azure Databricks (PySpark)  
- **Data Warehouse**: Azure Synapse Analytics  
- **NoSQL Enrichment**: MongoDB  
- **Visualization**: Power BI, Tableau, Microsoft Fabric  

---

## 🚀 How to Run  

1. Clone this repo  
   ```bash
   git clone https://github.com/YOURUSERNAME/Brazilian-Ecommerce-BigData.git
   cd Brazilian-Ecommerce-BigData
   ```
2. Upload the `Data/` folder to your ADLS Gen2 container.  
3. Deploy the **ADF pipeline** using `ForEachInput.json`.  
4. Open `DataIngestionToDB.ipynb` in **Databricks** and execute transformations.  
5. Run SQL scripts inside **Synapse** to build reporting tables.  
6. Connect Power BI/Tableau/Fabric to Synapse for dashboards.  

---

## 📈 Sample Insights  

- Top-selling product categories and seasonality  
- Payment method trends (credit card, boleto, voucher, etc.)  
- Customer satisfaction by seller/product (review scores)  
- Delivery performance vs promised SLA  
- Revenue growth by state & region  

---

## 👨‍💻 Author  

**Tarun Peela**  
📍 Tampa, FL | Data Engineer / Data Scientist  
📧 tarunpeela0@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/tarunpeela)  
🔗 [GitHub](https://github.com/TarunVirat)  

---
