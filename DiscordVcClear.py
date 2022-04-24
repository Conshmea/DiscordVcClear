import discord
from discord.ext import commands
import checkvc

#stuff
TOKEN = "[botToken]"
client = discord.Client()
bot = commands.Bot("vcc.")
bot.VC_messages = {}

#Bot connected readout
@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

#Checks if a message was posted in a VC and log it
@bot.event
async def on_message(message):
    if str(message.channel.type) == "voice":
        try:
            bot.VC_messages[message.channel.id].append(message)
        except KeyError:
            bot.VC_messages[message.channel.id] = []
            bot.VC_messages[message.channel.id].append(message)

#Add the Cog to monitor VCs
bot.add_cog(checkvc.CheckVc(bot))

#Run the bot
bot.run(TOKEN, bot=True, reconnect=True)

