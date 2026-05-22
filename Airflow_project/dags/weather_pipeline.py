from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from Airflow_project.scripts.extract import extract_weather
from Airflow_project.scripts.transform import transform_weather
from Airflow_project.scripts.load import load_weather

default_args = {
    "owner": "Apache Airflow",
    "retries": 2,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="weather_pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["portfolio", "etl"]
) as dag:

    extract_task = PythonOperator(
        task_id="extract_weather",
        python_callable=extract_weather
    )

    transform_task = PythonOperator(
        task_id="transform_weather",
        python_callable=transform_weather
    )

    load_task = PythonOperator(
        task_id="load_weather",
        python_callable=load_weather
    )

    extract_task >> transform_task >> load_task