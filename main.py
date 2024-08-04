import discord
from discord.ext import commands
import random
import billboard as bb

# Defina os intents
intents = discord.Intents.default()

#Intents(permissões do bot)
intents.messages = True
intents.message_content = True
intents.guilds = True

#Criação do prefixo do bot
client = commands.Bot(command_prefix='#', case_insensitive=True, intents=intents)

@client.event
async def on_ready():
    print('Entramos como {0.user}'.format(client))

#Comando para dizer olá
@client.command()
async def ola(ctx):
    await ctx.send(f'olá {ctx.author}, meu consagrado.')

#Comando de rolar um dado de faces escolhidas pelo usuário:
@client.command()
async def dado(ctx, numero: int):
    rolagem = random.randint(1,int(numero))
    await ctx.send(f'O Número que saiu no dado foi: {rolagem}')
    

#Comando de conversa com o bot:    
@client.command()
async def snoopy(ctx, *, mensagem: str):

    #Mensagens para o comando 'boa noite'
    msgsboanoite = ['boa noite meu parceiro, como vai a vida?','boa noite, deus lhe abençoe','bom dia ainda irmao','boa tarde!','eaí']

    if mensagem == 'boa noite'.lower().strip():
        await ctx.send(random.choice(msgsboanoite))

    elif mensagem == 'bom dia'.lower().strip():
        await ctx.send('buenos dias muchacho')

    elif mensagem == 'feliz dia'.lower().strip():
        await ctx.send('feliz dia das mães para todos os pombos e suas mães')
    
    elif mensagem == 'fala comigo'.lower().strip():
        await ctx.send('FAAAAAAAAAAAAAAAALA COMIGO')
    else:
        await ctx.send(f'coe {ctx.author}, fala baixo')


#Curiosidades biológicas:
@client.command()
async def bio(ctx):

    #Mensagens para o comando 'bio'
    curiosidades = ['Em relação ao tamanho, o músculo mais forte do corpo é a língua','A maior célula do corpo humano é o óvulo feminino e o menor é o espermatozoide masculino',
                    'O maior órgão interno é o intestino delgado.','O cérebro é muito mais ativo à noite do que durante o dia',
                    'Durante a sua vida, você produzirá saliva suficiente para encher duas piscinas olímpicas',
                    'O coração das mulheres bate mais rápido que o dos homens',
                    'Seus olhos são sempre do mesmo tamanho desde o nascimento até a morte, mas o nariz e as orelhas nunca param de crescer',
                    'Nossos olhos podem identificar cerca de 10 milhões de cores e o olfato pode registrar 50000 perfumes',
                    'Se os olhos humanos fossem câmeras fotográficas digitais, seriam de 576 megapixels',
                    'Em qualquer dia, a relação sexual acontece cerca de 120 milhões de vezes na terra',
                    'O cérebro em si não pode sentir dor'
                    ]

    await ctx.send(f'{ctx.author}, você sabia que {random.choice(curiosidades)}?')

# Definição do comando assíncrono
@client.command()
async def billboard(ctx, numero: int):
    # Obter os dados do Billboard Hot 100: biblioteca 'billboard.py'
    chart = bb.ChartData('hot-100')
    if numero < 1 or numero > len(chart):
        await ctx.send("Por favor, forneça um número entre 1 e 100.")
        return

    # Obter os dados da música específica
    song = chart[numero - 1]
    # Enviar a mensagem com o resultado
    await ctx.send(f'O top {numero} de hoje é "{song.title}" por {song.artist}')

@client.command()
async def billboard_top(ctx, numero: str):
    try:
        numero = int(numero) 
    except ValueError:
        await ctx.send("Por favor, forneça um número inteiro válido.")
        return

    chart = bb.ChartData('hot-100')
    if numero < 1 or numero > len(chart):  
        await ctx.send("Por favor, forneça um número entre 1 e 100.")
        return

    for i in range(numero):
        song = chart[i]
        await ctx.send(f' {i + 1} - {song.title} - {song.artist}')

#Token:
TOKEN = '' #TOKEN vazio por segurança.
client.run(TOKEN)
