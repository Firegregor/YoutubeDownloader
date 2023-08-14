from src import *
from pytube import Playlist, YouTube
import logging

class YoutubeDownloader:

    def __init__(self, data=None, incremental="output/incremental.json"):
        logging.debug("YoutubeDownloader Initialized")
        if data is None:
            self.data = JsonLogger(json_path=incremental)
        else:
            self.data = data
        self.ids = {'v':self.data['v'], 'list':self.data['list']}
        self.videos = set()

    def process_link(self, link):
        logging.debug(f"{type(self)} Process link - {link}")
        ids = {'v':[], 'list':[]}
        for k,v in url_parser(link).items():
            if k in self.ids:
                ids[k].append(v)
        return ids

    def process_multiple_links(self,*args):
        with self.data.suspend_writing():
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

    def download_all_videos(self, output=None):
        if output is None:
            output = './output'
        logging.debug(f'Downloading all videos to {output}')
        logging.debug(f'videos: {self.ids}')
        with self.data.suspend_writing():
            for _id in self.ids['v']:
                logging.debug(f"<download_all_videos> Downloading {_id}")
                play = YouTube(video_url(_id))
                download_video(play, output)

    def download_from_link(self, link, output="./output"):
        logging.debug(f"{type(self)} Download link - {link}")
        self.process_link(link)
        play = YouTube(link)
        download_video(play, output)

    def download_playlist(self, playlist=None):
        if playlist is None:
            download_list = self.ids['list']
        else:
            download_list = [playlist]
        with self.data.suspend_writing():
            for _id in download_list:
                if _id not in self.data["downloaded"]["playlist"]:
                    data = {
                            "name": None,
                            "index":0,
                            "ids":[]
                            }
                else:
                    data = self.data["downloaded"]["playlist"][_id]
                play = Playlist(playlist_url(_id))
                self.data["downloaded"]["playlist"][_id] = download_playlist(play,data)
