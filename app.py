from flask import Flask, request, send_file
from convert import convert_image
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Image Converter API is running"

@app.route("/convert", methods=["POST"])
def convert():
    file = request.files["file"]
    format = request.form["format"]
    scale = int(request.form.get("scale", 100))
    quality = int(request.form.get("quality", 90))

    input_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(input_path)

    output_path = convert_image(input_path, format, scale, quality)
    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run()