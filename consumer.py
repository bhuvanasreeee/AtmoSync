import json
import math
from datetime import datetime
from kafka import KafkaConsumer

KAFKA_TOPIC = "container-sensor-events"
KAFKA_SERVER = "localhost:9092"
def validate_sensor_reading(reading):
    errors = []

    required_fields = [
        "container_id",
        "timestamp",
        "temperature_c",
        "humidity_percent",
        "vibration_level"
    ]

    if not isinstance(reading, dict):
        return ["Reading must be a JSON object."]

    for field in required_fields:
        if field not in reading:
            errors.append(f"Missing field: {field}")

    if errors:
        return errors

    if not isinstance(reading["container_id"], str) or not reading["container_id"].strip():
        errors.append("Invalid container ID.")

    try:
        datetime.fromisoformat(reading["timestamp"])
    except (ValueError, TypeError):
        errors.append("Invalid timestamp.")

    sensor_ranges = {
        "temperature_c": (2.0, 10.0),
        "humidity_percent": (50.0, 90.0),
        "vibration_level": (0.1, 5.0)
    }

    for field, (minimum, maximum) in sensor_ranges.items():
        value = reading[field]

        if isinstance(value, bool) or not isinstance(value, (int, float)):
            errors.append(f"{field} must be a number.")
        elif not math.isfinite(value):
            errors.append(f"{field} must be finite.")
        elif not minimum <= value <= maximum:
            errors.append(f"{field} is outside the allowed range.")

    return errors

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=[KAFKA_SERVER],
    group_id="atmosync-consumer-group",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda data: json.loads(data.decode("utf-8"))
)

print("AtmoSync Kafka Consumer Started")
print("Waiting for sensor messages...\n")

try:
    for message in consumer:
        sensor_data = message.value

        errors = validate_sensor_reading(sensor_data)

        if errors:
            print("Invalid sensor reading:")
            for error in errors:
                print("-", error)
        else:
            print("Received valid sensor reading:")
            print(json.dumps(sensor_data, indent=4))

        print("-" * 50)

except KeyboardInterrupt:
    print("\nKafka Consumer Stopped.")

finally:
    consumer.close()