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

import asyncio
import logging
import random

import aiohttp
import discord
from redbot.core import commands

log = logging.getLogger("red.onii.animal")

class Animal(commands.Cog):
    
    __author__ = ["Onii-chan"]
    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"
        
# Facts Group will be added when I add a command for this group

#    @commands.group(aliases=["i"])
#    async def facts(self, ctx):
#        """All the commands in the image cog"""

    @commands.group(aliases=["c"])
    async def image(self, ctx):
    
    @image.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx: commands.Context):
        """Shows some dog images from reddit.

        Images shown are taken from r/dogpictures.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://www.reddit.com/r/dogpictures/new.json?sort=hot"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                children = data["children"]
                post = random.choice(children)["data"]
                title = post["title"]
                url = post["url_overridden_by_dest"]

        embed = discord.Embed(title=title, colour=discord.Colour.random())
        embed.set_image(url=url)
        embed.set_footer(
            text="Powered by r/dogpictures",
            icon_url=ctx.message.author.avatar_url,
        )
        await session.close()
        await ctx.reply(embed=embed, mention_author=False)

    @image.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cat(self, ctx: commands.Context):
        """Shows some cat images from reddit.

        Images shown are taken from r/catwallpapers.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://www.reddit.com/r/catwallpapers/new.json?sort=hot"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                children = data["children"]
                post = random.choice(children)["data"]
                title = post["title"]
                url = post["url_overridden_by_dest"]

        embed = discord.Embed(title=title, colour=discord.Colour.random())
        embed.set_image(url=url)
        embed.set_footer(
            text="Powered by r/catwallpapers",
            icon_url=ctx.message.author.avatar_url,
        )
        await session.close()
        await ctx.reply(embed=embed, mention_author=False)
