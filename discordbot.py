#before running this bot you need to install discord.py and latest python first
import discord
from discord.ext import commands
from discord import Game
from discord.ext.commands import Bot
import time
import random
from discord.utils import get

print("Welcome to this Discord Bot! Made by mal#1337")
x = input("Your Password: ")
if x == "testbot123": #set any password
    pass
else:
    print("Wrong password!")
    exit()
    
TOKEN = '#your discord bot token' #0
client = commands.Bot(command_prefix='?') #you can set any prefix you want

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Discord Bot", url="https://twitch.tv/ninja", type=1))
    print(f'\nLogged in as {client.user.name}#{client.user.discriminator}, User ID: {client.user.id}, Discord version: {discord.__version__}\n')
    
#good luck on your discord bot project, this is for running discord bot only.

client.run(TOKEN)