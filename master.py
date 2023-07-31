from src import YoutubeDownloader
import logging

logging.basicConfig(level=logging.DEBUG)

links = [ "https://www.youtube.com/watch?v=434tljD-5C8&t=48s",
    "https://www.youtube.com/watch?v=q98AwQwYcms",
    "https://www.youtube.com/watch?v=KoX4dY78Xt0",
    "https://www.youtube.com/playlist?list=PLsTV1v4UDgA5QeltJZFJS0GgFz4cyHV1t",
    "https://www.youtube.com/watch?v=VQKNys4Jk2U&list=PLaiPn4ewcbkFEqIvjfW7VZD34XMaqytsP&index=12",
    "https://www.youtube.com/playlist?list=PLddFZKqjWPorJDIDJHJbE35ljXKUMwwdD",
    "https://www.youtube.com/watch?v=Gs1VDYnS-Ac&t=3019s",
    "https://www.youtube.com/watch?v=Q4I_Ft-VLAg&t=2s"
        ]

you = YoutubeDownloader()
you.add_multiple_links(*links)
you.print_objects()
you.download_from_link(links[0])
