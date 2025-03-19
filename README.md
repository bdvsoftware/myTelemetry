# MyTelemetry

## Description
F1 23 UDP telemetry messages sniffer and processor.

## Prerequisites
- **Set up KAFKA at port 19092**
- **KAFKA = zookeeper, schema, broker and kafka-ui (this one is optional)**

Here is a `docker-compose.yml` file which can be used to set up kafka:

```yaml
version: '3'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    container_name: zookeeper
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - "2181:2181"

  schema-registry:
    image: confluentinc/cp-schema-registry:latest
    hostname: schema-registry
    depends_on:
      - kafka
    ports:
      - "8081:8081"
    environment:
      SCHEMA_REGISTRY_HOST_NAME: schema-registry
      SCHEMA_REGISTRY_KAFKASTORE_CONNECTION_URL: 'zookeeper:2181'
      SCHEMA_REGISTRY_LISTENERS: http://schema-registry:8081
      SCHEMA_REGISTRY_KAFKASTORE_BOOTSTRAP_SERVERS: PLAINTEXT://kafka:9092,PLAINTEXT_INTERNAL://localhost:19092
      SCHEMA_REGISTRY_DEBUG: 'true'

  kafka:
    image: confluentinc/cp-kafka:latest
    hostname: kafka
    ports:
      - "19092:19092"
    depends_on:
      - zookeeper
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: 'zookeeper:2181'
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_INTERNAL:PLAINTEXT
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092,PLAINTEXT_INTERNAL://localhost:19092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1

  kafkaui:
    image: provectuslabs/kafka-ui:latest
    ports:
      - "8080:8080"
    environment:
      KAFKA_CLUSTERS_0_NAME: local
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:9092
    depends_on:
      - kafka
    links:
      - kafka
```

## Requirements
- confluent-kafka==2.8.0
- scapy==2.6.1

In order to install this requirements, please execute: 
```
pip install --no-cache-dir -r requirements.txt
```

## Installation
Follow these steps to set up the project on your local machine:

1. Clone the repository:
   ```sh
   git clone https://github.com/bdvsoftware/myTelemetry.git
   ```
2. Navigate to the project directory:
   ```sh
   cd myTelemetry
   ```

## Usage
To run the project, use the following commands:

### Ensure all previous kafka docker containers are running
```sh
docker start zookeeper
docker start kafka-1
docker start schema-registry-1
docker start kafkaui-1
```
### Run the app
```sh
python scan.py
```

### Run the F1 23 videogame by EA Sports

## Work Flow
- 1. The app will request a stint name.
- 2. All kafka messages would contain this stint name and would be sended to the topic: 
   ```sh
   mytelemetry.udp.packet.created
   ```
