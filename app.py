from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

telemetry_log = []

def detect_anomaly(new_reading):
    """
    Lightweight multi-sensor anomaly detection.
    Checks:
    1. IMU spike compared to recent history
    2. Speed spike compared to recent history
    3. Weak signal strength
    4. High packet loss
    """
    reasons = []

    # Rule-based checks
    if new_reading["signal_strength"] < 50:
        reasons.append("low signal strength")

    if new_reading["packet_loss"] > 3:
        reasons.append("high packet loss")

    # Need some history before comparing trends
    if len(telemetry_log) >= 5:
        recent_imu = [entry["imu"] for entry in telemetry_log[-10:]]
        recent_speed = [entry["speed"] for entry in telemetry_log[-10:]]

        imu_mean = np.mean(recent_imu)
        imu_std = np.std(recent_imu)

        speed_mean = np.mean(recent_speed)
        speed_std = np.std(recent_speed)

        if imu_std > 0 and abs(new_reading["imu"] - imu_mean) > 2 * imu_std:
            reasons.append("imu spike detected")

        if speed_std > 0 and abs(new_reading["speed"] - speed_mean) > 2 * speed_std:
            reasons.append("speed spike detected")

    if reasons:
        return "anomaly", reasons

    return "normal", ["all sensors within expected range"]

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "Autonomous Navigation Telemetry + Anomaly API",
        "status": "running"
    })

@app.route("/telemetry", methods=["POST"])
def telemetry():
    data = request.get_json()

    required_fields = [
        "imu",
        "gps_lat",
        "gps_lon",
        "speed",
        "signal_strength",
        "heading",
        "altitude",
        "packet_loss"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    status, reasons = detect_anomaly(data)

    record = {
        "imu": data["imu"],
        "gps_lat": data["gps_lat"],
        "gps_lon": data["gps_lon"],
        "speed": data["speed"],
        "signal_strength": data["signal_strength"],
        "heading": data["heading"],
        "altitude": data["altitude"],
        "packet_loss": data["packet_loss"],
        "status": status,
        "reasons": reasons
    }

    telemetry_log.append(record)

    return jsonify({
        "message": "Telemetry received",
        "status": status,
        "reasons": reasons,
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