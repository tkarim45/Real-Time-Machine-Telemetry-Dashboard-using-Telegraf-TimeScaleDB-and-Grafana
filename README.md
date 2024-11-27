<h1 align="center">Real-Time-Machine-Telemetry-Dashboard-using-Telegraf-TimeScaleDB-and-Grafana</h1>

## Overview

This project demonstrates a real-time weather analytics pipeline using the following technologies:

1. **OpenWeather API**: For fetching real-time weather data.
2. **Telegraf**: As a client library to fetch and process weather data.
3. **TimescaleDB**: A time-series database for storing and querying weather data.
4. **Grafana**: For creating a real-time, interactive dashboard to visualize weather data and analytics.

## Features

- **Data Collection**: Fetches weather data for multiple cities in real-time from the OpenWeather API.
- **Storage**: Stores processed data in TimescaleDB, optimized for time-series analysis.
- **Visualization**: Visualizes weather data in Grafana with customizable dashboards.
- **Analysis**: Provides insights like aggregated metrics for temperature, humidity, wind speed, etc.

---

## Table of Contents

- [Setup](#setup)
- [Technologies Used](#technologies-used)
- [Usage](#usage)

---

## Setup

### Prerequisites

- Python 3.8 or above
- PostgreSQL with TimescaleDB extension
- Grafana installed on your system
- API key for OpenWeather API
- `.env` file configured with the following:

  ```env
  OPENWEATHER_API_KEY=your_openweather_api_key
  PGUSER=your_postgresql_user
  PGPASSWORD=your_postgresql_password
  PGDATABASE=your_database_name
  PGPORT=db_port
  PGHOST=localhost
  PGSSLMODE=require
  ```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tkarim45/Real-Time-Machine-Telemetry-Dashboard-using-Telegraf-TimeScaleDB-and-Grafana.git
   cd weather-analytics-dashboard
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database:

   - Install TimescaleDB extension.
   - Configure the `.env` file with database credentials.

4. Set up Grafana:
   - Install the TimescaleDB plugin.
   - Connect Grafana to the TimescaleDB database.

---

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)
![Telegraf](https://img.shields.io/badge/telegraf-%2358A4B0.svg?style=for-the-badge&logo=telegraf&logoColor=white)
![TimescaleDB](https://img.shields.io/badge/timescaledb-%23316192.svg?style=for-the-badge&logo=timescaledb&logoColor=white)

---
