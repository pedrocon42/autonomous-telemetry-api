# Autonomous Navigation Telemetry + Anomaly API

## Overview
This project is a REST API built with Flask that simulates telemetry from an autonomous navigation system and detects anomalous sensor readings in real time.

## Motivation
This project connects to my research in resilient autonomous navigation and cyber-physical security. Autonomous systems rely on continuous streams of sensor data such as IMU, GPS, and communication signals. This API demonstrates how backend systems can monitor and analyze that data.

## Features
- Receive telemetry data via POST requests
- Detect anomalies across multiple sensors (IMU, speed, signal strength, packet loss)
- Store and retrieve telemetry logs
- Simulate realistic sensor input (GPS, IMU, altitude, heading, etc.)

## Endpoints

### GET /
Check API status

### POST /telemetry
Send telemetry data

Example JSON:
```json
{
  "imu": 1.02,
  "gps_lat": 39.344,
  "gps_lon": -76.617,
  "speed": 21.5,
  "signal_strength": 88.0
}
```

### GET /logs
View stored telemetry

## How to Run

### 1. Run the API
```bash
python app.py
```

### 2. Run the simulator (in a second terminal)
```bash
python sensor_sim.py
```

## Tech Stack
- Python
- Flask
- NumPy

## Future Improvements
- Add database storage
- Implement ML-based anomaly detection
- Build a dashboard UI

## Project Structure
```
autonomous-telemetry-api/
│
├── app.py
├── sensor_sim.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Author
Pedro Contreras