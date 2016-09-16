import discord
from discord.ext import commands
from lib import configurator
import asyncio

class Responses:

    def __init__(self, bot):
        self.bot = bot
        self.phrases = configurator.getDict('responses', {})
        self.bot.async_event('on_message')

    async def on_message(self, msg):
        if msg.author.bot:
            return
        for phrase, response in self.phrases.items():
            if phrase.lower() in msg.content.lower():
                await self.bot.send_message(msg.channel, response)


def setup(bot):
    bot.add_cog(Responses(bot))
