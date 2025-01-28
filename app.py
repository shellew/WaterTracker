from flask import Flask
from WaterTracker import app

@app.route('/')
def index():
    return "Hello, World!"
