import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    waterboy_quotes = [
        'Bobby Boucher, what did momma tell you about girls!',
        'Bingpot!',
        (
            'My Mama says that alligators are ornery because they got all them teeth and no toothbrush.'
        ),
    ]

    stepbrother_quotes = [
        'That is so funny, the last time I heard that I laughed so hard I fell off my dinosaur.',
        'Why are you so sweaty? I was watching Cops.',
        'When I was a kid...I wanted to be a Tyrannosaurus Rex more than anything in the world. I made my arms short and I roamed the backyard, I chased the neighborhood cats, I growled and I roared. Everybody knew me and was afraid of me.',
        'You and your mom are hillbillies. This is a house of learned doctors.',
    ]

    if message.content == 'talk!':
        #response = random.choice(waterboy_quotes)
        response = random.choice(stepbrother_quotes)
        await message.channel.send(response)

client.run(TOKEN))
