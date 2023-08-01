import os
import shutil
import logging
from functools import wraps
from contextlib import contextmanager

def get_main_folder():
    return os.listdir()

def detect_new(base):
    current = get_main_folder()
    return [x for x in current if x not in base]

def output_set(path="output", verbose=False):
    def output_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            main_folder = get_main_folder()
            func(*args, **kwargs)
            for new in detect_new(main_folder):
                if verbose:
                    print(f"Downloaded {new}")
                shutil.move(new,f"{path}/{new}")
        return wrapper
    return output_decorator

@contextmanager
def outputfolder(path):
    main_folder = get_main_folder()
    if not os.path.exists(path):
        os.makedirs(path)
    logging.debug(f"Outputfolder set output to {path}")
    yield
    for new in detect_new(main_folder):
        shutil.move(new,f"{path}/{new}")
        logging.debug(f"Outputfolder moved {new} to {path}")

def url_parser(url):
    args = url.split("?")[1]
    out = {}
    for x in args.split('&'):
        (k,v) = x.split('=')
        out[k] = v
    return out


def video_url(_id):
    return f"https://www.youtube.com/watch?v={_id}"

def playlist_url(_id):
    return f"https://www.youtube.com/playlist?list={_id}"

