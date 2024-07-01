import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready ():
 print(f" \033[32m ☑️ conectado")
 await bot.tree.sync()

    
@bot.command(name='ping', help='Verificar o ping do bot')
async def ping(ctx: commands.Context):
    await ctx.send(f'🏓 Meu ping é {round(bot.latency * 1000)}ms')

@bot.command()
async def teste(ctx):
    await ctx.send('pong')

bot.run('token')
