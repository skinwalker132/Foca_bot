import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

SALDOS = {
    1038929134090457238: 1516886820342857820,
}

CANAL_SALDOS = 1512874142972510441

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

    mensagem_id = SALDOS.get(ctx.author.id)

    if not mensagem_id:
        await ctx.send("❌ Você não possui um saldo cadastrado.")
        return

    canal = bot.get_channel(CANAL_SALDOS)

    if canal is None:
        await ctx.send("❌ Canal de saldos não encontrado.")
        return

    try:
        msg = await canal.fetch_message(mensagem_id)

        if msg.embeds:
            await ctx.send(embed=msg.embeds[0])
        else:
            await ctx.send("❌ A mensagem não possui embed.")

    except Exception as e:
        await ctx.send(f"❌ Erro ao buscar saldo: {e}")

TOKEN = os.getenv("DISCORD_TOKEN")

bot.run(TOKEN)
