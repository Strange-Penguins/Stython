from discord.ext.commands import Bot


class CustomClient(Bot):

    def __init__(self, **options):
        super().__init__(**options)
