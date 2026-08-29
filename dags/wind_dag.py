import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.infrastructure.database import get_connection
from src.infrastructure.repository import PostgresWindTurbineRepository
from src.infrastructure.csv_loader import load_csv_to_bronze
from src.infrastructure.silver_loader import process_bronze_to_silver
from src.infrastructure.gold_loader import GoldWindAnalyticsLoader


def run_bronze():
    conn = get_connection()
    repo = PostgresWindTurbineRepository(conn)
    repo.truncate("wind_data_bronze")
    csv_name = os.environ.get("CSV_FILE", "wind_data.csv")
    load_csv_to_bronze(f"/opt/airflow/data/{csv_name}", repo)
    conn.close()


def run_silver():
    conn = get_connection()
    repo = PostgresWindTurbineRepository(conn)
    repo.truncate("wind_data_silver")
    process_bronze_to_silver(conn,repo)
    conn.close()


def run_gold():
    conn = get_connection()
    repo = PostgresWindTurbineRepository(conn)
    repo.truncate("wind_data_gold")
    gold = GoldWindAnalyticsLoader(repo)
    gold.load_gold_data()
    conn.close()


with DAG(
    dag_id="wind_analytics_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    max_active_runs=1,
) as dag:

    bronze_task = PythonOperator(task_id="bronze", python_callable=run_bronze)
    silver_task = PythonOperator(task_id="silver", python_callable=run_silver)
    gold_task = PythonOperator(task_id="gold", python_callable=run_gold)

    bronze_task >> silver_task >> gold_task
