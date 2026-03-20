import requests
import random
import time

API_URL = "http://127.0.0.1:5000/telemetry"

for i in range(10):
    reading = {
        "imu": round(random.uniform(0.95, 1.05), 3),
        "gps_lat": 39.344,
        "gps_lon": -76.617,
        "speed": round(random.uniform(18, 24), 2),
        "signal_strength": round(random.uniform(70, 95), 2),
        "heading": round(random.uniform(0, 360), 2),
        "altitude": round(random.uniform(10, 30), 2),
        "packet_loss": round(random.uniform(0, 1), 2)
    }

    # Inject a more obvious anomaly near the end
    if i == 8:
        reading["imu"] = 1.60
        reading["speed"] = 40.0
        reading["signal_strength"] = 35.0
        reading["packet_loss"] = 4.5

    try:
        response = requests.post(API_URL, json=reading)
        print("Sent:", reading)
        print("Response:", response.status_code, response.text)
    except Exception as e:
        print("Error:", e)

    time.sleep(1)