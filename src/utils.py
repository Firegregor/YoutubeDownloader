import os
import shutil
from functools import wraps

def get_main_folder():
    return os.listdir()

def detect_new(base):
    current = get_main_folder()
    return [x for x in current if x not in base]

def output_set(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        main_folder = get_main_folder()
        func(*args, **kwargs)
        for new in detect_new(main_folder):
            shutil.move(new,f"output/{new}")
    return wrapper

