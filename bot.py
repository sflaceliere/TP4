from discord import Client
import discord
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")


class MyBot(Client):
    def __init__(self):
        super().__init__()
        self.run("OTU4NjkyOTE1OTMxMTUyNDY1.YkRCWg.M7i9flltvGk-hLhZHDld-Lm8A0U")

   # async def on_ready(self):
   #a     self.log.infolog(f"{self.user} has connected to Discord!")

    # Créer un événement
    async def on_ready(self):
        print("Le bot est prêt !")

    def setprefix():
        prefix = "!"

    async def on_message(ctx, message):
        print(message.content)
        if message.content == "ping":
            await message.channel.send("Pong")
        if len(message.mentions) == 1:
            if message.content == "<@277429748609843200>":
                await message.channel.send("Il arrive")
            if message.content == "<@270144723950370817>":
                await message.channel.send("Le ping pas c le boss")
        file1 = open("logs.txt", "a")
        file1.write(f'{message.content}, {str(message.author)}')
        file1.write("\n")
        file1.close()
        
    async def help(ctx):
        discord.Embed(title = "Help", description = "Informations about commands")


    async def on_messages(message):
        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete()
    
    async def on_member_join(self, member): 
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Heyyy Welcome {0.mention} to {1.name}! S E B is happy to see you'.format(member, guild)
            await guild.system_channel.send(to_send)

    async def help(context):
        await context.send("Custom help command")

bot = MyBot() #instance
default_intents = discord.Intents.default()
intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
