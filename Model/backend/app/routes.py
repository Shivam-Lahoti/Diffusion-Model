from flask import Blueprint, request, jsonify, send_file
from .utils import generate_image

main = Blueprint("main", __name__)

@main.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")
    filename = data.get("filename", "generated_image.png")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        # Generate the image
        image_path = generate_image(prompt, filename)
        return jsonify({"imagePath": f"generated_images/{filename}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
