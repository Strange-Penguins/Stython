from discord.ext import commands


class Tutorial(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tutorial(self, ctx):
        await ctx.send("Not implemented")


def setup(client):
    client.add_cog(Tutorial(client))
