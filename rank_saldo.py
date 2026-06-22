import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

SALDOS = {
    1038929134090457238: 1516914901644214432,
    1282101053537390663: 1518064220216758304, 
    1267626324621525002: 1516914523011809483,
    1371596618322804747: 1518064772380102847, 
    769254925548519454: 1518065247074648216,
    568190975202164785: 1518065429388460155,
    1391101581000310836: 1518618328514564220,
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
