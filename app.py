from flask import Flask, render_template, request, flash, redirect, url_for, session
from WaterTracker import app

user_data = {
    "daily_goal": '',
    "total_intake": 0,
}

app.secret_key = 'water_reminder_app'

@app.route('/')
def index():
    return render_template('/WaterTracker/index.html', daily_goal=user_data["daily_goal"], total_intake=user_data["total_intake"])

@app.route('/set_goal', methods=['GET', 'POST'])
def set_goal():
    if request.method == 'POST':
        try:
            session.permanent = True 
            new_goal = int(request.form['daily_goal'])
            user_data["daily_goal"] = new_goal
            session["user_data"] = user_data["daily_goal"]
            flash(f"Daily goal set to {new_goal} ml", "success")
            return redirect(url_for('index'))
        except ValueError:
            flash("Please enter a valid number for the daily goal", "error")
    return render_template('/WaterTracker/set_goal.html', daily_goal=user_data["daily_goal"])

@app.route('/record_intake', methods=['GET', 'POST'])
def record_intake():
    if request.method == 'POST':
        try:
            intake = int(request.form['intake_amount'])
            user_data["total_intake"] += intake
            flash(f"Add {intake} ml to your total intake", "success")
            return redirect(url_for('index'))
        except ValueError:
            flash("Please enter a valid number for the intake amount", "error")
    return render_template('/WaterTracker/record_intake.html', total_intake=user_data["total_intake"])

@app.route('/reset_intake', methods=['POST'])
def reset_intake():
    user_data["total_intake"] = 0
    flash("Total intake has been reset.", "success")
    return redirect(url_for('index'))