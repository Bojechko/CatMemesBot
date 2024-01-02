import requests


def get_meme():
    r = requests.get("https://9gag.com/")

    print(r.text)
