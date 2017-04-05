import json
import os

dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{dir}/settings.json") as data_file:
    settings = json.load(data_file)

clientID = settings["clientID"]
token = settings["token"]
ownerID = settings["ownerID"]
prefixes = settings["prefix"]

dev_id = 150750980097441792
permissionsURL = "2146958463" # https://finitereality.github.io/permissions/
OAuth2 = "https://discordapp.com/oauth2/authorize?permissions={}&scope=bot&client_id={}".format(permissionsURL, clientID)
URL = OAuth2

GitHubUser = "OrangutanGaming"
GitHubRepo = "OG_Bot.py"
GitHub = "https://github.com/{}/{}".format(GitHubUser, GitHubRepo)

Patreon = "https://www.patreon.com/OrangutanGaming"

bots_discord_pw_key = settings["bots_discord_pw"]
discord_pw = bots_discord_pw_key