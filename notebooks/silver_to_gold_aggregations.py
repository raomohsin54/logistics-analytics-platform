# Databricks notebook source
# Replace these with your actual values
storage_account_name = "logisticsdatalake01"  # ✅ No `.dfs.core.windows.net`
access_key = "<YOUR_AZURE_ACCESS_KEY>"  # ✅ Keep it secure!

# Set configuration
spark.conf.set(
    f"fs.azure.account.key.{storage_account_name}.dfs.core.windows.net",
    access_key
)


# COMMAND ----------

from pyspark.sql.functions import col, to_timestamp, count, avg, sum, when, expr
from pyspark.sql.types import IntegerType

# Set up paths
silver = "silver"
gold = "gold"
storage = "logisticsdatalake01"  # Replace with yours

# Input paths (Silver)
shipments_path = f"abfss://{silver}@{storage}.dfs.core.windows.net/shipments"
vendors_path = f"abfss://{silver}@{storage}.dfs.core.windows.net/vendors"
routes_path = f"abfss://{silver}@{storage}.dfs.core.windows.net/routes"

# Output path (Gold)
gold_output = f"abfss://{gold}@{storage}.dfs.core.windows.net/shipment_summary"

# Read silver datasets
df_shipments = spark.read.parquet(shipments_path)
df_vendors = spark.read.parquet(vendors_path)
df_routes = spark.read.parquet(routes_path)

# Enrich shipments with calculated delay time in minutes
df_shipments = df_shipments.withColumn("Delay_Minutes", 
    (col("ArrivalTime").cast("long") - col("DepartureTime").cast("long")) / 60)

# Assume anything < 10 hours = on time (600 minutes)
df_shipments = df_shipments.withColumn("OnTime", when(col("Delay_Minutes") <= 600, 1).otherwise(0))

# Join with vendors and routes
df_joined = df_shipments.join(df_vendors, "Vendor_ID", "left") \
                        .join(df_routes, df_shipments["Origin"] != df_shipments["Destination"], "inner")

# Group and aggregate by vendor
df_summary = df_joined.groupBy("Vendor_ID", "Vendor_Name") \
    .agg(
        count("*").alias("Total_Shipments"),
        avg("Delay_Minutes").alias("Avg_Delay_Minutes"),
        expr("ROUND(100 * SUM(OnTime) / COUNT(*), 2)").alias("OnTime_Percent")
    ) \
    .orderBy(col("OnTime_Percent").desc())

# Write to gold layer
df_summary.write.mode("overwrite").parquet(gold_output)


# COMMAND ----------

# Output path
gold_output_detail = f"abfss://{gold}@{storage}.dfs.core.windows.net/shipment_detail"

# Create enriched shipment-level data
df_detail = df_shipments \
    .join(df_vendors, "Vendor_ID", "left") \
    .join(df_routes, df_shipments["Origin"] != df_shipments["Destination"], "inner") \
    .withColumn("Delay_Minutes", (col("ArrivalTime").cast("long") - col("DepartureTime").cast("long")) / 60) \
    .withColumn("OnTime", when(col("Delay_Minutes") <= 600, 1).otherwise(0)) \
    .select(
        "Shipment_ID", "Origin", "Destination",
        "DepartureTime", "ArrivalTime", "Delay_Minutes",
        "OnTime", "Vendor_ID", "Vendor_Name", "Route_Type", "Distance_KM"
    )

df_detail.write.mode("overwrite").parquet(gold_output_detail)


# COMMAND ----------

from pyspark.sql.functions import month, year

# Output path
gold_output_summary = f"abfss://{gold}@{storage}.dfs.core.windows.net/shipment_summary_by_dimensions"

df_summary = df_detail \
    .withColumn("Month", month("DepartureTime")) \
    .withColumn("Year", year("DepartureTime")) \
    .groupBy("Vendor_Name", "Route_Type", "Origin", "Destination", "Year", "Month") \
    .agg(
        count("*").alias("Total_Shipments"),
        avg("Delay_Minutes").alias("Avg_Delay_Minutes"),
        sum("OnTime").alias("OnTime_Count"),
        expr("ROUND(100 * SUM(OnTime) / COUNT(*), 2)").alias("OnTime_Percent")
    ) \
    .orderBy("Vendor_Name", "Year", "Month")

df_summary.write.mode("overwrite").parquet(gold_output_summary)
