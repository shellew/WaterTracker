from flask import Flask, request, redirect, jsonify, render_template, send_file
from datetime import datetime
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


user_data = {
    "daily_goal": 2000,
    "total_intake": 0
}

@app.route('/set_goal', methods=['POST'])
def set_goal():
    data = request.get_json()
    user_data["daily_goal"] = int(data["daily_goal"])
    return jsonify({"message": f"目標水分量 {user_data['daily_goal']} ml に設定しました"})

@app.route('/record_intake', methods=['POST'])
def record_intake():
    data = request.get_json()
    user_data["total_intake"] += int(data["intake_amount"])
    return jsonify({"message": f"{data['intake_amount']} ml を記録しました"})

@app.route('/reset_intake', methods=['POST'])
def reset_intake():
    user_data["total_intake"] = 0
    return jsonify({"message": "摂取記録をリセットしました"})

@app.route('/get_status', methods=['GET'])
def get_status():
    return jsonify(user_data)

@app.route('/')
def index():
    return render_template("/WaterTracker/index.html")

@app.route('/manifest.json')
def serve_manifest():
    return send_file('static/manifest.json', mimetype='application/manifest+json')

@app.route('/service-worker.js')
def serve_sw():
    return send_file('static/service-worker.js', mimetype='application/javascript')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)