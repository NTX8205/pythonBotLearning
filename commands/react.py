import discord
from discord.ext import commands
from Main_Core.setbot import CogSetup_Extension

import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class React(CogSetup_Extension):


    @commands.command()
    async def 圖片(self,ctx):
        random_pic = random.choice(jdata['pic1'])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)


    @commands.command()
    async def webpic(self,ctx):
        random_urlpic = random.choice(jdata['url'])
        await ctx.send(random_urlpic)


def setup(bot):
    bot.add_cog(React(bot))
