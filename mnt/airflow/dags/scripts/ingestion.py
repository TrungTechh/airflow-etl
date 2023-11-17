from pyspark.sql import SparkSession
from pyspark.sql.functions import col, substring
from pyspark.sql.functions import lit, max

import argparse


def main(table_name, executionDate):
  
  year, month, day = executionDate.split("-")

  spark = SparkSession. \
      builder \
      .appName('Ingestion - MySQL to hdfs') \
      .getOrCreate()

  df = spark.read.format("jdbc") \
  .option("driver","com.mysql.cj.jdbc.Driver") \
  .option("url", "jdbc:mysql://mysql:3306/bike_store?zeroDateTimeBehavior=convertToNull&autoReconnect=true&characterEncoding=UTF-8&characterSetResults=UTF-8") \
  .option("dbtable", f"{table_name}") \
  .option("user", "root") \
  .option("password", "root") \
    .load()


  
  output_df = df.withColumn("year", lit(year)).withColumn("month", lit(month)).withColumn("day", lit(day))

  output_df.write.partitionBy("year","month","day").mode("overwrite").parquet(f'/datalake/{table_name}')

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Ingest data from PostgreSQL to HDFS")
    parser.add_argument("--tblName", help="Name of the MySQL table to ingest data from", required=True)
    parser.add_argument("--executionDate", help="Date to filter data by in the format 'YYYY-MM-DD'", required=True)
    args = parser.parse_args()

    # Call the main function
    main(args.tblName, args.executionDate)