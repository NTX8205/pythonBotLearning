import discord
from discord.ext import commands
from Main_Core.setbot import CogSetup_Extension
import datetime

class Main(CogSetup_Extension):


    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'現在延遲 : {round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def hi(self,ctx):
        await ctx.send("hi how are you")


    @commands.command()
    async def em(self,ctx):
        embed = discord.Embed(
            title="測試", url="https://twitter.com/home?lang=zh-tw", description="bot ", color=0x78c9d3 ,timestamp = datetime.datetime.now(tz=datetime.timezone.utc))
        embed.set_author(name="time", url="https://twitter.com/AD0124578963",
                        icon_url="https://pbs.twimg.com/profile_images/918117889764237312/uQxG_AXX_400x400.jpg")
        embed.set_thumbnail(
            url="https://pbs.twimg.com/media/E53Pu2LVEAckkcl?format=jpg&name=900x900")
        embed.add_field(name="1", value="no1", inline=True)
        embed.add_field(name="2", value="no2", inline=True)
        embed.add_field(name="3", value="no3", inline=True)
        embed.add_field(name="4", value="no4", inline=True)
        embed.set_footer(text="bot_end")
        await ctx.send(embed=embed)

    @commands.command()
    async def repeat(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clear(self, ctx,num:int):
        await ctx.channel.purge(limit=num+1)

def setup(bot):
    bot.add_cog(Main(bot))