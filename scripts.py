import sys
import os
from PIL import Image


def jpeg_to_png(jpg_file_path, png_file_path):
    if jpg_file_path.endswith(".jpg") or jpg_file_path.endswith(".jpeg"):
        jpg_image = Image.open(jpg_file_path)
        _png_path = png_file_path if png_file_path.endswith(".png") else \
            os.path.splitext(png_file_path)[0] + ".png"
        jpg_image.save(_png_path)
    else:
        raise Exception("Invalid JPG file path")


# Check if an argument was passed
if len(sys.argv) > 1:
    # Get the argument value
    path = sys.argv[1]
    jpg_files = [file for file in os.listdir(path) if file.endswith(".jpg") or file.endswith(".jpeg")]
    if len(jpg_files) == 0:
        print("No JPG files found in the specified directory.")
        sys.exit(0)
    for file in jpg_files:
        abs_path = os.path.join(path, file)
        png_path = os.path.splitext(abs_path)[0] + ".png"
        print(f"Converted {file} to {png_path}")
        jpeg_to_png(abs_path, png_path)
else:
    print("No argument passed.")

input("Press Enter to exit...")
