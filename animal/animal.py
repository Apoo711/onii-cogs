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

import logging

import aiohttp
import discord
from redbot.core import commands

log = logging.getLogger("red.onii.animal")


class Animal(commands.Cog):
    """Get images of animals!"""
    def __init__(self, bot):
        self.bot = bot

    __author__ = ["Onii-chan"]
    __version__ = "1.2.1"

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    @commands.group()
    @commands.guild_only()
    async def fact(self, ctx: commands.Context):
        """Get some random facts"""

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx: commands.Context):
        """Shows some dog pictures from reddit.

        Pictures shown are taken from r/dogpictures.
        """
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.martinebot.com/v1/images/subreddit?name=dogpictures"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                title = data["title"]
                url = data["image_url"]
                link = data["post_url"]
                ups = data["upvotes"]
                comments = data["comments"]
                downvotes = data["downvotes"]
                created_at = data["created_at"]

                if data["subreddit"]:
                    subreddit = data["subreddit"]
                    sub_name = subreddit["name"]
                    sub_url = subreddit["url"]

                else:
                    subreddit = ""
                    sub_name = "Unknown"
                    sub_url = ""

                if data["author"]:
                    author = data["author"]
                    r_author = author["name"]
                    r_author_url = author["url"]

                else:
                    author = ""
                    r_author = "Unknown"
                    r_author_url = ""

        embed = discord.Embed(
            title="Here's a random image...:frame_photo:",
            colour=discord.Colour.random(),
            description=(
                "**Post by:** [u/{}]({})\n"
                "**From:** [r/{}]({})\n"
                "**This post was created on:** <t:{}:F>\n"
                "**Title:** [{}]({})"
            ).format(
                r_author,
                r_author_url,
                sub_name,
                sub_url,
                created_at,
                title,
                link,
            ),
        )
        embed.set_image(url=url)
        embed.set_footer(
            text="👍  {} • 👎  {} • 💬  {} • martinebot.com API".format(
                ups,
                downvotes,
                comments,
            ),
            icon_url=ctx.message.author.avatar_url,
        )
        await session.close()
        await ctx.trigger_typing()
        await ctx.reply(
            embed=embed,
            mention_author=False,
        )

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cat(self, ctx: commands.Context):
        """Shows some cat wallpaper from reddit.

        Wallpapers shown are taken from r/catwallpapers.
        """
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.martinebot.com/v1/images/subreddit?name=catwallpapers"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                title = data["title"]
                url = data["image_url"]
                link = data["post_url"]
                ups = data["upvotes"]
                comments = data["comments"]
                downvotes = data["downvotes"]
                created_at = data["created_at"]

                if data["subreddit"]:
                    subreddit = data["subreddit"]
                    sub_name = subreddit["name"]
                    sub_url = subreddit["url"]

                else:
                    subreddit = ""
                    sub_name = "Unknown"
                    sub_url = ""

                if data["author"]:
                    author = data["author"]
                    r_author = author["name"]
                    r_author_url = author["url"]

                else:
                    author = ""
                    r_author = "Unknown"
                    r_author_url = ""

        embed = discord.Embed(
            title="Here's a random image...:frame_photo:",
            colour=discord.Colour.random(),
            description=(
                "**Post by:** [u/{}]({})\n"
                "**From:** [r/{}]({})\n"
                "**This post was created on:** <t:{}:F>\n"
                "**Title:** [{}]({})"
            ).format(
                r_author,
                r_author_url,
                sub_name,
                sub_url,
                created_at,
                title,
                link,
            ),
        )
        embed.set_image(url=url)
        embed.set_footer(
            text="👍  {} • 👎  {} • 💬  {} • martinebot.com API".format(
                ups,
                downvotes,
                comments,
            ),
            icon_url=ctx.message.author.avatar_url,
        )
        await session.close()
        await ctx.reply(
            embed=embed,
            mention_author=False,
        )

    @fact.command(name="dog")
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def f_dog(self, ctx):
        """Get a random dog fact"""
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://some-random-api.ml/facts/dog"
                ) as request:
                response = await request.json()
                fact = response["fact"]

                embed = discord.Embed(color=(await ctx.embed_colour()))
                embed.set_image(
                    url="https://media.tenor.com/images/d7afbeb5c3b3efc48a86eb2c3450ceb8/tenor.gif"
                )
                embed.add_field(
                    name="Here's a random dog fact!", value=fact
                )
                await ctx.send(embed=embed)
