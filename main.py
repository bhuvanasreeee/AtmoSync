import json
import random
import time
import math
from datetime import datetime, timezone


def generate_sensor_reading(container_id):
    """Generate one simulated sensor reading."""
    return {
        "container_id": container_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature_c": round(random.uniform(2.0, 10.0), 2),
        "humidity_percent": round(random.uniform(50.0, 90.0), 2),
        "vibration_level": round(random.uniform(0.1, 5.0), 2)
    }


def validate_sensor_reading(reading):
    """Check sensor data for missing or invalid values."""
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
            errors.append(f"{field} must be a finite number.")
        elif not minimum <= value <= maximum:
            errors.append(
                f"{field} is outside the simulator range ({minimum} to {maximum})."
            )

    return errors


if __name__ == "__main__":

    container_ids = [
        "CONTAINER-001",
        "CONTAINER-002",
        "CONTAINER-003"
    ]

    print("AtmoSync IoT Simulator Started")
    print("Generating continuous sensor readings...")
    print("Press CTRL+C to stop.\n")

    try:
        while True:
            for container_id in container_ids:

                sensor_data = generate_sensor_reading(container_id)

                errors = validate_sensor_reading(sensor_data)

                if errors:
                    print("Invalid sensor reading:")
                    for error in errors:
                        print("-", error)
                else:
                    print(json.dumps(sensor_data, indent=4))

            print("-" * 50)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nAtmoSync IoT Simulator Stopped.")