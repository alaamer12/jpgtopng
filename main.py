from PIL import Image
import winreg
import os
from functools import wraps
import threading
import contextlib



class JPGTOPNG:
    __instance = None
    __lock = threading.Lock()
    SUB_KEY = r"directory\background\shell\JPG to PNG"


    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, jpg_file_path: str, png_file_path=None):
        self.jpg_file_path = jpg_file_path
        self.png_file_path = jpg_file_path if png_file_path is None else png_file_path
        self.cwd = os.getcwd()
        self.script_path = os.path.join(self.cwd, "scripts.py")
        self.PYTHONPATH = os.environ.get("PYTHONPATH").split(";")[1]

    @staticmethod
    def _run_once(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not wrapper.has_run:
                wrapper.has_run = True
                return func(*args, **kwargs)
        wrapper.has_run = False
        return wrapper

    def jpeg_to_png(self):
        if self.jpg_file_path.endswith(".jpg") or self.jpg_file_path.endswith(".jpeg"):
            with contextlib.suppress(Exception):
                jpg_image = Image.open(self.jpg_file_path)
                png_path = self.png_file_path if self.png_file_path.endswith(".png") else os.path.splitext(self.png_file_path)[0] + ".png"
                jpg_image.save(png_path)
        raise Exception("Invalid JPG file path")

    @_run_once
    def register(self):
        try:
            key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, self.SUB_KEY)
            winreg.SetValue(key, "command", winreg.REG_SZ, f"{self.PYTHONPATH} \"{self.script_path}\" \"%V\"")

        except Exception as e:
            print(f"Failed to register: {e}")

if __name__ == "__main__":
    j = JPGTOPNG("","")
    j.register()