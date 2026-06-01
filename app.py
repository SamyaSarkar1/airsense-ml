from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/forecast")
def forecast():
    return jsonify({
        "predictedAQI": 145
    })

if __name__ == "__main__":
    app.run()