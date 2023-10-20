import discord
import responses
import os
from dotenv import load_dotenv

load_dotenv()

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        # Send to private if is_private
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as e:
        print(e)

def run_discord_bot():

    # To not ignoring user's messages
    intents = discord.Intents().all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print (f"{client.user} is now running!")

    @client.event
    async def on_message(message):
        if message.author == client.user:  # makes sure the bot does not reply to itself
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        is_private = isinstance(message.channel, discord.DMChannel)
        
        # Initialize with character "?" (can be any prefix) to get directed message
        if user_message and user_message[0] == "?":
            user_message = user_message[1:] # removing the "?" character
            await send_message(message, user_message, is_private = True)
        elif user_message:
            await send_message(message, user_message, is_private = False)

        await send_message(message, user_message, is_private = False)


    client.run(os.getenv("TOKEN"))