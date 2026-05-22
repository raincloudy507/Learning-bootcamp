# Table of Contents
1. [Project Architecture](#Project-Architecture)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Setup](#setup)
	- [Docker Setup](#docker-setup)
5. [DAG (Directed Acyclic Graph) Flow](#dag-flow)
6. [Screenshots](#screenshots)
7. [Future Enhancements](#future-enhancements)

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
| Workflow Orchestration | Apache Airflow |
| Containerization      | Docker & Docker Compose |
| Programming Language  | Python 3.12 |
| Database              | PostgreSQL |
| Data Processing       | Pandas |
| API Integration       | Requests |
| ORM / Database Access | SQLAlchemy |
| Development Platform  | GitHub Codespaces |
| Version Control       | Git & GitHub |
| Operating Environment | Linux Containers |

## Setup

### Prerequisites

Ensure the following tools are installed on your machine:

- Docker Desktop
- Docker Compose
- Git

### Clone the Repository

```
git clone <your-github-repo-url>
cd airflow-weather-pipeline
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