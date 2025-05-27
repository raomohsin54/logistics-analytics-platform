 
📦 Logistics Analytics Platform – End-to-End Azure Data Engineering Project
This project demonstrates a modern data engineering workflow using the Medallion Architecture (Bronze → Silver → Gold) to deliver operational logistics insights. It's designed for enterprise-scale logistics or transport companies to monitor shipment performance, delays, and fleet/vendor KPIs using:

🚛 Azure Data Factory
🚀 Azure Databricks + PySpark
📁 Delta Lake + Parquet
📊 Power BI for Visualization

🧱 Architecture

![Architecture Diagram](https://github.com/user-attachments/assets/6610ad97-d196-454e-95de-926f9b7d493e)


📁 Folder Structure
bash
Copy
Edit
logistics-analytics-platform/
│
├── data/                    # Dummy CSVs (drivers, vendors, routes, shipments)
├── notebooks/               # Databricks Notebooks for each layer
├── adf_pipelines/           # ADF JSON definitions
├── powerbi/                 # Power BI screenshots or .pbix
├── architecture/            # Architecture diagram
├── README.md                # This file
└── .gitignore

📊 Power BI Dashboard Features
KPI Cards: Total Shipments, Avg Delay, On-Time %

Vendor performance bar charts

Monthly delivery trend lines

Route-level delay matrix

Map visualization (simulated)

Filters: Vendor, Route Type, Origin, Destination


📌 Pipeline Stages
🔹 Bronze Layer (Raw Ingestion)
Files: drivers.csv, vendors.csv, routes.csv, shipments.csv

Copied via ADF into the bronze/ container

🔸 Silver Layer (Cleansed)
Standardized field names

Converted timestamps and distances

Saved as partitioned Parquet files

🟡 Gold Layer (Aggregated)
Shipment KPIs by vendor, route, month

Calculated delay time and on-time %

Output stored in gold/ container


🧠 Skills Demonstrated
Metadata-driven ADF pipelines (parameterized & looped)

Databricks transformation logic with PySpark

Partitioned & incremental data processing

Delta Lake best practices (Parquet format)

End-to-end orchestration in cloud

Business-first Power BI dashboard design


📤 How to Reproduce
Clone this repo

Upload /data/ files to Azure Data Lake Gen2

Import ADF pipelines from /adf_pipelines/

Run notebooks in /notebooks/ inside Databricks

Load Power BI from /powerbi/ and connect to Gold layer


📩 Contact
📧 rao.mohsin.54@gmail.com
🌐 LinkedIn: https://www.linkedin.com/in/mohsin-mukhtiar/
✍️ Medium

⭐ Star this repo if you found it useful!
