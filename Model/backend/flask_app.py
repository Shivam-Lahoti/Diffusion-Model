from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from Model.backend.app import create_app

app = create_app()
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")  # Initialize SocketIO

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000)  # Run the app with SocketIO
