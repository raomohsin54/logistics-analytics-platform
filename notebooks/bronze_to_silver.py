# Databricks notebook source
# Set fixed container names
bronze_container = "bronze"
silver_container = "silver"
storage_account_name = "logisticsdatalake01"  # Replace with your actual name

# No 'abfss:' in container variable!
drivers_path = f"abfss://{bronze_container}@{storage_account_name}.dfs.core.windows.net/drivers.csv"
drivers_output = f"abfss://{silver_container}@{storage_account_name}.dfs.core.windows.net/drivers"


# COMMAND ----------

# Set credentials securely (run only once per notebook)
spark.conf.set(
  f"fs.azure.account.key.{storage_account_name}.dfs.core.windows.net",
  "<YOUR_AZURE_ACCESS_KEY>"
)

# Read from bronze
df_drivers = spark.read.option("header", True).csv(drivers_path)

# Clean and rename columns
df_drivers_clean = df_drivers \
    .withColumnRenamed("DriverID", "Driver_ID") \
    .withColumnRenamed("Name", "Driver_Name") \
    .withColumnRenamed("ExperienceYears", "Experience_Years")

# Write to silver
df_drivers_clean.write.mode("overwrite").parquet(drivers_output)



# COMMAND ----------

routes_path = f"abfss://{bronze_container}@{storage_account_name}.dfs.core.windows.net/routes.csv"
routes_output = f"abfss://{silver_container}@{storage_account_name}.dfs.core.windows.net/routes"

df_routes = spark.read.option("header", True).csv(routes_path)

df_routes_clean = df_routes \
    .withColumnRenamed("RouteID", "Route_ID") \
    .withColumnRenamed("DistanceKM", "Distance_KM") \
    .withColumnRenamed("AverageTimeMin", "Average_Time_Min") \
    .withColumnRenamed("RouteType", "Route_Type")

df_routes_clean.write.mode("overwrite").parquet(routes_output)


# COMMAND ----------

vendors_path = f"abfss://{bronze_container}@{storage_account_name}.dfs.core.windows.net/vendors.csv"
vendors_output = f"abfss://{silver_container}@{storage_account_name}.dfs.core.windows.net/vendors"

df_vendors = spark.read.option("header", True).csv(vendors_path)

df_vendors_clean = df_vendors \
    .withColumnRenamed("VendorID", "Vendor_ID") \
    .withColumnRenamed("VendorName", "Vendor_Name") \
    .withColumnRenamed("SLACompliance%", "SLA_Compliance_Percent") \
    .withColumnRenamed("ContactPerson", "Contact_Email")

df_vendors_clean.write.mode("overwrite").parquet(vendors_output)


# COMMAND ----------

from pyspark.sql.functions import to_timestamp

shipments_path = f"abfss://{bronze_container}@{storage_account_name}.dfs.core.windows.net/shipments.csv"
shipments_output = f"abfss://{silver_container}@{storage_account_name}.dfs.core.windows.net/shipments"

df_shipments = spark.read.option("header", True).csv(shipments_path)

df_shipments_clean = df_shipments \
    .withColumn("DepartureTime", to_timestamp("DepartureTime")) \
    .withColumn("ArrivalTime", to_timestamp("ArrivalTime")) \
    .withColumnRenamed("ShipmentID", "Shipment_ID") \
    .withColumnRenamed("VendorID", "Vendor_ID")

df_shipments_clean.write.mode("overwrite").parquet(shipments_output)
