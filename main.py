import os
import customclient
from discord.ext import commands
from discord import Intents
import discord

prefix = os.environ.get("DISCORD_PREFIX")


# Returns a prefix. Warning: Two Arguments required
def get_prefix(client, message):
    return commands.when_mentioned_or(prefix)(client, message)


# A Function to load all Modules
def load_modules():
    for file in os.listdir('./cogs'):
        if file.endswith(".py"):
            client.load_extension(f'cogs.{file[:-3]}')
            print(f"Starting {file}")


# Creates a client
client = customclient.CustomClient(command_prefix=get_prefix, intents=Intents.all(), case_insensitive=True,
                                   status=discord.Status.dnd, activity=discord.Game("Die Stämme"))
load_modules()


# Shows Ping
@client.command()
async def ping(ctx):
    """Shows the actual Ping"""
    await ctx.send(f'🏓 Pong 🏓 (took: {round(client.latency * 1000, 1)} ms)')


# Load a module
@client.command()
@commands.is_owner()  # checks owner_ids too
async def load(ctx, extension):
    """Loads a module"""
    await ctx.send(f':green_circle: {extension} loaded!')


# unload a module
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    """Unloads a module"""
    await ctx.send(f':green_circle: {extension} unloaded!')


# Reload a module
@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    """Reloads a module"""
    await ctx.send(f':green_circle: {extension} reloaded!')


# Load Modules
@client.command()
@commands.is_owner()
@commands.is_owner()
async def shutdown(ctx, reason="regular shutdown"):
    """Shuts the bot down"""
    await ctx.send("Bot shuts down...")
    client.reason = reason
    await client.close()


client.run(os.environ.get("DISCORD_TOKEN"))
