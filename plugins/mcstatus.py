import discord
from discord.ext import commands
from mcstatus import MinecraftServer
from lib import configurator
import asyncio

class MCStatus:

    def __init__(self, bot):
        self.bot = bot
        self.servers = configurator.getList('minecraft_servers', ['nerd.nu'])

    @commands.command()
    async def status(self):
        """Checks the status of configured Minecraft servers"""
        response = "```\n"
        for server in self.servers:
            response += await self.ping(server) + "\n"
        response += "```\n"
        await self.bot.say(response)

    async def ping(self, host):
        try:
            server = MinecraftServer(host, 25565)
            status = server.status()
            return "{0} [{1}/{2}]".format(host, status.players.online, status.players.max)
        except Exception as e:
            return "{0} seems to be down".format(host)

def setup(bot):
    bot.add_cog(MCStatus(bot))
