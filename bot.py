import os
import random
import discord
import requests

anime_base_url = os.environ['ANIME_BASE_URL']
anime_yuck_url = os.environ['ANIME_YUCK_URL']
token = os.environ['BOT_TOKEN']
cloudinary_base = os.environ["CLOUDINARY_BASE"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_help():
    m = "You have summoned the crap bot.\n\tcrap waifu: get waifu pics\n\tcrap doge help: get help with the crap doge commands"
    return m

def get_waifu():
    keywords = [
            'waifu',
            'waifu',
            'waifu',
            'waifu',
            'waifu',
            'waifu',
            'neko',
            'neko',
            'neko',
            'neko',
            'cuddle',
            'hug',
            'awoo',
            'kiss',
            'pat',
            'smug',
            'bonk',
            'blush',
            'smile',
            'wave',
            'handhold',
            'happy',
            'wink'
    ]
    keyword = keywords[random.randint(0, len(keywords))]
    url = os.path.join(anime_base_url, keyword)
    res = requests.get(url)
    return res.json()['url']

def get_waifu_nsfw():
    url = os.path.join(anime_yuck_url, "waifu")
    res = requests.get(url)
    return res.json()['url']

def get_doge(doge_type):
    assert doge_type in ['help', 'smirk', 'gun', 'sitting', 'quoge', 'wow', 'sad', 'swole', 'dancing', 'cry', 'sly', 'party', 'sleep']

    if doge_type == 'help':
        m = "Available doge commands:\n\tcrap doge sly\n\tcrap doge sitting\n\tcrap doge smirk\n\tcrap doge dancing\n\tcrap doge quoge\n\tcrap doge gun\n\tcrap doge wow\n\tcrap doge sad\n\tcrap doge swole\n\tcrap doge cry"
        return m
    
    if doge_type == 'smirk':
        url = os.path.join(cloudinary_base, "v1625167973/doge_smirk.png")
        return url

    if doge_type == 'gun':
        url = os.path.join(cloudinary_base, "v1625168273/doge_gun.png")
        return url

    if doge_type == 'sitting':
        url = os.path.join(cloudinary_base, "v1625168164/doge_sitting.png")
        return url

    if doge_type == 'quoge':
        url = os.path.join(cloudinary_base, "v1625168322/doge_quoge.png")
        return url

    if doge_type == 'wow':
        url = os.path.join(cloudinary_base, "v1625247089/doge_wow.jpg")
        return url

    if doge_type == 'sad':
        url = os.path.join(cloudinary_base, "v1625247015/doge_sad.png")
        return url

    if doge_type == 'swole':
        url = os.path.join(cloudinary_base, "v1625246942/doge_swole.jpg")
        return url

    if doge_type == 'dancing':
        url = os.path.join(cloudinary_base, "v1629090203/doge_dancing.gif")
        return url
    
    if doge_type == 'cry':
        url = os.path.join(cloudinary_base, "v1630430142/doge_cry.png")
        return url
    
    if doge_type == 'sly':
        url = os.path.join(cloudinary_base, "v1644738902/doge_sly.gif")
        return url
    
    if doge_type == 'party':
        url = os.path.join(cloudinary_base, "v1646316228/doge_party.gif")
        return url
    
    if doge_type == 'sleep':
        url = os.path.join(cloudinary_base, "v1651397436/doge_sleep.jpg")
        return url

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    msg = message.content.lower().replace(" ", "")

    if msg == "craphelp":
        response = get_help()
        await message.channel.send(response)

    if msg == "crapwaifu":
        response = get_waifu()
        await message.channel.send(response)
    
    if msg == "crapnsfw":
        response = get_waifu_nsfw()
        await message.channel.send(response)

    if msg == "crapquote":
        response = get_quote()
        await message.channel.send(response)
    
    if msg == "crapstare":
        response = os.path.join(cloudinary_base, "v1646315977/stare.png")
        await message.channel.send(response)

    if msg[0:8] == "crapdoge":
        doge_type = msg[8:]
        response = get_doge(doge_type)
        await message.channel.send(response)

client.run(token)
