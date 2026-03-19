from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

telemetry_log = []

def detect_anomaly(new_reading):
    """
    Very simple anomaly detector:
    checks whether imu differs too much from recent values.
    """
    if len(telemetry_log) < 5:
        return "normal"

    imu_values = [entry["imu"] for entry in telemetry_log[-10:]]
    mean_val = np.mean(imu_values)
    std_val = np.std(imu_values)

    if std_val == 0:
        return "normal"

    if abs(new_reading["imu"] - mean_val) > 2 * std_val:
        return "anomaly"

    return "normal"

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "Autonomous Navigation Telemetry + Anomaly API",
        "status": "running"
    })

@app.route("/telemetry", methods=["POST"])
def telemetry():
    data = request.get_json()

    required_fields = ["imu", "gps_lat", "gps_lon", "speed", "signal_strength"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    status = detect_anomaly(data)

    record = {
        "imu": data["imu"],
        "gps_lat": data["gps_lat"],
        "gps_lon": data["gps_lon"],
        "speed": data["speed"],
        "signal_strength": data["signal_strength"],
        "status": status
    }

    telemetry_log.append(record)

    return jsonify({
        "message": "Telemetry received",
        "status": status,
        "record": record
    }), 200

@app.route("/logs", methods=["GET"])
def logs():
    return jsonify({
        "count": len(telemetry_log),
        "data": telemetry_log
    })

if __name__ == "__main__":
    app.run(debug=True)