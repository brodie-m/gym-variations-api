from flask import Flask
from flask_cors import CORS
bench_1rm = 85
squat_1rm = 180
diddy_1rm = 220
ohp_1rm = 85

def create_app():
    app = Flask(__name__)
    CORS(app)
    from .views import main
    app.register_blueprint(main)
    return app