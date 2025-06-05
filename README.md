# 📦 Logistics Analytics Platform – End-to-End Azure Data Engineering Project

This project demonstrates a modern data engineering workflow using the **Medallion Architecture (Bronze → Silver → Gold)** to deliver operational logistics insights.  
It's designed for enterprise-scale logistics or transport companies to monitor **shipment performance**, **delays**, and **fleet/vendor KPIs** using:

- 🚛 **Azure Data Factory**  
- 🚀 **Azure Databricks + PySpark**  
- 📁 **Delta Lake + Parquet**  
- 📊 **Power BI for Visualization**

---

## 🧱 Architecture

![Architecture Diagram](architecture/Architecture%20Diagram.png)

---

## 📁 Folder Structure

logistics-analytics-platform/
│
├── data/ # Dummy CSVs (drivers, vendors, routes, shipments)
├── notebooks/ # Databricks Notebooks for each layer
├── adf_pipelines/ # ADF JSON definitions
├── powerbi/ # Power BI screenshots or .pbix files
├── architecture/ # Architecture diagram image
├── README.md # This file
└── .gitignore

---

## 📊 Power BI Dashboard Features

- ✅ KPI Cards: Total Shipments, Avg Delay, On-Time %
- 📊 Vendor performance bar charts
- 📈 Monthly delivery trend lines
- 🗺️ Route-level delay matrix (simulated map)
- 🎯 Filters: Vendor, Route Type, Origin, Destination

---

## 📌 Pipeline Stages

### 🔹 Bronze Layer (Raw Ingestion)
- Raw files: `drivers.csv`, `vendors.csv`, `routes.csv`, `shipments.csv`
- Ingested using **ADF Copy Activity** with **ForEach loop**
- Stored in Azure Data Lake under the `bronze/` container

### 🔸 Silver Layer (Cleansed)
- Field renaming and schema standardization
- Converted timestamps and metrics (e.g., delay in minutes)
- Stored as partitioned Parquet files in `silver/` container

### 🟡 Gold Layer (Aggregated)
- Enriched metrics like:
  - On-Time %
  - Delay by route
  - Vendor KPIs
  - Monthly trends
- Written to `gold/` container, ready for Power BI

---

## 🧠 Skills Demonstrated

- ✅ Metadata-driven ADF pipelines (parameterized + looped)
- 🧠 Databricks data transformation using PySpark
- 🗃️ Medallion architecture (Bronze → Silver → Gold)
- 💾 Delta Lake & partitioned Parquet files
- 📅 Incremental + batch pipeline logic
- 📈 Clean and professional Power BI dashboards
- 🔐 Secure handling of storage & access configuration

---

## 📤 How to Reproduce

1. Clone this repo
2. Upload `/data/` CSVs to Azure Data Lake Gen2 (`raw` container)
3. Import and run ADF pipelines from `/adf_pipelines/`
4. Execute transformation notebooks in `/notebooks/` inside Databricks
5. Open Power BI file from `/powerbi/` and connect to `gold` container

---

## 📩 Contact

📧 Email: **rao.mohsin.54@gmail.com**  
🌐 [LinkedIn](https://www.linkedin.com/in/mohsin-mukhtiar/)  
✍️ [Medium Profile](https://medium.com/@rao.mohsin.54)

---

## ⭐ Star This Repo

If you found this project useful, give it a ⭐ on GitHub — and feel free to fork or adapt it!

---
