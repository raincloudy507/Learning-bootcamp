# Table of Contents
1. [Project Architecture](#Project-Architecture)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Setup](#setup)
5. [DAG (Directed Acyclic Graph) Flow](#dag-flow)

# Project Architecture
## Architecture Overview
Simulates a prod-style ETL platform using : 
- Apache Airflow for orchestration
- Docker and Docker Compose for containerized deployment
- PostgreSQL for metadata and pipeline storage
- Python + Pandas for data processing
- Open-Meteo public API for external data ingestion

The pipeline performs : 
1. API extraction
2. Data transformation
3. Database loading
4. Scheduled orchestration via Airflow DAGs

## Architecture Diagrams
### Airflow Architecture
![alt text](/Airflow_project/images/Airflow_arch.png)

### Docker Container Architecture
![alt text](/Airflow_project/images/Airflow_DCA.png)

# Features

- End-to-end ETL pipeline orchestration using Apache Airflow
- Dockerized multi-container architecture using Docker Compose
- Automated weather data ingestion from the Open-Meteo public API
- Data transformation and cleansing using Pandas
- PostgreSQL integration for persistent structured storage
- Modular Airflow DAG design with reusable Python scripts
- Production-style workflow scheduling and task orchestration
- Retry handling and task dependency management
- Local development and execution without requiring cloud infrastructure
- GitHub Codespaces compatible setup for cloud-based development
- Persistent logging and mounted Docker volumes
- Airflow Web UI for workflow monitoring and execution tracking
- Easy-to-extend architecture for additional data sources and pipelines

# Tech Stack


| Category              | Technology |
|----------------------|------------|
| Workflow Orchestration | [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/index.html) |
| Containerization      | [Docker](https://docs.docker.com/desktop/) & [Docker Compose](https://docs.docker.com/compose/) |
| Programming Language  | [Python 3.12](https://docs.python.org/3.12/) |
| Database              | [PostgreSQL](https://www.postgresql.org/docs/) |
| Data Processing       | [Pandas](https://pandas.pydata.org/docs/user_guide/index.html) |
| API Integration       | [Requests](https://pypi.org/project/requests/) |
| ORM / Database Access | [SQLAlchemy](https://docs.sqlalchemy.org/en/20/) |
| Development Platform  | [GitHub Codespaces](https://github.com/features/codespaces) |
| Version Control       | [Git](https://git-scm.com/docs) & [GitHub](https://docs.github.com/en) |
| Operating Environment | [Linux Containers](https://linuxcontainers.org/) |

## Setup

### Prerequisites

Ensure the following tools are installed on your machine:

- Docker Desktop
- Docker Compose
- Git

### Clone the Repository

```
git clone https://github.com/raincloudy507/Learning-bootcamp.git
cd Airflow_project
```

### Create Required Folders
```
mkdir -p dags logs plugins data scripts
```

### Configure Environment Variables
Create a .env file in the project root with the below content :
```
AIRFLOW_UID=50000
```

### Start the application
Build and start all the containers :
```
docker compose up --build
```

### Access Airflow UI
Open the Airflow web interface:
```
http://localhost:8080
```

### Default Login Credentials
```
Username: admin
Password: admin
```

### Trigger the DAG
1. Open the Airflow UI
2. Enable the weather_pipeline DAG
3. Trigger the DAG manually
4. Monitor task execution in Graph View

### Stop the Application
```
docker compose down
```

### Rebuild the containers (optional)
```
docker compose down -v
docker compose up --build
```

# DAG (Directed Acyclic Graph) Flow
## DAG Flow

The `weather_pipeline` DAG orchestrates an end-to-end ETL workflow that ingests weather forecast data from an external API, processes the dataset, and stores the transformed output into a PostgreSQL database.

The workflow is designed using Apache Airflow task dependencies to simulate a production-style data engineering pipeline.

### DAG Workflow

```text
extract_weather
       |
       v
transform_weather
       |
       v
load_weather
```

## Task Breakdown
1. Extract Weather Data (Task : ```extract_weather```)
- Connects to the Open-Meteo public weather API
- Retrieves daily weather forecast data
- Converts the API response into a structured Pandas DataFrame
- Stores the raw dataset as a CSV file for downstream processing

Output:
data/raw_weather.csv

2. Transform Weather Data (Task : ```transform_weather```)
- Reads the raw weather dataset
- Standardizes column names
- Performs basic data cleansing and transformation
- Converts temperature data from Celsius to Fahrenheit
- Creates a processed dataset ready for storage

Output:
data/processed_weather.csv

3. Load Weather Data (Task : ```load_weather```)
- Reads the processed dataset
- Establishes a connection to PostgreSQL using SQLAlchemy
- Loads transformed records into the weather_data database table
- Supports append-based incremental loading

Target Table:
weather_data

## DAG features
- Capability to schedule Daily execution using Airflow scheduling
- Modular Python-based task implementation
- Retry and failure handling support
- Sequential task dependency management
- Dockerized execution environment
- Persistent storage using PostgreSQL

## Operational Flow
1. Airflow Scheduler triggers the DAG
2. The Extract task pulls weather data from the API
3. The Transform task processes and enriches the dataset
4. The Load task stores the final dataset into PostgreSQL
5. Airflow logs and monitors execution through the Web UI
