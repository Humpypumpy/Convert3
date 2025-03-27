from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image
import os
from io import BytesIO

app = Flask(__name__)
CORS(app)  # This enables CORS for all domains and routes

@app.route('/')
def home():
    return "Backend is live!"

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    format = request.form.get('format', 'png').lower()
    scale = int(request.form.get('scale', 100))
    quality = int(request.form.get('quality', 90))

    img = Image.open(file.stream)

    # Resize
    width, height = img.size
    img = img.resize((int(width * scale / 100), int(height * scale / 100)))

    # Convert mode if needed
    if format in ['jpeg', 'jpg', 'webp', 'avif', 'tiff'] and img.mode != 'RGB':
        img = img.convert('RGB')

    # Save to BytesIO
    output = BytesIO()
    img.save(output, format=format.upper(), quality=quality)
    output.seek(0)

    return send_file(output, mimetype=f'image/{format}', as_attachment=True, download_name=f'converted.{format}')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
