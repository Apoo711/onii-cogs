import discord
import random 

from redbot.core import commands

class Oniitools(commands.Cog):
    """A random assortment of fun commands!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def penis(self, ctx, user : discord.Member):
        """Detects user's penis length this is 100% accurate."""
        random.seed(user.id)
        p = "8" + "="*random.randint(0, 30) + "D"
        await ctx.reply("Size: " + p, mention_author=False)
        
