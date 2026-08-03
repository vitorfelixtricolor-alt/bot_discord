import discord
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} está online!")

@bot.command()
async def clima(ctx):
    await ctx.send(
        "**🌎 O que é a mudança climática?**\n\n"
        "Mudança climática é a alteração de longo prazo no clima da Terra. "
        "Ela provoca mudanças na temperatura, nas chuvas e em outros fenômenos naturais."
    )

@bot.command()
async def gravidade(ctx):
    await ctx.send(
        "**⚠️ Qual é a gravidade desse problema?**\n\n"
        "É um problema global que afeta todos. Pode causar ondas de calor, secas, "
        "enchentes, aumento do nível do mar e perda da biodiversidade."
    )

@bot.command()
async def causas(ctx):
    await ctx.send(
        "**🏭 O que causa as mudanças climáticas?**\n\n"
        "A principal causa é a emissão de gases de efeito estufa pela queima de "
        "combustíveis fósseis, desmatamento, indústrias e agropecuária."
    )

@bot.command()
async def solucoes(ctx):
    await ctx.send(
        "**🌱 Como podemos conter as mudanças climáticas?**\n\n"
        "Podemos reduzir a emissão de gases poluentes, preservar as florestas, "
        "usar energias renováveis, economizar energia, reciclar e consumir de forma consciente."
    )

bot.run(TOKEN)






