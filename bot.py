import os
import discord
from dotenv import load_dotenv
import asyncio

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents, application_id='1230611368999260232')


@bot.event
async def on_ready():
    print("Online")


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message[0] == '.':
        return
    if message.author == bot.user:
        return
    await message.channel.send("ma ciaone")


async def load():  # cairca le cogs quando parte il bot
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')


async def main():
    await load()
    await bot.start(TOKEN)


asyncio.run(main())

bot.run(TOKEN)
