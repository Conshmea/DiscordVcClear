import discord
from discord.ext import commands

class CheckVc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Vcs = {}

        print(bot.hi)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        print(member, before.channel, after.channel)
        try:
            if before.channel == None:
                self.Vcs[str(after.channel)].append(f"{member.name}#{member.discriminator}")
            else:
                self.Vcs[str(before.channel)].remove(f"{member.name}#{member.discriminator}")
        except KeyError:
            if before.channel == None:
                self.Vcs[str(after.channel)] = []
                self.Vcs[str(after.channel)].append(f"{member.name}#{member.discriminator}")
            else:
                self.Vcs[str(before.channel)] = []
                self.Vcs[str(before.channel)].remove(f"{member.name}#{member.discriminator}")

        if before.channel != None:
            print(self.bot.VC_messages[before.channel.id])
            if self.Vcs[str(before.channel)] == []:
                for message in self.bot.VC_messages[before.channel.id]:
                    await message.delete()
                self.bot.VC_messages[before.channel.id] = []
