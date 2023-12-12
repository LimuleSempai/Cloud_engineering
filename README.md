# Cloud Engineering Project

## Overview

This project implements a cloud-based architecture for handling and processing data, particularly focusing on ticket data ingestion, processing through Kafka, and storage in MongoDB. It includes an API server for data reception, an Admin server for data management, a Ticket Generator for simulating data, and a Kafka Consumer for data processing. The project is containerized using Docker and orchestrated with Docker Compose and in the future with Kubernetes.

## Services

- **API Server**: Receives data and publishes it to Kafka.
- **Admin Server**: Provides an interface to query and manage data in MongoDB.
- **Ticket Generator**: Generates and sends simulated ticket data.
- **Kafka Consumer**: Consumes messages from Kafka and stores them in MongoDB.
- **Kafka & Zookeeper**: Manages message queuing.
- **MongoDB**: Database for storing processed data.
- **Prometheus & Grafana**: For monitoring and visualizing metrics.

## Project Structure

```python
project_root/
│
├── api_server/
│ ├── Dockerfile
│ ├── server.py
│ └── requirements.txt
│
├── admin_server/
│ ├── Dockerfile
│ ├── admin.py
│ └── requirements.txt
│
├── ticket_generator/
│ ├── ticket_generator.py
│ └── requirements.txt
│
├── kafka_consumer/
│ ├── kafka_consumer.py
│ └── requirements.txt
│
├── k8s_configs/
│ ├── deployments/
│ ├── services/
│ └── volumes/
│
├── prometheus_config/
│ └── prometheus.yml
│
└── docker-compose.yaml
```

## Setup and Installation

### Prerequisites

- Docker and Docker Compose
- Kubernetes with Minikube or a preferred cloud provider
- Python (version as per `Dockerfile`)

### Running the Application

1. **Start Docker Containers**: Run `docker-compose up --build` in the project root.
2. **Apply Kubernetes Configurations**: Use `kubectl apply -f` for each file in `k8s_configs/`.
3. **Access Services**:
   - API Server on `localhost:8000`
   - Admin Server on `localhost:8001`
   - Prometheus on `localhost:9090`
   - Grafana on `localhost:3000`

## Usage

## Monitoring

Access Prometheus and Grafana for system monitoring. Default login for Grafana is typically `admin`/`admin`.

## License

## Contact
