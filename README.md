AtmoSync

AtmoSync is a data analytics project that monitors environmental conditions during the transportation of perishable goods. It analyzes temperature, humidity, and vibration data to identify spoilage risks and explore rerouting opportunities. Using Python, Kafka, Snowflake, dbt, SQL, and Superset, it transforms data into insights and visual dashboards.

Current Development: Python IoT Simulator

The Python IoT simulator generates simulated sensor readings for multiple containers.

Sensor Parameters

- Container ID
- Timestamp
- Temperature (°C)
- Humidity (%)
- Vibration level

Project Structure

AtmoSync/
├── data/
│   └── sensor_readings.jsonl
├── docs/
├── src/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

Setup Instructions

1. Clone the repository:

git clone https://github.com/bhuvanasreeee/AtmoSync.git

2. Open the project folder:

cd AtmoSync

3. Create a virtual environment:

python -m venv venv

4. Activate the virtual environment on Windows:

venv\Scripts\activate

5. Install dependencies:

pip install -r requirements.txt

Run the Simulator

Execute:

python main.py

The simulator continuously generates readings for three containers.

Press "CTRL + C" to stop the simulator.

Data Storage

Generated and validated sensor readings are stored locally in:

data/sensor_readings.jsonl

Each line contains one JSON sensor reading.

Data Validation

The simulator checks:

- Missing required fields.
- Invalid container IDs.
- Invalid timestamps.
- Non-numeric sensor values.
- Values outside the simulator's configured ranges.

Current Progress

- Python project environment configured.
- IoT sensor data simulator developed.
- Multiple container simulation implemented.
- Sensor data validation implemented.
- JSONL data storage implemented.
- Simulator testing completed.
- Apache Kafka 4.4.0 setup completed.
- Kafka broker started successfully.
- Kafka topic `container-sensor-events` created successfully.
- Python Kafka library (kafka-python) installed.
- Python Kafka producer developed.
- IoT simulator connected to Kafka topic `container-sensor-events`.
- Sensor data transmission to Kafka tested successfully.
- Python Kafka consumer developed.
- Kafka consumer connected to `container-sensor-events`.
- Incoming sensor messages received successfully.
- Sensor data validation performed by the consumer.
- Kafka producer-consumer communication tested successfully.
- Snowflake account activated and configured.
- Created Snowflake database `ATMOSYNC_DB`.
- Created `RAW` schema.
- Created `SENSOR_READINGS` table for raw sensor data.
- Created `COMMODITY_PRICES` table for raw commodity pricing data.
- Verified both table structures using DESCRIBE TABLE.
- Snowflake Python connector configured successfully.
- Kafka consumer connected to Snowflake.
- Sensor readings inserted into the Snowflake SENSOR_READINGS table.
- Sensor data ingestion verified by querying Snowflake.
- Snowflake connection established from Python.
- Kafka consumer integrated with Snowflake.
- Sensor readings successfully inserted into the SENSOR_READINGS table.
- Mock commodity pricing data prepared and inserted into the COMMODITY_PRICES table.
- Verified sensor readings and commodity pricing records using Snowflake SQL queries.

Future Development

- Snowflake data storage.
- dbt-based data transformation.
- SQL analytics.
- Apache Superset dashboards.

---

Project: AtmoSync – Micro-Climate Arbitrage Analytics