import os
import customclient
from discord.ext import commands
from discord import Intents


def get_prefix(client, message):
    return "py!"


client = customclient.CustomClient(command_prefix=get_prefix, intents=Intents.all(), case_insensitive=True)


@client.command()
async def ping(ctx):
    """Zeigt den aktuellen Ping"""
    await ctx.send( f'Pong!')


# Load Modules
@client.command()
@commands.is_owner()
async def shutdown(ctx, reason="erwarteter Shutdown"):
    """Fährt den Bot herunter. Danach muss man ihn auf dem Server in der Console neustarten lol."""
    await ctx.send("Bot wird heruntergefahren...")
    client.reason = reason
    await client.close()


client.run(os.environ.get("DISCORD_TOKEN"))
