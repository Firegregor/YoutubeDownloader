import os
import shutil
import logging
from pytube import YouTube, Playlist
from src import get_main_folder, detect_new, url_parser, outputfolder, video_url, playlist_url

def download_from_link(link, output=None):
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

def download_playlist(play, data):
    if data['name'] is None:
        data['name'] = play.title
    output_path = os.path.join("output", data['name'])
    logging.info(f"Download playlist {play.title} to {output_path}")
    logging.info(f"Downloaded {data['index']} / {len(play.videos)}")
    for video in play.videos[data['index']:len(play.videos)]:
        download_video(video, output_path)
        data['index'] += 1
        logging.info(f"Downloaded {data['index']} / {len(play.videos)}")
    return data

def download_video(youtube_obiect, output):
    logging.info(f"Download video {youtube_obiect.title} to {output}")
    with outputfolder(output):
        tmp = youtube_obiect.streams.get_highest_resolution()
        tmp.download()
