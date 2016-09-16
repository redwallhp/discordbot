from discord.ext import commands
from lib import configurator

ownerid = configurator.getString('owner', '133894531950182400')

def is_owner():
    def perform_check(ctx):
        return ctx.message.author.id == ownerid
    return commands.check(lambda ctx: perform_check(ctx))
