# Healthcare Patient Monitoring System

A multi-database healthcare system for real-time patient monitoring, analytics, and alerting.  
**Technologies:** MongoDB, InfluxDB/TimescaleDB, Neo4j, Cassandra, Redis, Python.

## Features

- Store patient profiles (MongoDB)
- Real-time body measurements (InfluxDB)
- Doctor-patient relationships (Neo4j)
- Patient data analytics (Cassandra)
- Abnormal readings & alerts (Redis)
- Region-based partitioning, high availability, replication, and fault tolerance

## Getting Started

### Prerequisites

- Python 3.9+
- Docker or local instances for MongoDB, InfluxDB, Cassandra, Neo4j, Redis
- `pip install -r requirements.txt`

### Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/0Qusay0Alawneh0/Healthcare-Patient-Monitoring-System.git
   cd Healthcare-Patient-Monitoring-System
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure database connection strings in `/src/config.py` as needed.

4. Run sample scripts in `/src` to test DB functionality.

## Structure

```
/src
  patients.py         # MongoDB – Patient info CRUD
  measurements.py     # InfluxDB – Real-time measurements
  relationships.py    # Neo4j – Doctor-patient graph
  analytics.py        # Cassandra – Data analytics
  alerts.py           # Redis – Alerts & notifications
  config.py           # DB configs
/config
  mongo_init.js
  influxdb_init.txt
  neo4j_init.txt
  cassandra_init.cql
requirements.txt
README.md
```

## Demo

See the `presentation.pptx` for a walkthrough of architecture, features, and code.

## License

MIT

---
