from src import *
import logging

class YoutubeDownloader:

    def __init__(self, incremental="output/incremental.json"):
        logging.debug("YoutubeDownloader Initialized")
        self.ids = JsonLogger(json_path=incremental)
        self.videos = set()

    def process_link(self, link):
        logging.debug(f"{type(self)} Process link - {link}")
        ids = {'v':[], 'list':[]}
        for k,v in url_parser(link).items():
            if k in self.ids:
                ids[k].append(v)
        return ids

    def process_multiple_links(self,*args):
        tmp = [self.process_link(link) for link in args]
        logging.debug(f"{type(self)} Process multiple links - {tmp}")
        vid = [link['v'] for link in tmp]
        lis = [link['list'] for link in tmp]
        return {'v':vid, 'list':lis}

    def add_multiple_links(self,*args):
        logging.debug(f"{type(self)} Adding multiple links")
        new = self.process_multiple_links(*args)
        for key in new:
            tmp = set(self.ids[key])
            tmp.update(*new[key])
            self.ids[key] = list(tmp)

    def print_objects(self):
        logging.debug(f"{type(self)} Printing ovjects")
        for k,v in self.ids.items():
            print(k)
            print(v)

    def download_from_link(self, link):
        logging.debug(f"{type(self)} Download link - {link}")
        self.process_link(link)
        download(link, 'output')

