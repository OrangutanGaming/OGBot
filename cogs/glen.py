from imgurpython import ImgurClient
import BotIDs
import re

album = "http://imgur.com/a/5oSFy"
albumID = re.findall(r"imgur.com/a/(\w+)", album)[0]

client = ImgurClient(BotIDs.imgur_clientID, BotIDs.imgur_Secret)

albumObj = client.get_album(albumID)
albumPics = client.get_album_images(albumID)

quotes = {}

for pic in albumPics:
    quotes[pic.description] = pic.link