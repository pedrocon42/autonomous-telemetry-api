# Autonomous Navigation Telemetry + Anomaly API

## Overview
This project is a REST API built with Flask that simulates telemetry from an autonomous navigation system and detects anomalous sensor readings in real time.

## Motivation
This project connects to my research in resilient autonomous navigation and cyber-physical security. Autonomous systems rely on continuous streams of sensor data such as IMU, GPS, and communication signals. This API demonstrates how backend systems can monitor and analyze that data.

## Features
- Receive telemetry data via POST requests
- Detect anomalies in IMU readings
- Store and retrieve telemetry logs
- Simulate sensor input with a Python script

## Endpoints

### GET /
Check API status

### POST /telemetry
Send telemetry data

### GET /logs
View stored telemetry

## How to Run

```bash
python app.py