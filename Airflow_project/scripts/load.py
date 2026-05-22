import pandas as pd
from sqlalchemy import create_engine

def load_weather():

    df = pd.read_csv("/opt/airflow/data/processed_weather.csv")

    engine = create_engine(
        "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"
    )

    df.to_sql(
        "weather_data",
        engine,
        if_exists="append",
        index=False
    )

    print("Load complete")