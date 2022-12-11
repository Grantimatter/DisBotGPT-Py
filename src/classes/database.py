import sqlite3
import discord


# Database class that keeps track of discord message id as text, message thread as text, if thread is gpt
# conversation as boolean, parent_id as text, conversation_id as text
class Database:
    def __init__(self, database_path: str):
        self.database_path = database_path

        # Create database file if it does not exist
        open(self.database_path, "a").close()

        # Connect to database
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()

        # Create table if it does not already exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
            discord_message_id INTEGER PRIMARY KEY,
            parent_id TEXT,
            conversation_id TEXT,
            discord_channel_id INTEGER
        )''')

        # Commit changes
        self.connection.commit()

    def get_conversation_id_and_parent_id(self, discord_message: discord.Message):
        # Get conversation id and parent id from database
        self.cursor.execute('''SELECT conversation_id, parent_id FROM messages WHERE discord_channel_id = ?''',
                            (discord_message.channel.id,))

        # Return conversation id and parent id
        return self.cursor.fetchone()

    def get_conversation_id(self, message: discord.Message):
        # Get conversation id from database
        self.cursor.execute('''SELECT conversation_id FROM messages WHERE discord_channel_id = ?''',
                            (message.channel.id,))

        # Return conversation id
        return self.cursor.fetchone()

    def add_message(self, discord_message_id: int, parent_id: str,
                    conversation_id: str, discord_channel_id: int):
        # Add message to database
        self.cursor.execute('''INSERT INTO messages VALUES (?, ?, ?, ?)''',
                            (discord_message_id, parent_id, conversation_id, discord_channel_id))

        print('adding to database')
        # Commit changes
        self.connection.commit()

    def get_message(self, discord_message_id: int):
        # Get message from database
        self.cursor.execute('''SELECT * FROM messages WHERE discord_message_id = ?''', (discord_message_id,))

        print('Found message in database')
        # Return message
        return self.cursor.fetchone()

    def update_message(self, discord_message_id: int, discord_channel_id: int, parent_id: str,
                       conversation_id: str):
        # Update message in database
        self.cursor.execute(
            '''UPDATE messages SET discord_channel_id = ?, parent_id = ?, conversation_id = ? WHERE discord_message_id = ?''',
            (discord_channel_id, parent_id, conversation_id, discord_message_id))

        # Commit changes
        self.connection.commit()

    def delete_message(self, discord_message_id: str):
        # Delete message from database
        self.cursor.execute('''DELETE FROM messages WHERE discord_message_id = ?''', (discord_message_id,))

        # Commit changes
        self.connection.commit()

    def delete_all_messages_in_channel(self, discord_channel_id: int):
        # Delete all messages in channel from database
        self.cursor.execute('''DELETE FROM messages WHERE discord_channel_id = ?''', (discord_channel_id,))

        print('Deleting all messages in channel from database')
        # Commit changes
        self.connection.commit()

    def close(self):
        # Close connection
        self.connection.close()
