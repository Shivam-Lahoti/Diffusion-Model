from flask import Blueprint, request, jsonify, send_file
from .utils import generate_image

main = Blueprint("main",__name__)

@main.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()  
    prompt = data.get("prompt")  
    filename= data.get("filename","generated_image.png")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        # Generate and retrieve the image path
        image_path = generate_image(prompt,filename)
        return send_file(image_path, mimetype="image/png")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

