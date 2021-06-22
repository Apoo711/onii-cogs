"""
Copyright 2021 Onii-chan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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
        
