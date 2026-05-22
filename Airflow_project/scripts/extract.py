import requests
import pandas as pd

def extract_weather():

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=43.65"
        "&longitude=-79.38"
        "&daily=temperature_2m_max"
        "&timezone=auto"
    )

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data["daily"])

    df.to_csv("/opt/airflow/data/raw_weather.csv", index=False)

    print("Extraction complete")