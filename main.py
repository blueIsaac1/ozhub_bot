import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTMxOTEwNTUyNDc0NjE2MjIxNw.GFCeRS.Db0Zj8-3YJNqAiFRY0XWhed0sXTBUygaMfVJxI')

# permission interger: 2419452944