import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")
default_Intents = discord.Intents.default()
default_Intents.members = True
client = discord.Client(intents=default_Intents)
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Le bot es prêt.")
    print("Prêt à être lancé")
    print('-------')


@bot.command(name='start')
async def on_message(message):
    await message.channel.send("Le bot est lancé.", delete_after=5)
    print("Le bot a été lancé.")


@bot.event
async def on_member_join(member):
    arrivee_channel: discord.TextChannel = client.get_channel(992164726358425620)
    await arrivee_channel.send(content=f"Bienvenue dans le discord {member.display.name} !")


@bot.command(name='clear')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_message in messages:
        await each_message.delete()
    print(f"Un utilisateur à supprimé {number_of_messages} message(s)(pour plus d'informations va voir dans les logs).")


bot.run(os.getenv("TOKEN"))
