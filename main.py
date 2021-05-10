from keep_alive import keep_alive
import discord
import os
import random
import logging
from discord.ext import commands

bot = commands.Bot(command_prefix="D$", case_insensitive=True)


def is_owner():
    async def predicate(ctx):
        return ctx.author.id == 597467552079282186

        return commands.check(predicate)


@bot.command()
@commands.is_owner()
async def secret(ctx):
    await ctx.send('Hello Maker!')


@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Nothing to see here friend.')


@bot.command()
async def hello(ctx):
    await ctx.send(
        'Hiya there! I am DogeBot™, An automated Python based program designed to send users to "Horny Jail"! Thank you for adding me to your server! I hope I can enjoy my stay, and remember, dont get Bonked!'
    )


@bot.command()
async def bonk(ctx):
    await ctx.send(file=discord.File('DogeBot.jpg'))


@bot.command()
async def member(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

keep_alive()
bot.run(os.getenv("TOKEN"))
