import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

@bot.command()
async def rank(ctx):
    canal = bot.get_channel(1512862501237297393)

    msg = await canal.fetch_message(1512879697359405228)

    if msg.embeds:
        await ctx.send(embed=msg.embeds[0])
    else:
        await ctx.send("Nenhum embed encontrado.")

@bot.command()
async def saldo(ctx):
    await ctx.send(f"💰 Teste de saldo para {ctx.author.display_name}")

TOKEN = os.getenv("MTUxNjg5MDg4MzE2ODAxNDM4Ng.GPFsv3.AfWEmeQN5pxjukr6L0_VvP24__tJyombr4qMyo")

bot.run(TOKEN)