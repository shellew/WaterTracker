from flask import Flask

app = Flask(__name__)
app.config.from_object('WaterTracker.config')

import WaterTracker.app