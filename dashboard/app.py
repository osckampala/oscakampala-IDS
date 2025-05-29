from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

LOG_FILE = 'logs/alerts.log'

def read_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, 'r') as f:
        return f.readlines()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def logs():
    return jsonify(read_logs())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
