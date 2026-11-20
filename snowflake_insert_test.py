from datetime import datetime, timezone

from snowflake_writer import (
    create_snowflake_connection,
    insert_sensor_reading
)

connection = None

test_reading = {
    "container_id": "TEST-CONTAINER-001",
    "timestamp": datetime.now(timezone.utc),
    "temperature_c": 5.5,
    "humidity_percent": 65.0,
    "vibration_level": 1.2
}

try:
    connection = create_snowflake_connection()

    insert_sensor_reading(connection, test_reading)

    connection.commit()
    print("Test sensor data saved in Snowflake!")

except Exception as error:
    if connection:
        connection.rollback()
    print("Insertion failed:", error)

finally:
    if connection:
        connection.close()