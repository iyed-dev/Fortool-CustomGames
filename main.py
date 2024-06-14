import discord
from discord.ext import commands

def get_prefix(client, message):
    prefixes = ['*']
    return commands.when_mentioned_or(*prefixes)(client, message)

# Define the intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True  # Enable messages intent
intents.message_content = True  # Enable message content intent

bot = commands.Bot(
    command_prefix=get_prefix,
    description='Bot pour créer des parties personnalisées',
    owner_id=394621750987456522,
    case_insensitive=True,
    intents=intents
)

cogs = ['cogs.solo', 'cogs.duo', 'cogs.section', 'cogs.soloprivate', 'cogs.duoprivate', 'cogs.sectionprivate', 'cogs.arene', 'cogs.areneprivate', 'cogs.register', 'cogs.setup']

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name} - {bot.user.id}')
    await bot.change_presence(activity=discord.Game("Fortnite 🛒"))
    for cog in cogs:
        await bot.load_extension(cog)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = "Veuillez patientez `{:.2f}s` puis ensuite réssayer".format(error.retry_after)
        await ctx.send(msg)

bot.run("TOKEN BOT", reconnect=True)
