import discord
from discord.ext import commands
from lib import configurator

enabled_plugins = [
    "plugins.admin",
    "plugins.conversions",
    "plugins.imdb",
    "plugins.insults",
    "plugins.mcstatus",
    "plugins.responses",
    "plugins.rss",
    "plugins.wolframalpha"
]

description = '''A bot for the Nerd.nu Discord guild'''
bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('Logged in as {0} with ID {1}'.format(bot.user.name, bot.user.id))
    print('Joined {0} servers'.format(len(bot.servers)))

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.errors.CheckFailure):
        await bot.send_message(ctx.message.channel, "You don't have permission to run that command.")

def load_plugins():
    for p in enabled_plugins:
        try:
            print("Loading plugin: " + p)
            bot.load_extension(p)
        except Exception as e:
            print('Failed to load extension {0}\n{1}: {2}'.format(p, type(e).__name__, e))

if __name__ == '__main__':
    load_plugins()
    bot.run(configurator.getString('token', None))
