from flask import Flask
from WaterTracker.config import SECRET_KEY
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('WaterTracker.config')
app.secret_key = SECRET_KEY
CORS(app) # CORSを有効化

import WaterTracker.app