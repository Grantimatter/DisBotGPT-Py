import discord
from functools import wraps


# Discord bot class
class Bot:
    def __init__(self, token: str):
        self.token = token

        # Set up discord client intents
        self.intents = discord.Intents()
        self.intents.message_content = True
        self.intents.messages = True
        self.intents.typing = True
        self.intents.guilds = True
        self.intents.guild_messages = True
        # Set up Discord client
        self.client = discord.Bot(intents=self.intents)

    def run(self):
        self.client.run(self.token)
