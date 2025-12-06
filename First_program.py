from flask import Flask, request, render_template, jsonify
import json
import datetime

app = Flask(__name__)

# Store alerts in memory (you can change to file or DB)
alerts = []


@app.route("/")
def home():
    return render_template("index.html", alerts=alerts)


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()

        alert_message = data.get("message", "No message provided")

        # Add timestamp
        alert_entry = {
            "message": alert_message,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Store alert
        alerts.append(alert_entry)

        print("Alert Received:", alert_entry)

        return jsonify({"status": "success", "received": alert_entry}), 200
#aaa
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)