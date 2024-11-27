import pandas as pd
from datetime import datetime


def fetch_latest_databy_city_date(city, date, df):
    """
    This function fetches the latest data for a specific city and date

    Args:
        city: str: the city for which you want to fetch the data
        date: str: the date for which you want to fetch the data
        df: pd.DataFrame: the DataFrame containing the data

    Returns:
        pd.DataFrame: the latest data for the specified city and date

    """

    df_copy = df.copy()
    df_copy = df_copy[df_copy["city"] == city]
    df_copy = df_copy[df_copy["time"] > pd.Timestamp(datetime.now().date())]
    df_copy = df_copy.sort_values("time", ascending=False)
    return df_copy


def fetch_avg_metrics(city, df):
    """
    This function fetches the average metrics for a given city from the DataFrame.
    The average metrics are calculated for the following columns:
    - temperature
    - humidity
    - pressure
    - wind_speed
    - cloudiness

    Args:
        city (str): The city for which the metrics are to be fetched
        df (DataFrame): The DataFrame containing the metrics

    Returns:
        DataFrame: The DataFrame containing the average metrics for the given city
    """

    df_copy = df.copy()
    df_copy = df_copy[df_copy["city"] == city]
    avg_metrics = df_copy[
        ["temperature", "humidity", "pressure", "wind_speed", "cloudiness"]
    ].mean()
    # change the column names to reflect the average values
    avg_metrics.index = [
        "avg_temperature",
        "avg_humidity",
        "avg_pressure",
        "avg_wind_speed",
        "avg_cloudiness",
    ]
    return avg_metrics


def fetch_max_min_metrics(city, df):
    """
    This function fetches the maximum and minimum metrics for a given city from the DataFrame.
    The maximum and minimum metrics are calculated for the following columns:
    - temperature
    - humidity
    - pressure
    - wind_speed
    - cloudiness

    Args:
        city (str): The city for which the metrics are to be fetched
        df (DataFrame): The DataFrame containing the metrics

    Returns:
        DataFrame: The DataFrame containing the maximum and minimum metrics for the given city
    """

    df_copy = df.copy()
    df_copy = df_copy[df_copy["city"] == city]

    max_min_metrics = pd.DataFrame(
        {
            "max_temperature": [df_copy["temperature"].max()],
            "min_temperature": [df_copy["temperature"].min()],
            "max_humidity": [df_copy["humidity"].max()],
            "min_humidity": [df_copy["humidity"].min()],
            "max_pressure": [df_copy["pressure"].max()],
            "min_pressure": [df_copy["pressure"].min()],
            "max_wind_speed": [df_copy["wind_speed"].max()],
            "min_wind_speed": [df_copy["wind_speed"].min()],
            "max_cloudiness": [df_copy["cloudiness"].max()],
            "min_cloudiness": [df_copy["cloudiness"].min()],
        }
    )

    return max_min_metrics


def fetech_latest_metrics(city, df):
    """
    This function fetches the latest metrics for a given city from the DataFrame.
    The latest metrics are the metrics for the most recent timestamp for the given city.
    The latest metrics are calculated for the following columns:
    - temperature
    - humidity
    - pressure
    - wind_speed
    - cloudiness

    Args:
        city (str): The city for which the metrics are to be fetched
        df (DataFrame): The DataFrame containing the metrics

    Returns:
        DataFrame: The DataFrame containing the latest metrics for the given city
    """

    df_copy = df.copy()
    df_copy = df_copy[df_copy["city"] == city]
    latest_metrics = df_copy.head(1)[
        ["temperature", "humidity", "pressure", "wind_speed", "cloudiness"]
    ]
    # change the column names to indicate that these are the latest metrics
    latest_metrics.columns = [
        "latest_temperature",
        "latest_humidity",
        "latest_pressure",
        "latest_wind_speed",
        "latest_cloudiness",
    ]
    return latest_metrics


def fetch_all_metrics(city, df):
    """
    Fetch all metrics (latest, average, max/min) for a specific city.
    """
    # Filter once and reuse
    today = pd.Timestamp(datetime.now().date())
    latest_data = fetch_latest_databy_city_date(city, today, df)

    if latest_data.empty:
        return {city: "No data available for the specified date and city."}

    avg_metrics = fetch_avg_metrics(city, latest_data)
    max_min_metrics = fetch_max_min_metrics(city, latest_data)
    latest_metrics = fetech_latest_metrics(city, latest_data)

    metrics = {
        city: {
            **avg_metrics.to_dict(),
            **max_min_metrics.iloc[0].to_dict(),
            **latest_metrics.iloc[0].to_dict(),
        }
    }
    return metrics
