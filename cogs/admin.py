import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def startworld(self, ctx, world_id: int):
        self.client.db.create_world(world_id)
        await ctx.send(f"Created new World {world_id}")

    # TODO: Get Informations of a world

    @startworld.error
    async def startworld_error(self, ctx, error):
        error = getattr(error, 'orginal', error)

        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("Missing required Argument World (int)!")


def setup(client):
    client.add_cog(Admin(client))
