import discord
from discord.ext import commands
import os
import json
import asyncio
import random
from config import token, PREFIX, acces




client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="h!help", url="https://www.twitch.tv/user4313"))

@client.command()
async def load(ctx, extension):
    user = ctx.author.id
    if user in acces:
        client.load_extension(f'cogs.{extension}') #loads the extension in the "cogs" folder
        await ctx.send(f'Loaded "{extension}"')
        return
    else:
        return

    


@client.command()
async def unload(ctx, extension):
    user = ctx.author.id
    if user in acces:
        client.unload_extension(f'cogs.{extension}') #unloads the extension in the "cogs" folder
        await ctx.send(f'Unloaded "{extension}"')
        return
    else:
        return


for filename in os.listdir('./cogs'): #loads all files (*.py)
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') #loads the file without ".py" for example: cogs.ping





client.run(token)
