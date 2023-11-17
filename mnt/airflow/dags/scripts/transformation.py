from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, substring, lit, max, year, month, round

from datetime import datetime

now = datetime.now()
formatted_current_date = now.strftime('%Y-%m-%d')

#init spark session
spark = SparkSession.builder.appName("Bike Revenue Report") \
    .config("spark.sql.warehouse.dir", 'hdfs://namenode:9000/datawarehouse')\
    .config('hive.exec.dynamic.partition','true') \
    .config('hive.exec.dynamic.partition.mode', 'nonstrict') \
    .enableHiveSupport().getOrCreate()

#Read data
brandsDF = spark.read.parquet('/datalake/brands').drop('year','month','day')
categories = spark.read.parquet('/datalake/categories').drop('year','month','day')
customers = spark.read.parquet('/datalake/customers').drop('year','month','day')
order_items = spark.read.parquet('/datalake/order_items').drop('year','month','day')
orders = spark.read.parquet('/datalake/orders').drop('year','month','day')
products = spark.read.parquet('/datalake/products').drop('year','month','day')
staffs = spark.read.parquet('/datalake/staffs').drop('year','month','day')
stocks = spark.read.parquet('/datalake/stocks').drop('year','month','day')
stores = spark.read.parquet('/datalake/stores').drop('year','month','day')

#select product with categories
product_categories = products.filter(products['created_at'] <= (formatted_current_date + ' 23:59:00')) \
                    .join(categories, categories['category_id'] == products['category_id'], "inner")

#revenue of product in month of year
product_sales_ym = orders.join(order_items, order_items['order_id'] == orders['order_id'], "inner") \
                    .withColumn("year", year(col("order_date"))) \
                    .withColumn("month", month(col("order_date"))) \
                    .groupBy("year","month","product_id") \
                    .agg(sum("quantity").alias("units_sold"))

#revenue of each categories in month
avg_units = product_sales_ym.join(product_categories, product_categories['product_id'] == product_sales_ym['product_id'],"inner") \
            .groupBy("month","category_name") \
            .agg( round(avg("units_sold"),2).alias("avg_units_sold"))


#store to hdfs
avg_units.write.partitionBy("month").option("path", "hdfs://localhost:9000/datawarehouse").mode("overwrite").saveAsTable('bike_store.monthly_units_revenue')