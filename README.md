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

Future Development

- Apache Kafka data streaming.
- Snowflake data storage.
- dbt-based data transformation.
- SQL analytics.
- Apache Superset dashboards.

---

Project: AtmoSync – Micro-Climate Arbitrage Analytics