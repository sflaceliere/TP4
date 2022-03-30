
from discord import Client
import discord



class MyBot(Client):
    def __init__(self):
        super().__init__()
        self.run("OTU4NjkyOTE1OTMxMTUyNDY1.YkRCWg.Gt1yl-Gmw1msMHVFk44q2ITlEvU")

   # async def on_ready(self):
   #a     self.log.infolog(f"{self.user} has connected to Discord!")

    # Créer un événement
    async def on_ready(self):
        print("Le bot est prêt !")

    async def on_message(ctx, message):
        if message.content == "Ping":
            await message.channel.send("Pong")
    
    async def on_messages(message):
        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete()

bot = MyBot() #instance