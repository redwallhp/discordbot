import discord
from discord.ext import commands
import asyncio

class Conversions:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def c(self, f : float):
        """Convert Fahrenheit to Celsius"""
        c = (f-32) * 5/9
        await self.bot.say("{0} Celsius".format(c))

    @commands.command()
    async def f(self, c : float):
        """Convert Celsius to Fahrenheit"""
        f = c * 9/5 + 32
        await self.bot.say("{0} Fahrenheit".format(f))

def setup(bot):
    bot.add_cog(Conversions(bot))
