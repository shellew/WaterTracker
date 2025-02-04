from flask import Flask, request, redirect, jsonify
from WaterTracker import app
from datetime import datetime


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