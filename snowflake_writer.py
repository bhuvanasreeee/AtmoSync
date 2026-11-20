import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()


def create_snowflake_connection():
    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        role=os.getenv("SNOWFLAKE_ROLE")
    )


def insert_sensor_reading(connection, reading):
    cursor = connection.cursor()

    try:
        query = """
            INSERT INTO SENSOR_READINGS (
                CONTAINER_ID,
                READING_TIMESTAMP,
                TEMPERATURE_C,
                HUMIDITY_PERCENT,
                VIBRATION_LEVEL
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            reading["container_id"],
            reading["timestamp"],
            reading["temperature_c"],
            reading["humidity_percent"],
            reading["vibration_level"]
        )

        cursor.execute(query, values)
        print("Sensor reading inserted into Snowflake successfully!")

    finally:
        cursor.close()