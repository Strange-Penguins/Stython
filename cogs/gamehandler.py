import discord
from game import gamedata as gd
from discord.ext import commands


class GameHandler(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.game = gd.GameData()
        # A map structure that has the current available windows
        # self.points_mapping = json.load()

        # Playerid -> World -> Village
        self.playerviews = {}

    # Switch the World the player is currently playing on
    @commands.command()
    async def switchworld(self, ctx, world_id):
        """Switches the current active world of a player"""
        # Check if player plays on the world
        world = 0

        # Gets his first Village
        self.playerviews[ctx.author.id] = (world, )
        await ctx.send(f"Switched your current world to world {world}")

    @commands.command()
    async def switchvillage(self, ctx, village_id):
        world = self.playerviews[ctx.author.id][0]
        self.playerviews[ctx.author.id] = (world, village_id)
        await ctx.send(f"Switched your current world to world {village_id} on {world}")

    @commands.command()
    async def overview(self, ctx):
        """Shows an overview of your current village"""
        # TODO: Points calculation

        points = 260

        # TODO: Capacity calculation
        capacity = 1000
        farm_limit = 2000

        points_path = {10999: "https://cdn.discordapp.com/attachments/820622377208643586/820622658370142278/W6.png",
                       8999: "https://cdn.discordapp.com/attachments/820622377208643586/820622636794118164/W5.png",
                       2999: "https://cdn.discordapp.com/attachments/820622377208643586/820622582789308446/W4.png",
                       999: "https://cdn.discordapp.com/attachments/820622377208643586/820622556511469568/W3.png",
                       299: "https://cdn.discordapp.com/attachments/820622377208643586/820622462009475082/W2.png"}

        overview_embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at,
                                       title=f"Village of {ctx.author}"
                                       )

        for k, v in points_path.items():
            if points > k:
                overview_embed.set_thumbnail(url=v)
                break
        else:
            overview_embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/820622377208643586/820622462005149696/W1.png")
        overview_embed.add_field(name="Resources",
                                 value=f":wood: {0}/{capacity} :bricks: {0}/{capacity} :nut_and_bolt: {0}/{capacity} "
                                       f":bust_in_silhouette: {0}/{farm_limit}"
                                 )

        overview_embed.add_field(name="Punkte", value=f'{points}')

        overview_embed.add_field(name="Buildings",
                                 value=f":office: {0} :crossed_swords: {0} :horse: {0} :hammer_pick: {0} "
                                       f":european_castle: {0} :hammer: {0} :bow_and_arrow: {0} :statue_of_liberty:"
                                       f"{0}\n:department_store: {0} :wood: {0} :bricks: {0} :nut_and_bolt: {0} "
                                       f":farmer: {0} :classical_building: {0} :key: {0} :shield: {0}",
                                 inline=False
                                 )

        overview_embed.add_field(name="Troops",
                                 value=f":magic_wand: {0} :crossed_swords: {0} :axe: {0} :mag: {0} :horse_racing: {0}\n"
                                       f":carousel_horse: {0} :left_facing_fist: {0} :comet: {0} :dagger: {0}"
                                       f":crown: {0}",
                                 inline=False
                                 )

        await ctx.send(embed=overview_embed)

        # Add emojis

        # Register Listener

    @commands.command()
    async def map(self, ctx):
        """Shows the map"""
        map_embed = discord.Embed(
            color=ctx.author.color, timestamp=ctx.message.created_at,  title=f"Map centered at {ctx.author}"
        )
        # request villages

        await ctx.send(embed=map_embed)

    @commands.command()
    async def attack(self, ctx):
        """Attacks a village"""
        await ctx.send("Not implemented")

    # @commands.Cog.listener(): TODO: Do a eventlistener


def setup(client):
    client.add_cog(GameHandler(client))
