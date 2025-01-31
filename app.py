from flask import Flask, request, redirect, jsonify
from WaterTracker import app
from WaterTracker.database import init_db, update_goal, get_goal, record_intake, get_today_intake, get_history, reset_intake
from datetime import datetime

init_db()

@app.route('/set_goal', methods=['POST'])
def set_goal():
    data = request.json
    daily_goal = data.get("daily_goal")
    
    if not isinstance(daily_goal, int) or daily_goal <= 0:
        return jsonify({"error": "Invalid goal value"}), 400

    update_goal(daily_goal)
    return jsonify({"message": "Daily goal updated", "daily_goal": daily_goal})

@app.route('/record_intake', methods=['POST'])
def record_intake_route():
    data = request.json
    intake_amount = data.get("intake_amount")

    if not isinstance(intake_amount, int) or intake_amount <= 0:
        return jsonify({"error": "Invalid intake amount"}), 400

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record_intake(intake_amount, timestamp)

    return jsonify({"message": f"Recorded {intake_amount} ml", "intake_amount": intake_amount})

@app.route('/get_today_intake', methods=['GET'])
def get_today_intake_route():
    today_date = datetime.now().strftime("%Y-%m-%d")
    total_intake = get_today_intake(today_date)
    daily_goal = get_goal()

    return jsonify({"total_intake": total_intake, "daily_goal": daily_goal})

@app.route('/get_history', methods=['GET'])
def get_history_route():
    history = get_history()
    return jsonify({"history": history})

@app.route('/reset_intake', methods=['POST'])
def reset_intake_route():
    reset_intake()
    return jsonify({"message": "Water intake data reset"})