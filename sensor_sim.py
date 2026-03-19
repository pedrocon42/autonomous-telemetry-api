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
        "signal_strength": round(random.uniform(70, 95), 2)
    }

    if i == 8:
        reading["imu"] = 1.60

    try:
        response = requests.post(API_URL, json=reading)
        print("Sent:", reading)
        print("Response:", response.status_code, response.text)
    except Exception as e:
        print("Error:", e)

    time.sleep(1)