import discord
from discord.ext import commands
from lib import perms
import asyncio

class Admin:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @perms.is_owner()
    async def botsay(self, ctx, channelid : str, *, msg : str):
        """Speak as the bot. Usage: .botsay <chan_id> <msg>"""
        chan = self.bot.get_server(channelid)
        await self.bot.send_message(chan, msg)

def setup(bot):
    bot.add_cog(Admin(bot))
