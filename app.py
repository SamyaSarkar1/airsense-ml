from flask import Flask, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load AQI data
df = pd.read_csv("aqi_data.csv")

# Prepare training data
X = df[["hour"]]
y = df["aqi"]

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

@app.route("/")
def home():
    return jsonify({
        "message": "AirSense ML Service Running"
    })

@app.route("/forecast")
def forecast():
    # Predict next hour AQI
    next_hour = int(df["hour"].max()) + 1

    prediction = model.predict([[next_hour]])[0]

    return jsonify({
        "nextHour": next_hour,
        "predictedAQI": round(float(prediction), 2),
        "model": "Linear Regression"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)