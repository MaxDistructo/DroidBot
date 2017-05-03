import discord
from discord.ext import commands

class Droidbot:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot
@commands.command()  
async def punch(self, user : discord.member):
    if user is discord.member:
        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

@commands.command()
async def stuff(self):
    await self.bot.say("I can do stuff!")

        
@commands.group(name = "info", pass_context = True)
async def info(self, ctx):
    
    @info.command(pass_context = True)
    async def owners(self):
        await self.bot.say("The Owners of this Discord are @MaxDistructo#3927, @Lufia, Over And Out#4839 , and @Toasty with a new home#1297")
    @info.command(pass_context = True)
    async def bot(self):
        await self.bot.say("This bot is a RedBot, writen with discord.py")
    @info.command(pass_context = True)
    async def server(self):
        await self.bot.say("The MC url is 192.168.0.1")
    @info.command(pass_context = True)
    async def fourm(self):
        await self.bot.say("http://lufiahang.comxa.com/001/forem/index.php The Website is currently down")
    @info.command(pass_context = True)
    async def download(self):
        await self.bot.say("The server download link is http://www.example.com")
    @info.command(pass_context = True)
    async def link(self):
        await self.bot.say("The Discord invite link is http://discord.gg/")
        
@commands.group(name = "rule", pass_context = True)
async def rule(self, ctx):
    
    @rule.command(pass_context = True)
    async def one(self):
        await self.bot.say("Rule 1: Don't Be A Dick!")
    @rule.command(pass_context = True)
    async def two(self):
        await self.bot.say("Rule 2: ")
    @rule.command(pass_context = True)
    async def three(self):
        await self.bot.say("Rule 3: ")
    @rule.command(pass_context = True)
    async def four(self):
        await self.bot.say("Rule 4: ")
    @rule.command(pass_context = True)
    async def five(self):
        await self.bot.say("Rule 5: ")
        

def setup(bot):
    bot.add_cog(Droidbot(bot))
