import discord
import os
from dotenv import load_dotenv
import webserver

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.messages = True 
intents.message_content = True  

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord! again...")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(f"Received message: {message.content}") 
    
    if message.content.startswith('https://x.com/') or message.content.startswith('https://twitter.com/'):
        link = message.content
        if link.startswith('https://twitter.com/'):
            fx_link = link.replace('https://twitter.com/', 'https://fxtwitter.com/')
        elif link.startswith('https://x.com/'):
            fx_link = link.replace('https://x.com/', 'https://fxtwitter.com/')

        await message.delete()
        await message.channel.send(f"From: {message.author.mention} \n{fx_link}")

webserver.keep_alive()
client.run(TOKEN)
