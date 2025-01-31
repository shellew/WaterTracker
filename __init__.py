from flask import Flask
from WaterTracker.config import SECRET_KEY

app = Flask(__name__)
app.config.from_object('WaterTracker.config')
app.secret_key = SECRET_KEY

import WaterTracker.app