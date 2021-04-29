from keep_alive import keep_alive
import discord
import os
from replit import db
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix="D$", case_insensitive=True)

client = discord.Client()

sus_words = []

starter_encouragements = []

if "responding" not in db.keys():
    db["responding"] = True


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.startswith('D$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))

    if message.author == client.user:
        return

        msg = message.content

    if msg.startswith("D$hello"):
        await message.channel.send(
            'Hiya there! I am DogeBot™, An automated Python based program designed to send users to "Horny Jail"! Thank you for adding me to your server! I hope I can enjoy my stay, and remember, dont get Bonked!'
        )

    if msg.startswith("D$bonk"):
        await message.channel.send(file=discord.File('DogeBot.jpg'))

        if any(word in msg for word in sus_words):
            await message.channel.send(file=discord.File('DogeBot.jpg'))

    if msg.startswith("D$responding"):
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")


keep_alive()
client.run(os.getenv("TOKEN"))
