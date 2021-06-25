import os
from PIL import Image
from lib import get_map, download_bg
c = os.getcwd()
beatmapid = input('Insert the beatmap id of the bg you want to download: ')
if os.stat(f"{c}\keyapi.txt").st_size == 0:
    ak = input('Insert your api key here, it will be saved on your machine for future uses: ')
    with open(f"{c}\keyapi.txt.", 'w') as a:
        a.write(ak)
apikey = open(f"{c}\keyapi.txt", 'r')
get_map(int(beatmapid), apikey.read())
download_bg(int(beatmapid), c)
img = Image.open(f'{c}\cover.jpg')
img.show()