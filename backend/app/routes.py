from flask import Blueprint, request, jsonify, send_file
from .utils import generate_image

main = Blueprint("main",__name__)

@main.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt =  data.get("promot")
    if not prompt:
        return jsonify({"error":"No prompt given"}),400
    
    try:
        image_path= generate_image(prompt)
        return send_file(image_path, mimetype="image/png")
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
