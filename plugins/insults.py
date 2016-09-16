import discord
from discord.ext import commands
import asyncio
import random

# Shakespearean insult word list credit: http://www.pangloss.com/seidel/shake_rule.html

class Insults:

    def __init__(self, bot):
        self.bot = bot
        self.word1 = ["artless","bawdy","beslubbering","bootless","churlish","cockered","clouted","craven","currish","dankish","dissembling","droning","errant","fawning","fobbing","froward","frothy","gleeking","goatish","gorbellied","impertinent","infectious","jarring","loggerheaded","lumpish","mammering","mangled","mewling","paunchy","pribbling","puking","puny","qualling","rank","reeky","roguish","ruttish","saucy","spleeny","spongy","surly","tottering","unmuzzled","vain","venomed","villainous","warped","wayward","weedy","yeasty"]
        self.word2 = ["base-court","bat-fowling","beef-witted","beetle-headed","boil-brained","clapper-clawed","clay-brained","common-kissing","crook-pated","dismal-dreaming","dizzy-eyed","doghearted","dread-bolted","earth-vexing","elf-skinned","fat-kidneyed","fen-sucked","flap-mouthed","fly-bitten","folly-fallen","fool-born","full-gorged","guts-griping","half-faced","hasty-witted","hedge-born","hell-hated","idle-headed","ill-breeding","ill-nurtured","knotty-pated","milk-livered","motley-minded","onion-eyed","plume-plucked","pottle-deep","pox-marked","reeling-ripe","rough-hewn","rude-growing","rump-fed","shard-borne","sheep-biting","spur-galled","swag-bellied","tardy-gaited","tickle-brained","toad-spotted","unchin-snouted","weather-bitten"]
        self.word3 = ["apple-john","baggage","barnacle","bladder","boar-pig","bugbear","bum-bailey","canker-blosso","clack-dish","clotpole","coxcomb","codpiece","death-token","dewberry","flap-dragon","flax-wench","flirt-gill","foot-licker","fustilarian","giglet","gudgeon","haggard","harpy","hedge-pig","horn-beast","hugger-mugger","joithead","lewdster","lout","maggot-pie","malt-worm","mammet","measle","minnow","miscreant","moldwarp","mumble-news","nut-hook","pigeon-egg","pignut","puttock","pumpion","ratsbane","scut","skainsmate","strumpet","varlot","vassal","whey-face","wagtail"]

    @commands.command(pass_context=True)
    async def insult(self, ctx, name : str = None):
        """Insult a user in the Shakespearean manner"""
        member = ctx.message.server.get_member_named(name)
        if member is not None:
            await self.bot.say("{0}, you {1}!".format(member.mention, self.generate_insult()))
        else:
            await self.bot.say("That user could not be found, you {0}".format(self.generate_insult()))

    def generate_insult(self):
        w1 = random.choice(self.word1)
        w2 = random.choice(self.word2)
        w3 = random.choice(self.word3)
        return "{0} {1} {2}".format(w1, w2, w3)

def setup(bot):
    bot.add_cog(Insults(bot))
