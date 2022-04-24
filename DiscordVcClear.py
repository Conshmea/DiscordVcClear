import discord
from discord.ext import commands
import checkvc

TOKEN = "[botToken]"

client = discord.Client()





bot = commands.Bot("vcc.")

bot.VC_messages = {}

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

@bot.event
async def on_message(message):
    if str(message.channel.type) == "voice":
        try:
            bot.VC_messages[message.channel.id].append(message)
        except KeyError:
            bot.VC_messages[message.channel.id] = []
            bot.VC_messages[message.channel.id].append(message)

#@bot.command()
#async def channel(ctx):
#    await ctx.send(f"{ctx.author.mention}, {ctx.channel}")
#    await ctx.message.delete()

bot.hi = "Starting"

bot.add_cog(checkvc.CheckVc(bot))

bot.run(TOKEN, bot=True, reconnect=True)

