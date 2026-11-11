import json
import random
from datetime import datetime, timezone


def generate_sensor_reading():
    reading = {
        "container_id": "CONTAINER-001",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature_c": round(random.uniform(2.0, 10.0), 2),
        "humidity_percent": round(random.uniform(50.0, 90.0), 2),
        "vibration_level": round(random.uniform(0.1, 5.0), 2)
    }

    return reading


if __name__ == "__main__":
    sensor_data = generate_sensor_reading()
    print(json.dumps(sensor_data, indent=4))