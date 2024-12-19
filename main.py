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

def update_html(bot_info):
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <title>Bot Status</title>
    <meta http-equiv="refresh" content="30">  <!-- Atualiza a página a cada 30 segundos -->
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f0f0f0;
        }}
        .status-card {{
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            max-width: 500px;
            margin: 0 auto;
        }}
        .status-item {{
            margin: 10px 0;
            padding: 10px;
            border-bottom: 1px solid #eee;
        }}
        .online {{
            color: #43b581;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="status-card">
        <h1>Status do Bot</h1>
        <div class="status-item">
            <strong>Nome:</strong> {bot_info['name']}
        </div>
        <div class="status-item">
            <strong>ID:</strong> {bot_info['id']}
        </div>
        <div class="status-item">
            <strong>Servidores:</strong> {bot_info['guild_count']}
        </div>
        <div class="status-item">
            <strong>Status:</strong> <span class="online">{bot_info['status']}</span>
        </div>
        <div class="status-item">
            <strong>Última Atualização:</strong> {bot_info['last_update']}
        </div>
    </div>
</body>
</html>
    """
    
    with open('page.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

# Evento quando o bot está pronto
@bot.event
async def on_ready():
    bot_info = {
        'name': bot.user.name,
        'id': str(bot.user.id),
        'guild_count': len(bot.guilds),
        'status': 'Online',
        'last_update': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Atualiza o arquivo HTML
    update_html(bot_info)

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