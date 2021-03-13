from discord.ext import commands


class Game(commands.Cog):

    def __init__(self, client):
        self.client = client
        # A map structure that has the current available windows
        # message id -> playerid -> window
        self.open_windows = {}

    # Switch the World the player is currently playing on
    @commands.command()
    async def switchworld(self, ctx):
        await ctx.send("Not implemented")

    @commands.command()
    async def attack(self, ctx):
        await ctx.send("Not implemented")

    @commands.command()
    async def overview(self, ctx):
        await ctx.send("Not implemented")


def setup(client):
    client.add_cog(Game(client))
