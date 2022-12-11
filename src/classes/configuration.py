import configparser
import os


class Configuration:
    def __init__(self):
        # Create a ConfigParser instance
        self.config = configparser.ConfigParser()

        # Check if the config.ini file exists
        if not os.path.exists("config.ini"):
            # If the file does not exist, create it and get user input for the configuration settings
            self.create_config_file()
        else:
            # If the file exists, read the configuration settings
            self.config.read("config.ini")

            # Check if the required settings are present
            if not self.config.has_section("database") or not self.config.has_option("database", "path"):
                print("Missing 'database.path' setting in config.ini")
                self.prompt_for_database_path()
            if not self.config.has_section("openai") or not self.config.has_option("openai", "email"):
                print("Missing 'openai.email' setting in config.ini")
                self.prompt_for_openai_email()
            if not self.config.has_section("openai") or not self.config.has_option("openai", "password"):
                print("Missing 'openai.password' setting in config.ini")
                self.prompt_for_openai_password()
            if not self.config.has_section("discord") or not self.config.has_option("discord", "token"):
                print("Missing 'discord.token' setting in config.ini")
                self.prompt_for_discord_token()
            if not self.config.has_section("bot") or not self.config.has_option('bot', 'thread_title_prompt'):
                print("Missing 'bot.thread_title_prompt' setting in config.ini")
                self.prompt_for_thread_title_prompt()

        with open("config.ini", "w") as f:
            self.config.write(f)

        self.database_path = self.config["database"]["path"]
        self.openai_email = self.config["openai"]["email"]
        self.openai_password = self.config["openai"]["password"]
        self.discord_token = self.config["discord"]["token"]
        self.thread_title_prompt = self.config["bot"]["thread_title_prompt"]

    # Run all prompts for user config
    def create_config_file(self):
        self.prompt_for_database_path()
        self.prompt_for_openai_email()
        self.prompt_for_openai_password()
        self.prompt_for_discord_token()
        self.prompt_for_thread_title_prompt()

    def prompt_for_database_path(self):
        # Get user input for the 'database.path' setting
        database_path = input("Enter a path for the database:")
        self.config["database"]["path"] = database_path

    def prompt_for_openai_email(self):
        # Get user input for the 'openai.email' setting
        openai_email = input("Enter your OpenAI email:")
        print(openai_email)
        self.config["openai"]["email"] = openai_email

    def prompt_for_openai_password(self):
        # Get user input for the 'openai.password' setting
        openai_password = input("Enter your OpenAI password:")
        self.config["openai"]["password"] = openai_password

    def prompt_for_discord_token(self):
        # Get user input for the 'discord.token' setting
        discord_token = input("Enter the bot token:")
        self.config["discord"]["token"] = discord_token

    def prompt_for_thread_title_prompt(self):
        # Get user input for the 'bot.thread_title_prompt' setting
        thread_title_prompt = input("Enter the prompt that will generate thread titles:")
        self.config["bot"]["thread_title_prompt"] = thread_title_prompt
