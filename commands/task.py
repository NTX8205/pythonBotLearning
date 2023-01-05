import discord
from discord.ext import commands
from Main_Core.setbot import CogSetup_Extension

import json,asyncio,datetime

class task(CogSetup_Extension):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

        self.counter=0

        # async def interval():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(766770240477462528)
        #     while not self.bot.is_closed():
        #         await self.channel.send('the bot is running')
        #         await asyncio.sleep(5)

        # self.bg_task = self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(766770240477462528)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now().strftime('%H%M')
                with open('setting.json', 'r', encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time'] and self.counter==0:
                    await self.channel.send('task is useful')
                    self.counter=1
                    await asyncio.sleep(3)

                else:
                    await asyncio.sleep(3)
                    pass


        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set channel:{self.channel.mention} success!')

    @commands.command()
    async def set_time(self,ctx,time):
        self.counter=0
        with open('setting.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)

        jdata['time'] = time
        with open('setting.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent=4)

def setup(bot):
    bot.add_cog(task(bot))
