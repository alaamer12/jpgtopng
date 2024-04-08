from PIL import Image
import winreg
import sys
import threading
import tqdm
import os


SUB_KEY = "Software\\Classes\\.jpg"
class JPGTOPNG:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance
    def __init__(self, jpg_file_path: str, png_file_path):
        self.jpg_file_path = jpg_file_path
        self.png_file_path = jpg_file_path if png_file_path is None else png_file_path
        # Register the file type on instance creation
        self.register()

    def jpeg_to_png(self):
        if self.jpg_file_path.endswith(".jpg") or self.jpg_file_path.endswith(".jpeg"):
            # Open the JPG image
            jpg_image = Image.open(self.jpg_file_path)
            # Convert the JPG image to PNG
            png_path = self.png_file_path if self.png_file_path.endswith(".png") else os.path.splitext(self.png_file_path)[0] + ".png"
            jpg_image.save(png_path)
        else:
            raise Exception("Invalid JPG file path")

    def register(self):
        try:
            key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, ".jpg")
            winreg.SetValue(key, None, winreg.REG_SZ, "JPEG Image")
            winreg.SetValue(key, "Content Type", winreg.REG_SZ, "image/jpeg")
        except:
            pass

    def create_progress_bar(self):
        pass

    def get_file_sizes(self):
        pass



    def get_args(self):
        pass