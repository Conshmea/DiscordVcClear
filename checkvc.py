import discord
from discord.ext import commands

class CheckVc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Vcs = {}

    #runs on user joining or leaving VC
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        print(member, before.channel, after.channel)
        
        #When user joins or leaves VC add or remove them from that VCs list. If there is no list create one
        try:
            if after.channel != None:
                self.Vcs[str(after.channel)].append(f"{member.name}#{member.discriminator}")
            else:
                self.Vcs[str(before.channel)].remove(f"{member.name}#{member.discriminator}")
        except KeyError:
            if after.channel != None:
                self.Vcs[str(after.channel)] = []
                self.Vcs[str(after.channel)].append(f"{member.name}#{member.discriminator}")
            else:
                self.Vcs[str(before.channel)] = []
                self.Vcs[str(before.channel)].remove(f"{member.name}#{member.discriminator}")

        #If it is the last user to leave the VC delete and clear the logged messagesfor the VC
        if before.channel != None:
            print(self.bot.VC_messages[before.channel.id])
            if self.Vcs[str(before.channel)] == []:
                for message in self.bot.VC_messages[before.channel.id]:
                    await message.delete()
                self.bot.VC_messages[before.channel.id] = []
