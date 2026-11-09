# AtmoSync - Micro-Climate Arbitrage Analytics

from datetime import datetime

def generate_sample_data():
    readings = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature_c": 8.5,
        "humidity_percent": 72,
        "vibration_level": 2.1
    }
    return readings


def analyze_conditions(data):
    print("\n--- AtmoSync Environmental Report ---")
    print("Timestamp:", data["timestamp"])
    print("Temperature:", data["temperature_c"], "°C")
    print("Humidity:", data["humidity_percent"], "%")
    print("Vibration:", data["vibration_level"])

    if data["temperature_c"] > 8:
        print("Alert: Temperature is above the sample threshold.")
    else:
        print("Temperature is within the sample threshold.")


if __name__ == "__main__":
    sample_data = generate_sample_data()
    analyze_conditions(sample_data)