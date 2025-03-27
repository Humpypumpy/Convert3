from PIL import Image
import os

def convert_image(input_path, output_format, scale=100, quality=90):
    with Image.open(input_path) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')

        if scale < 100:
            width, height = img.size
            img = img.resize((int(width * scale / 100), int(height * scale / 100)))

        output_path = f"{os.path.splitext(input_path)[0]}_converted.{output_format.lower()}"
        img.save(output_path, output_format.upper(), quality=quality)
        return output_path