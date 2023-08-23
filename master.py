from src import YoutubeDownloader, JsonLogger
import logging

logging.basicConfig(level=logging.INFO)

links = [ "https://www.youtube.com/watch?v=434tljD-5C8&t=48s",
    "https://www.youtube.com/watch?v=q98AwQwYcms",
    "https://www.youtube.com/watch?v=KoX4dY78Xt0",
    "https://www.youtube.com/playlist?list=PLsTV1v4UDgA5QeltJZFJS0GgFz4cyHV1t",
    "https://www.youtube.com/watch?v=VQKNys4Jk2U&list=PLaiPn4ewcbkFEqIvjfW7VZD34XMaqytsP&index=12",
    "https://www.youtube.com/playlist?list=PLddFZKqjWPorJDIDJHJbE35ljXKUMwwdD",
    "https://www.youtube.com/watch?v=Gs1VDYnS-Ac&t=3019s",
    "https://www.youtube.com/playlist?list=PL_y_nXztWbM2SSuLENZeaw6aUX2WDYfh-",
    "https://www.youtube.com/watch?v=diMw493NnkU&list=PLaiPn4ewcbkHu0r8zHJbXSf5_OvHL45Bq",
    "https://www.youtube.com/watch?v=OwYGxq2NTMQ&t=2199s",
    "https://www.youtube.com/watch?v=Q4I_Ft-VLAg&t=2s"
        ]

data = JsonLogger(json_path=r"D:\tmp\output\incremental.json")
you = YoutubeDownloader(data = data)
#you.add_multiple_links(*data['links'])
you.download_playlist()
#you.download_all_videos("output/Nieperfekcyjni")
#you.download_from_link("https://www.youtube.com/watch?v=Ufu7Xm6KBM4","./output/Nieperfekcyjni")

