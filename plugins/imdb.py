import discord
from discord.ext import commands
import asyncio, aiohttp

class IMDB:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def imdb(self, *, title : str):
        """Find a movie title on IMDB"""
        res = await self.json_request("http://omdbapi.com", {'s': title})
        await self.bot.say(self.format_response(res))

    def format_response(self, res):
        pattern = "'{0}' ({1}) - http://www.imdb.com/title/{2}/"
        r = res['Search'][0]
        return pattern.format(r['Title'], r['Year'], r['imdbID'])

    async def json_request(self, url, params):
        async with aiohttp.get(url, params=params) as response:
            assert response.status == 200
            return await response.json()

def setup(bot):
    bot.add_cog(IMDB(bot))
