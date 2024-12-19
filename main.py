import discord
from discord.ext import commands
import datetime

# Configuração de intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Para eventos relacionados a membros
intents.presences = True  # Para status de presença

# Configuração do bot com mais opções
bot = commands.Bot(
    command_prefix='$',  # Prefixo dos comandos
    intents=intents,
    case_insensitive=True,  # Comandos não distinguem maiúsculas/minúsculas
    help_command=None,  # Desativa o comando help padrão
    activity=discord.Activity(
        type=discord.ActivityType.playing,
        name="Digite $help"
    ),  # Status do bot
    status=discord.Status.online  # Status online (pode ser: online, idle, dnd, invisible)
)

# Evento quando o bot está pronto
@bot.event
async def on_ready():
    print(f'Bot está online!')
    print(f'Nome: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print(f'Quantidade de servidores: {len(bot.guilds)}')
    print('----------------------------------------')

# Comando de help personalizado
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Ajuda do Bot",
        description="Lista de comandos disponíveis",
        color=discord.Color.blue(),
        timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(name="$hello", value="Envia uma saudação", inline=False)
    embed.set_footer(text=f"Solicitado por {ctx.author.name}")
    await ctx.send(embed=embed)

# Tratamento de erros
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Comando não encontrado! Use $help para ver os comandos disponíveis.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Você não tem permissão para usar este comando!")
    else:
        print(f'Erro: {error}')

# Evento quando um membro entra no servidor
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f'Bem-vindo(a) {member.mention} ao servidor!')

# Seu comando hello original
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

bot.run('MTMxOTEwNTUyNDc0NjE2MjIxNw.GFCeRS.Db0Zj8-3YJNqAiFRY0XWhed0sXTBUygaMfVJxI')

#token: MTMxOTEwNTUyNDc0NjE2MjIxNw.GFCeRS.Db0Zj8-3YJNqAiFRY0XWhed0sXTBUygaMfVJxI
# permission interger: 2419452944