import discord
from discord.ext import commands


class Tutorial(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tutorial(self, ctx):
        await ctx.send(embed=discord.Embed(
            title="Short tutorial",
            description="You can start a new game using py!join <world>"))

        await ctx.send("Not implemented")


def setup(client):
    client.add_cog(Tutorial(client))
