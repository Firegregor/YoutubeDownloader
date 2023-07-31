import shutil
from pytube import YouTube, Playlist
from src import get_main_folder, detect_new, url_parser, outputfolder

def download(link, output=None):
    main_folder = get_main_folder()
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    for new in detect_new(main_folder):
        print(f"Downloaded {new}")
        if output is not None:
            shutil.move(new,f"{output}/{new}")

def download_list(link, name):
    params = url_parser(link)
    start=0
    try:
        start=int(params["index"])-1
    except NameError:
        pass
    playlistObject = Playlist(f"https://www.youtube.com/playlist?list={params['list']}")
    videos = playlistObject.video_urls
    nr_of_videos = len(videos)
    print(start)
    for i, yt in enumerate(videos[start:nr_of_videos]):
        with outputfolder(name):
            print(yt)
            download(yt, name)
        print(f"Downloaded {i+1}/{playlistObject.length-start-1}")

class Downloader:
    def __init__(self):
        self.ids = set()
        self.obiects = set()

    def add_videos(self, *args):
        new = set(args).difference_update(self.ids)
        new_videos = {Youtube(video_link(x)).streams.get_highest_resolution() for x in new}
        self.ids.update(new)
        self.obiects.update(new_videos)
