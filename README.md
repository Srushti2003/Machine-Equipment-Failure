# 🔧 Equipment Failure Prediction and Power BI Dashboard

This is a **Data Analytics and Machine Learning project** that predicts equipment failure based on environmental and sensor data. It includes a **machine learning backend in Python**, a **frontend built with HTML/CSS/JavaScript**, and a **Power BI dashboard** for visual analytics.

---

## 🚀 Project Overview

In industrial environments, equipment failures can lead to high costs and downtime. This project uses **sensor data** (temperature, pressure, vibration, humidity, etc.) and metadata (equipment type and location) to:

- Predict if a piece of equipment is likely to fail (ML classification)
- Provide a user-friendly web interface for data input and prediction
- Visualize failure trends and equipment behavior using Power BI

---

## 🎯 Features

✅ **Machine Learning Model**
- Built using Random Forest Classifier in Python  
- Trained on labeled sensor and metadata  
- Encodes categorical values using `LabelEncoder`  
- Predicts binary output: **Faulty (1)** or **Healthy (0)**

✅ **Web Frontend (HTML + CSS + JS)**
- Input form to submit temperature, pressure, etc.
- Equipment and location dropdowns populated dynamically
- Prediction result displayed instantly via AJAX

✅ **Flask Backend (Python)**
- Serves HTML templates and static files
- Exposes `/predict` API for ML inference
- Handles label encoding and model input preprocessing

✅ **Power BI Dashboard**
- Interactive visual analytics dashboard
- Includes slicers, charts, and KPIs for:
  - Equipment failure trends
  - Correlation analysis (vibration vs temperature)
  - Faulty vs healthy equipment summary
  - Location-wise failure distributions

---

## 📸 Screenshots

### 🔍 Web Interface

![image](https://github.com/user-attachments/assets/00767e31-a103-4939-8a3d-f476fe79bac3)

![image](https://github.com/user-attachments/assets/8de3b680-354c-4e47-a2a6-632ad9623078)

### 📊 Power BI Dashboard

![Predictive Maintenance and Failure](https://github.com/user-attachments/assets/5a3e143f-057b-49e2-b1fd-c2e0aafd48c5)
