import pandas as pd

def transform_weather():

    df = pd.read_csv("/opt/airflow/data/raw_weather.csv")

    df.columns = [c.lower() for c in df.columns]

    df["temperature_fahrenheit"] = (
        df["temperature_2m_max"] * 9/5 + 32
    )

    df.to_csv("/opt/airflow/data/processed_weather.csv", index=False)

    print("Transformation complete")