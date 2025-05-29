from flask import Flask, render_template, request
import re

app = Flask(__name__)

LOG_FILE = "logs/alerts.log"

def parse_log():
    alerts = []
    severity_colors = {
        "CRITICAL": "red",
        "HIGH": "darkorange",
        "MEDIUM": "orange",
        "LOW": "yellowgreen",
        "INFO": "green"
    }
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
        for line in lines:
            # Example log line: 2025-05-29 12:00:00,000 | INFO | [ALERT 🚨] Rule ID: 1 | ...
            match = re.search(r"\|\s*(\w+)\s*\|\s*(.*)", line)
            if match:
                level = match.group(1)
                message = match.group(2).strip()
                alerts.append({
                    "level": level,
                    "message": message,
                    "color": severity_colors.get(level, "gray")
                })
    except FileNotFoundError:
        alerts = []
    return alerts

@app.route("/")
def index():
    alerts = parse_log()
    total = len(alerts)
    counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}
    for alert in alerts:
        lvl = alert["level"]
        if lvl in counts:
            counts[lvl] += 1
    return render_template("index.html", alerts=alerts, total=total, counts=counts)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
