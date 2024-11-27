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
- [Docker](#docker)

---

## Setup

### Prerequisites

- Python 3.9 or above
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

### Setup Telegraf

1. Install Telegraf:

   ```bash
   sudo apt-get update
   sudo apt-get install telegraf
   ```

2. Configure Telegraf:

   - Replace the contents of the `telegraf.conf` file with the contents of `telegraf.conf` in this repository.
   - Update the `urls` field in the `[[inputs.openweathermap]]` section with the cities you want to fetch weather data for.
   - Update the `database` field in the `[[outputs.postgresql]]` section with your TimescaleDB database name.

3. Start the Telegraf service:

   ```bash
    sudo service telegraf start
   ```

### Setup Grafana

1. Start the Grafana server:

   ```bash
   sudo service grafana-server start
   ```

2. Open Grafana in your browser:

   ```bash
    http://localhost:3000
   ```

3. Log in with the default credentials:

   - Username: `admin`
   - Password: `admin`

4. Add the TimescaleDB data source:

- Go to `Configuration > Data Sources`.
- Click on `Add data source`.
- Select `Postgresql` from the list of data sources.
- Configure the data source with the following credentials:

  - Host: `timescaledb`
  - Database: `weather`
  - User: `postgres`
  - Password: `password`

---

## Docker

### Prerequisites

- Docker installed on your system
- Docker Compose installed on your system

### Usage

1. Build the Docker containers:

   ```bash
   docker compose up -d
   ```

---

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)
![Telegraf](https://img.shields.io/badge/telegraf-%2358A4B0.svg?style=for-the-badge&logo=telegraf&logoColor=white)
![TimescaleDB](https://img.shields.io/badge/timescaledb-%23316192.svg?style=for-the-badge&logo=timescaledb&logoColor=white)

---
