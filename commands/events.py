import discord
from discord.ext import commands
from Main_Core.setbot import CogSetup_Extension

import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Event(CogSetup_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['demo_channel']))
        await channel.send(f"{member} join")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['demo_channel']))
        await channel.send(f"{member} leave")


    @commands.Cog.listener()
    async def on_message(self,msg):
        keywords = ['apple','pen','hi','you']
        if msg.content in keywords and msg.author != self.bot.user:
            await msg.channel.send('success')


def setup(bot):
    bot.add_cog(Event(bot))
