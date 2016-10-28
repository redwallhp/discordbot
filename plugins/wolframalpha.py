import discord
from discord.ext import commands
import asyncio, aiohttp
import re
import xml.etree.ElementTree as ET
from lib import configurator

class WolframAlpha:

    def __init__(self, bot):
        self.bot = bot
        self.apikey = configurator.getString('wolfram_key', None)

    @commands.command()
    async def wa(self, *, query : str):
        """Ask Wolfram Alpha a question"""
        if self.apikey == None:
            await self.bot.say("A Wolfram Alpha API key must be configured to use this command.")
            return
        params = {
            "appid": self.apikey,
            "input": query,
            "format": "plaintext"
        }
        res = await self.http_request("http://api.wolframalpha.com/v2/query", params)
        text = await self.extract_response(res)
        await self.bot.say(text)

    async def extract_response(self, res):
        xml = ET.fromstring(res)
        success = xml.get('success') == 'true'
        if success:
            pods = xml.findall('.//pod[@primary=\'true\']/subpod/plaintext')
            if len(pods) < 1:
                return "No result found."
            results = pods[-1].text.split('\n')
            return ', '.join(results)
        else:
            return "No result found."

    async def http_request(self, url, params):
        async with aiohttp.get(url, params=params) as response:
            assert response.status == 200
            return await response.text()

def setup(bot):
    bot.add_cog(WolframAlpha(bot))
