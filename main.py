# Packages
import discord

# Local
from src.classes.database import Database
from src.classes.bot import Bot
from src.classes.configuration import Configuration
from src.classes.messaging import MessageHandler


# Setup configuration
config = Configuration()
database = Database(database_path=config.database_path)
bot = Bot(token=config.discord_token)
message_handler = MessageHandler(bot=bot, config=config, database=database)


@bot.client.event
async def on_ready():
    print(f'Bot logged in as {bot.client.user}')


@bot.client.event
async def on_message(message: discord.Message):
    await message_handler.on_message(message)


@bot.client.event
async def on_thread_delete(thread: discord.Thread):
    database.delete_all_messages_in_channel(thread.id)

# Run the Discord bot
bot.run()
