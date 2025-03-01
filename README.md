### Spark Ecosystem Cluster 🚀🔥

Welcome to **Spark Ecosystem**, a fully operational local setup to experiment with a Spark-based ecosystem. This project leverages `docker-compose` to create a cluster with Spark, Kafka, LocalStack, RabbitMQ, PostgreSQL, Hive, Airflow, and other supporting tools—all running locally! 🐳✨

---

## Features ✨

- **Apache Spark**: A Spark master and two workers to execute distributed computations.
- **Kafka**: Message streaming with Kafka, including topic initialization.
- **Hive Metastore**: Centralized metadata storage for Spark SQL.
- **LocalStack**: Mock AWS services for development and testing (e.g., S3, SQS, Events).
- **RabbitMQ**: Message broker for your pub/sub or task queue needs.
- **PostgreSQL**: RDBMS support for applications like Hive and Airflow.
- **Airflow**: Workflow orchestration made easy.
- **Superset**: Data visualization and dashboarding tool.
- **Jupyter**: Interactive notebooks for data exploration with PySpark.
- **Prometheus & Grafana**: Monitoring and visualization of your cluster.

---

## Architecture 🏛️

Here's a simplified text-based diagram representing the cluster architecture:

```plaintext
+---------------------+    +---------------------+    +---------------------+
|   Spark Master      |    |   Spark Worker A    |    |   Spark Worker B    |
| (spark-master:9090) |    | (spark-worker-a:9091)|    | (spark-worker-b:9093)|
+---------+-----------+    +---------+-----------+    +---------+-----------+
          |                        |                        |
          +------------------------+------------------------+
                      | Spark Cluster Network (spark-kafka) |
                      |                                    |
+---------------------+    +---------------------+    +---------------------+
|     Kafka           |    |   Hive Metastore    |    |   PostgreSQL        |
|   (kafka:9092)      |    | (hive-metastore:9083)|    | (postgres:5432)     |
+---------+-----------+    +---------+-----------+    +---------+-----------+
          |                        |                        |
          +------------------------+------------------------+
                      | Infrastructure Services            |
                      |                                    |
+---------------------+    +---------------------+    +---------------------+
|   LocalStack        |    |   RabbitMQ          |    |   Airflow           |
| (localstack:4566)   |    | (rabbitmq:5672/15672)|    | (airflow-webserver:8080)|
+---------+-----------+    +---------+-----------+    +---------+-----------+
          |                        |                        |
          +------------------------+------------------------+
                      | Monitoring & Data Exploration      |
                      |                                    |
+---------------------+    +---------------------+    +---------------------+
|   Prometheus        |    |   Grafana           |    |   Jupyter           |
| (prometheus:19090)  |    | (grafana:3000)      |    | (jupyter:8888)      |
+---------------------+    +---------------------+    +---------------------+
|     Superset        |
|   (superset:8081)   |
+---------------------+

```

Note: Ports shown are host ports. Container ports might differ but are mapped accordingly.  All services communicate within the `spark-kafka` Docker network.

---

## Use Cases and Examples 🚀

This cluster is designed for learning and experimentation. Here are a few examples of what you can do:

* **Run PySpark jobs in Jupyter Notebook:**
   *   Access Jupyter at [http://localhost:8888](http://localhost:8888).
   *   Create a new PySpark notebook and start experimenting with Spark DataFrames, SQL, and MLlib.
   *   Example PySpark code (you can run this in Jupyter):

    ```python
    from pyspark.sql import SparkSession
    import time

    spark = SparkSession.builder.appName("EasyApp").getOrCreate()

    data = [("Anna", 25), ("Peter", 40), ("Joan", 35), ("Maria", 28)]
    columns = ["Name", "Age"]

    df = spark.createDataFrame(data, columns)

    df.show()

    filtered_df = df.filter(df.Age > 30)

    filtered_df.show()
    time.sleep(300) # Keep app running for UI exploration

    spark.stop()
    ```

*  **Stream data with Kafka and process with Spark Streaming:**
   *   Kafka is running and topics can be created using the `init-kafka` service.
   *   You can produce and consume messages to Kafka topics from Spark Streaming applications running in Jupyter or via `spark-submit`.

*  **Query data using Spark SQL and Hive Metastore:**
   *   Hive Metastore is configured to use PostgreSQL as the backend.
   *   You can create tables in Hive Metastore and query them using Spark SQL through Jupyter or Spark Thrift Server.
   *   Connect to Spark Thrift Server ( `localhost:10000` ) using tools like Beeline or JDBC/ODBC clients.

*  **Visualize data with Superset:**
   *   Access Superset at [http://localhost:8081](http://localhost:8081).
   *   Connect Superset to Spark Thrift Server or directly to PostgreSQL to create dashboards and visualizations.

*  **Experiment with AWS services locally using LocalStack:**
   *   LocalStack provides mock AWS services like S3, SQS, and Events.
   *   Configure Spark to use S3-like storage pointing to LocalStack endpoint ( `http://localhost:4566` ).
   *   Use the provided SQS scripts in the `sqs/` directory to interact with mock SQS queues.

*  **Orchestrate workflows with Airflow:**
   *   Access Airflow at [http://localhost:8080](http://localhost:8080).
   *   Create and schedule DAGs to orchestrate Spark jobs, data pipelines, or other tasks within the ecosystem.

---

## Getting Started 🛠️

### Prerequisites 📝

Ensure you have the following installed:

- Docker 🐋
- Docker Compose 📦

### Setup & Run ▶️

1.  Clone this repository:
    ```bash
    git clone [git@github.com:cherrera20/spark-ecosystem-cluster.git](git@github.com:cherrera20/spark-ecosystem-cluster.git)
    cd spark-ecosystem-cluster
    ```

2.  Build and start the services:
    ```bash
    docker compose up --build
    ```

3.  Access the services using their respective URLs/Ports:

    | Service             | URL/Port                                        |
    |--------------------------------------------------|---------------------|
    | Spark Master        | [http://localhost:9090](http://localhost:9090)   |
    | Spark Worker A      | [http://localhost:9091](http://localhost:9091)   |
    | Spark Worker B      | [http://localhost:9093](http://localhost:9093)   |
    | Kafka               | [http://localhost:9092](localhost:9092)          |
    | Hive Metastore      | [http://localhost:9093](localhost:9083)          |
    | Airflow             | [http://localhost:8080](http://localhost:8080)   |
    | Superset            | [http://localhost:8081](http://localhost:8081)   |
    | Grafana             | [http://localhost:3000](http://localhost:3000)   |
    | Prometheus          | [http://localhost:19090](http://localhost:19090) |
    | Jupyter Notebook    | [http://localhost:8888](http://localhost:8888)   |

4.  **Stopping the cluster:** To stop and remove all containers, networks and volumes defined in `docker-compose.yml`, run:

    ```bash
    docker compose down
    ```

---

## Directory Structure 🗂️

```plaintext
.
├── docker-compose.yml         # Compose file defining the ecosystem
├── spark/                     # Spark configurations and Dockerfiles
├── data/                      # Data storage for Hive and Spark
├── notebooks/                 # Jupyter notebooks for PySpark experiments
├── prometheus/                # Prometheus configuration
├── superset/                  # Superset setup
├── airflow-data/              # Airflow DAGs, logs, and config
├── hive/                      # Hive-specific configurations
├── sqs/                       # Scripts for interacting with mock SQS (LocalStack)
├── config/                    # (New) For storing service-specific config files (future improvement)
├── docs/                      # (New) For more extensive documentation (future improvement)
├── scripts/                   # (New) Utility scripts (future improvement)
```

**Note:**  The `config/`, `docs/`, and `scripts/` directories are currently empty and are suggested for future organizational improvements.

---

## Customization ⚙️

*  **Spark Configuration:**
   *   Modify `spark/config/spark-defaults.conf` (you might need to create the `config/` directory first) to adjust Spark settings like memory allocation, cores, etc.
   *   Edit `spark/config/metrics.properties` for Prometheus monitoring configuration.

*  **Kafka Topics:**
   *   Kafka topics are initialized by the `init-kafka` service in `docker-compose.yml`.
   *   Modify the `command` section of the `init-kafka` service in `docker-compose.yml` to create different or additional Kafka topics upon cluster startup.

*  **Service Ports:**
   *   Service ports are defined in the `ports` section of each service in `docker-compose.yml`.
   *   Change the host ports (e.g., `9090:8080` -  `9090` is the host port) in `docker-compose.yml` if you need to avoid conflicts with other applications running on your host machine. **Be careful not to change the container ports (e.g., `8080` in `9090:8080`) unless you know what you are doing.**

*  **Environment Variables:**
   *   Many services are configured via environment variables in `docker-compose.yml`.
   *   Adjust environment variables in the `environment` section of each service to customize service behavior (e.g., Spark worker memory, Kafka settings, database credentials, etc.).

---

## Troubleshooting 🐛

*   **Port Conflicts:** If you encounter errors related to ports already being in use, modify the host ports in the `docker-compose.yml` file as described in the "Customization" section.

*   **Service Startup Issues:** Check the logs of the failing service using `docker-compose logs <service_name>`.  Common issues might be related to:
   *   **Dependencies not met:** Ensure services are started in the correct order (check `depends_on` in `docker-compose.yml`).
   *   **Configuration errors:** Double-check configuration files (e.g., `hive-site.xml`, `prometheus.yml`, `docker-compose.yml`) for typos or incorrect settings.
   *   **Resource limits:**  If your system has limited resources, try reducing resource allocation for services (e.g., Spark worker memory, cores) in `docker-compose.yml`.

*   **Jupyter Connection Issues:** If you cannot connect to the Spark context from Jupyter notebooks, ensure:
   *   The Spark Master service is running correctly.
   *   The `SPARK_MASTER` environment variable in the `jupyter` service in `docker-compose.yml` is correctly set to `spark://spark-master:7077`.
   *   There are no network connectivity issues between Jupyter and Spark Master containers (they should be in the same `spark-kafka` network).

---

## Contributing 🤝

If you'd like to contribute to this project, feel free to:

*   **Report issues:** If you find bugs or unexpected behavior, please open an issue on GitHub.
*   **Suggest enhancements:**  If you have ideas for new features or improvements, please open an issue or submit a pull request.
*   **Submit pull requests:**  If you've implemented a fix or a new feature, submit a pull request with a clear description of your changes.

---

## Purpose and Scope 🎯

This project is intended for **local learning and testing purposes**. It provides a complete Spark ecosystem setup running locally using Docker Compose.  It's designed to be a convenient and isolated environment for:

*   Learning about Apache Spark and its ecosystem components (Kafka, Hive, etc.).
*   Experimenting with different Spark configurations and workloads.
*   Developing and testing Spark applications locally before deploying to production environments.
*   Exploring data visualization with Superset and workflow orchestration with Airflow in a Spark context.

**Limitations:**

*   This is a **local development environment** and is **not intended for production use**.
*   Performance may be limited by the resources of your local machine.
*   Security configurations are simplified for local development and are not production-grade.
