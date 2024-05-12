#O TOKEN foi removido por questões de segurança.

import discord
from discord.ext import commands
import random


# Intents do bot
intents = discord.Intents.default()

intents.messages = True
intents.message_content = True
intents.guilds = True

client = commands.Bot(command_prefix='!!', case_insensitive=True, intents=intents)

@client.event
async def on_ready():
    print('Entramos como {0.user}'.format(client))

@client.command()
async def ola(ctx):
    await ctx.send(f'olá {ctx.author}, meu consagrado')

@client.command()
async def dado(ctx, numero):
    variavel = random.randint(1,int(numero))
    await ctx.send(f'O Número que saiu no dado foi {variavel}')

#Inserir TOKEN 
TOKEN = 'token'

client.run(TOKEN)
