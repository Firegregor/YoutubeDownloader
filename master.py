from src import download_list, url_parser

print("Test1")
links = ["https://www.youtube.com/watch?v=q98AwQwYcms",
"https://www.youtube.com/watch?v=KoX4dY78Xt0"]

playlist = "https://www.youtube.com/playlist?list=PLsTV1v4UDgA5QeltJZFJS0GgFz4cyHV1t"

universeIo = "https://www.youtube.com/watch?v=VQKNys4Jk2U&list=PLaiPn4ewcbkFEqIvjfW7VZD34XMaqytsP&index=12"

test_music = "https://www.youtube.com/playlist?list=PLddFZKqjWPorJDIDJHJbE35ljXKUMwwdD"
out = url_parser(test_music)
#print(out)
#for link in links:
#    download(link)
download_list(universeIo, "output/UniverseIo")
