import json
import random
import time
from datetime import datetime, timezone


def generate_sensor_reading(container_id):
    reading = {
        "container_id": container_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature_c": round(random.uniform(2.0, 10.0), 2),
        "humidity_percent": round(random.uniform(50.0, 90.0), 2),
        "vibration_level": round(random.uniform(0.1, 5.0), 2)
    }

    return reading


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
                print(json.dumps(sensor_data, indent=4))

            print("-" * 50)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nAtmoSync IoT Simulator Stopped.")