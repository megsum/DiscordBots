import discord
import asyncio
import insult
import sys
from random import randint

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.wait_until_ready()
	channel = client.get_channel(355230783511855105)
	await channel.send('Megatron Activated!')

@client.event
async def on_message(message):
	bot = message.author
	
	if message.content.startswith('!test'):
		bot_insult = insult.random_insult()
		await message.channel.send( ' Thou ' + bot_insult)
	
	elif str(bot) != "Megatron#0236" and "robots" in [y.name.lower() for y in bot.roles]:
		bot_insult = insult.random_insult()
		await message.channel.send(bot.name  + ' : Thou ' + bot_insult)
		
	elif message.content.startswith('m!exit'):
			await message.channel.send("I'll be back")
			await client.logout()
			sys.exit()

client.run('MzU1MjM3NzE2ODQ3NDkzMTIx.XxN9nA.VIlBJyotinERuZDRk6XtYUobLKM')
