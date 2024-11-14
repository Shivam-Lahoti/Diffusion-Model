from flask import Flask
from flask_cors import CORS
from Model.backend.app import create_app

app =create_app()
CORS(app)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000)

    


