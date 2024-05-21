import discord
from discord.ext import commands
import random


# Intents padrão da biblioteca discord.
intents = discord.Intents.default()

# Intents especificados que serão utilizados:
intents.messages = True
intents.message_content = True
intents.guilds = True

#Criação do prefixo do bot
client = commands.Bot(command_prefix='#', case_insensitive=True, intents=intents)

@client.event
async def on_ready():
    print('Entramos como {0.user}'.format(client))

@client.command()
async def ola(ctx):
    await ctx.send(f'olá {ctx.author}, meu consagrado.')

@client.command()
async def dado(ctx, numero):
    variavel = random.randint(1,int(numero))
    await ctx.send(f'O Número que saiu no dado foi: {variavel}')
    
@client.command()
async def a(ctx,*,mensagem):
    if mensagem == 'boa noite':
        await ctx.send('boa noite minha fera.')
    else:
        await ctx.send('coe paizao, fala baixo')


# Insira seu token aqui
TOKEN = 'token'

client.run(TOKEN)
