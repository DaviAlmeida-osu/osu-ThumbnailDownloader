import os
from PIL import Image
from lib import get_map, download_bg
c = os.getcwd()
try:
    beatmapid = input('Insert the beatmap id of the bg you want to download: ')
    apikey = open(f"{c}\keyapi.txt", 'r')
    get_map(int(beatmapid), apikey.read())
    download_bg(int(beatmapid), c)
    img = Image.open(f'{c}\cover.jpg')
    img.show()
except:
    print('Please copy your osu api key to the keyapi.txt file')
