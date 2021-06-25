from requests import get
import requests
from json import loads
def get_map(a, p):
    b = get(f'https://osu.ppy.sh/api/get_beatmaps?k={p}&s={a}')
    c = loads(b.text)
    return print(c[0]['title'])


def download_bg(a, c):
    response = requests.get(f"https://assets.ppy.sh/beatmaps/{a}/covers/cover.jpg")
    file = open(f"{c}\cover.jpg", "wb")
    file.write(response.content)
    file.close()