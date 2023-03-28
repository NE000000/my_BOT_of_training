import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")
default_Intents = discord.Intents.default()
default_Intents.members = True
client = discord.Client(intents=default_Intents)


class BotTest(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!')

# information une fois le bot lancé
    async def on_ready(self):
        print("Le bot est lancé")
        print(self.user.name)
        print(self.user.id)
        print("--------------------------")
        print(f"{self.user} est connecté au serveur")

# commande 'start' pour allumer le bot dans le serveur
        @BotTest.command(self, name='start')
        async def on_message(ctx):
            await ctx.channel.send("Le bot est lancé !", delete_after=5)
            print(f"'{self.user.name}' a été lancé !")

# commande 'clear' pour supprimer des messages dans le serveur
            @BotTest.command(self, name='clear')
            async def delete(ctx, number_of_messages: int):
                messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()
                print(f"Messages supprimées : {number_of_messages}")

                for each_message in messages:
                    await each_message.delete()


bot_test = BotTest()
bot_test.run(os.getenv("TOKEN"))
