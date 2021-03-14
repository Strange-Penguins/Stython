from discord.ext.commands import Bot
import discord
from datetime import datetime
import platform
import databasemanager as dbm


class CustomClient(Bot):

    def __init__(self, **options):
        self.creation_date = datetime.now()
        super().__init__(**options)
        self.loop.create_task(self.greet())
        self.db = dbm.DatabaseManager()

    async def greet(self):
        """Prints Info one time on startup"""
        await self.wait_until_ready()
        now_date = datetime.now()
        time_delta = now_date - self.creation_date
        print(
            f"----------\n[{now_date.strftime('%H:%M:%S')}] {self.user} started and connection established sucessfully."
            f"(Took:{round(time_delta.microseconds / 1_000_000, 1)}sec)\n"
            f">> Guilds: {[guild.name for guild in self.guilds]}\n"
            f">> Running on {platform.system()} "
            f"- Discord.py: {discord.__version__} - Python: {platform.python_version()}"
        )
