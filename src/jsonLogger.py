from contextlib import contextmanager
from functools import wraps
import json
import logging


class JsonLogger(dict):

    def __init__(self, *args,json_path=None, **kw):
        super(JsonLogger,self).__init__(*args, **kw)
        self.__path = json_path
        self.__save_on_write = 1
        self['v'] = []
        self['list'] = []
        if json_path is not None:
            self.__load_from_file()
            self.__save_on_write = 0

    def __setitem__(self, key, value):
        super(JsonLogger,self).__setitem__(key, value)
        self.__save_to_file()

    def __iter__(self):
        return iter(self.itemlist)

    @property
    def item_list(self):
        return super(JsonLogger,self).keys()

    def values(self):
        return [self[key] for key in self]  

    def itervalues(self):
        return (self[key] for key in self)

    def __load_from_file(self):
        with open(self.__path) as log:
            tmp = json.loads(log.read())
        for key,val in tmp.items():
            self[key] = val

    def __save_to_file(self):
        if 0 == self.__save_on_write:
           logging.debug(f"{type(self)} save json")
           with open(self.__path, 'w') as log:
               log.write(json.dumps(self, indent=2))

    @contextmanager
    def suspend_writing(self):
        self.__save_on_write += 1
        logging.debug(f"{type(self)} suspend writing level {self.__save_on_write}")
        yield
        self.__save_on_write -= 1
        logging.debug(f"{type(self)} suspend writing level {self.__save_on_write}")
        self.__save_to_file()

    def bulk_update(self, func):
        @wraps
        def wrapper(*args, **kwargs):
            with self.suspend_writing():
                func(*args,**kwargs)
        return wrapper
