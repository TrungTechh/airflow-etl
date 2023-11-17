from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.apache.hive.operators.hive import HiveOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.email import EmailOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator

from datetime import datetime, timedelta
import csv
import requests
import json
from datetime import datetime

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

# Create a new Spark connection
# new_conn = Connection(
#     conn_id='spark_conn',
#     conn_type='spark',
#     host='spark://spark-master',
#     port=7077
# )

# # Add the connection to Airflow's metadata database
# session = settings.Session()
# session.add(new_conn)
# session.commit()
# session.close()


now = datetime.now()
formatted_current_date = now.strftime('%Y-%m-%d')

with DAG("bike_sales_pipeline", start_date=datetime(2023, 10 ,1), 
    schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    # creating_database = HiveOperator(
    #     task_id="creating_database",
    #     hive_cli_conn_id="hive_conn",
    #     hql="""
    #         CREATE DATABASE IF NOT EXISTS bike_store('LOCATION'='warehouse/reports'); 
    #     """
    # )

    # ingestion_brands = SparkSubmitOperator(
    #     task_id="ingestion_brands",
    #     application="/opt/airflow/dags/scripts/ingestion.py",
    #     application_args=['--tblName', 'brands', '--executionDate', formatted_current_date],
    #     conn_id="spark_conn",
    #     verbose=False
    # )

    # ingestion_categories = SparkSubmitOperator(
    #     task_id="ingestion_categories",
    #     application="/opt/airflow/dags/scripts/ingestion.py",
    #     application_args=['--tblName', 'categories', '--executionDate', formatted_current_date],
    #     conn_id="spark_conn",
    #     verbose=False
    # )

    # ingestion_products = SparkSubmitOperator(
    #     task_id="ingestion_products",
    #     application="/opt/airflow/dags/scripts/ingestion.py",
    #     application_args=['--tblName', 'products', '--executionDate', formatted_current_date],
    #     conn_id="spark_conn",
    #     verbose=False
    # )

    # ingestion_customers = SparkSubmitOperator(
    #     task_id="ingestion_customers",
    #     application="/opt/airflow/dags/scripts/ingestion.py",
    #     application_args=['--tblName', 'customers', '--executionDate', formatted_current_date],
    #     conn_id="spark_conn",
    #     verbose=False
    # )

    # ingestion_order_items = SparkSubmitOperator(
    #     task_id="ingestion_order_items",
    #     application="/opt/airflow/dags/scripts/ingestion.py",
    #     application_args=['--tblName', 'order_items', '--executionDate', formatted_current_date],
    #     conn_id="spark_conn",
    #     verbose=False
    # )

    # ingestion_orders = SparkSubmitOperator(
    #     task_id="ingestion_orders",
    #     application="/opt/airflow/dags/scripts/ingestion.py",
    #     application_args=['--tblName', 'orders', '--executionDate', formatted_current_date],
    #     conn_id="spark_conn",
    #     verbose=False
    # )

    # ingestion_staffs = SparkSubmitOperator(
    #     task_id="ingestion_staffs",
    #     application="/opt/airflow/dags/scripts/ingestion.py",
    #     application_args=['--tblName', 'staffs', '--executionDate', formatted_current_date],
    #     conn_id="spark_conn",
    #     verbose=False
    # )

    # ingestion_stocks = SparkSubmitOperator(
    #     task_id="ingestion_stocks",
    #     application="/opt/airflow/dags/scripts/ingestion.py",
    #     application_args=['--tblName', 'stocks', '--executionDate', formatted_current_date],
    #     conn_id="spark_conn",
    #     verbose=False
    # )

    # ingestion_stores = SparkSubmitOperator(
    #     task_id="ingestion_stores",
    #     application="/opt/airflow/dags/scripts/ingestion.py",
    #     application_args=['--tblName', 'stores', '--executionDate', formatted_current_date],
    #     conn_id="spark_conn",
    #     verbose=False
    # )

    # transformation = SparkSubmitOperator(
    #     task_id="transformation",
    #     application="/opt/airflow/dags/scripts/transformation.py",
    #     conn_id="spark_conn",
    #     verbose=False
    # )

    creating_database = BashOperator(
        task_id="creating_database",
        bash_command="""
            ls
        """
    )

    ingestion_brands = BashOperator(
        task_id="ingestion_brands",
        bash_command="""
            ls
        """
    )

    ingestion_categories = BashOperator(
        task_id="ingestion_categories",
        bash_command="""
            ls
        """
    )

    ingestion_products = BashOperator(
        task_id="ingestion_products",
        bash_command="""
            ls
        """
    )

    ingestion_customers = BashOperator(
        task_id="ingestion_customers",
        bash_command="""
            ls
        """
    )

    ingestion_order_items = BashOperator(
        task_id="ingestion_order_items",
        bash_command="""
            ls
        """
    )

    ingestion_orders = BashOperator(
        task_id="ingestion_orders",
        bash_command="""
            ls
        """
    )

    ingestion_staffs = BashOperator(
        task_id="ingestion_staffs",
        bash_command="""
            ls
        """
    )

    ingestion_stocks = BashOperator(
        task_id="ingestion_stocks",
        bash_command="""
            ls
        """
    )

    ingestion_stores = BashOperator(
        task_id="ingestion_stores",
        bash_command="""
            ls
        """
    )

    transformation = BashOperator(
        task_id="transformation",
        bash_command="""
            ls
        """
    )

# Set dependencies between tasks
creating_database.set_downstream(ingestion_brands)
creating_database.set_downstream(ingestion_categories)
creating_database.set_downstream(ingestion_products)
creating_database.set_downstream(ingestion_customers)
creating_database.set_downstream(ingestion_order_items)
creating_database.set_downstream(ingestion_orders)
creating_database.set_downstream(ingestion_staffs)
creating_database.set_downstream(ingestion_stocks)
creating_database.set_downstream(ingestion_stores)

ingestion_brands.set_downstream(transformation)
ingestion_categories.set_downstream(transformation)
ingestion_products.set_downstream(transformation)
ingestion_customers.set_downstream(transformation)
ingestion_order_items.set_downstream(transformation)
ingestion_orders.set_downstream(transformation)
ingestion_staffs.set_downstream(transformation)
ingestion_stocks.set_downstream(transformation)
ingestion_stores.set_downstream(transformation)