from discord import DMChannel
import nextcord
from nextcord.ext import commands
import random
import typing
from typing import Optional
import asyncio

class rand(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def pp(self, ctx: commands.Context, member: Optional[nextcord.Member] = None):
        size = ['8D 🔍', '8=D', '8==D', '8===D', '8====D', '8=====D', '8======D', '8=======D', '8========D', '8=========D', '8==========D', 'E=======8 (backwards pp)', 'Too big to calculate']
        choose_pp = random.choice(size)
        member = member or ctx.author

        embed = nextcord.Embed(
            title='PP Calculator',
            description=f'{member.mention} pp is `{choose_pp}` long',
            color= nextcord.Color.random()
        )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def gayrate(self, ctx: commands.Context, member: Optional[nextcord.Member] = None):
        rate = ["0%","1%","2%","3%","4%","5%","6%","7%","8%","9%","10%","11%","12%","13%","14%","15%","16%","17%","18%","19%","20%","21%","22%","23%","24%","25%","26%","27%","28%","29%","30%","31%","32%","33%","34%","35%","36%","37%","38%","39%","40%","41%","42%","43%","44%","45%","46%","47%","48%","49%","50%","51%","52%","53%","54%","55%","56%","57%","58%","59%","60%","61%","62%","63%","64%","65%","66%","67%","68%","69%","70%","71%","72%","73%","74%","75%","76%","77%","78%","79%","80%","81%","82%","83%","84%","85%","86%","87%","88%","89%","90%","91%","92%","93%","94%","95%","96%","97%","98%","99%","100%"]
        choose_rate = random.choice(rate)
        member = member or ctx.author

        embed = nextcord.Embed(
            title='🏳‍🌈 Gay Rate Calculator',
            description=f'{member.mention} is {choose_rate} Gay',
            color= nextcord.Color.random()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def report(self, ctx):
        embed = nextcord.Embed(
            title='Reports',
            description = 'To report someone use the link below to report them\n',
            color=nextcord.Color.random()
        )
        await ctx.author.send(embed=embed)
        await ctx.reply("Check your dms.")
      
    
 
def setup(client):
    client.add_cog(rand(client))