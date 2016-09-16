import discord
from discord.ext import commands
import asyncio, aiohttp
import json
import feedparser
from lib import configurator
from lib import persistence

class RSS:

    def __init__(self, bot):
        self.bot = bot
        self.config = configurator.getJson()
        self.load_feed_list()
        self.bookmarks = persistence.load('rss')
        self.bot.loop.create_task(self.task_background_fetch())

    def load_feed_list(self):
        self.feeds = {}
        if 'rss_feeds' in self.config:
            self.feeds = self.config['rss_feeds']

    async def task_background_fetch(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed:
            await self.fetch_feeds()
            await asyncio.sleep(600)

    async def http_request(self, url):
        async with aiohttp.get(url) as response:
            assert response.status == 200
            return await response.read()

    async def fetch_feeds(self):
        for url, channel in self.feeds.items():
            resp = await self.http_request(url)
            f = feedparser.parse(resp)
            print("Fetched feed: " + url)
            if (len(f.entries) > 0):
                if self.bookmarks.get(url) != f.entries[0].link:
                    self.bookmarks[url] = f.entries[0].link
                    await self.broadcast_link(channel, f.entries[0])
        persistence.save('rss', self.bookmarks)

    async def broadcast_link(self, channel_id, entry):
        channel = discord.Object(id=channel_id)
        msg = "{0} {1}".format(entry.title, entry.link)
        await self.bot.send_message(channel, msg)

def setup(bot):
    bot.add_cog(RSS(bot))
