from flask import Flask
from .routes import main  # Import routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)  # Register blueprint
    return app
