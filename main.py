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

bot.owner_id = 836449409226637313

sus_words = []

starter_encouragements = []

if "responding" not in db.keys():
    db["responding"] = True


@bot.command()
async def hello(ctx):
    await ctx.send(
        'Hiya there! I am DogeBot™, An automated Python based program designed to send users to "Horny Jail"! Thank you for adding me to your server! I hope I can enjoy my stay, and remember, dont get Bonked!'
    )


@bot.command()
async def bonk(ctx):
    await ctx.send(file=discord.File('DogeBot.jpg'))


keep_alive()
bot.run(os.getenv("TOKEN"))
