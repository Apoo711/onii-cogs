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


async def api_call(call_uri, returnObj=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{call_uri}") as response:
            response = await response.json()
            if returnObj == False:
                return response["url"]
            elif returnObj == True:
                return response

log = logging.getLogger("red.onii.image")


class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def naruto(self, ctx: commands.Context):
        """Shows some naruto wallpapers from reddit.

        Wallpapers shown are taken from r/narutowallpapers.
        """
        async with ctx.typing():
            await asyncio.sleep(1)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.martinebot.com/v1/images/subreddit?name=narutowallpapers"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                author = data["author"]
                subreddit = data["subreddit"]
                sub_name = subreddit["name"]
                sub_url = subreddit["url"]
                title = data["title"]
                url = data["image_url"]
                link = data["post_url"]
                ups = data["upvotes"]
                comments = data["comments"]
                r_author = author["name"]
                r_author_url = author["url"]
                downvotes = data["downvotes"]
                created_at = data["created_at"]

        embed = discord.Embed(
            title="Here's a random image...",
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
            text="👍 {} • 👎 {} • 💬 {} • martinebot.com API".format(
                ups,
                downvotes,
                comments,
            ),
            icon_url=ctx.message.author.avatar_url,
        )
        await ctx.trigger_typing()
        await ctx.reply(
            embed=embed,
            mention_author=False,
        )

    @commands.command(name="randomwallpaper", aliases=["ran"])
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wallpaper_random(self, ctx: commands.Context):
        """Shows some anime wallpaper from reddit.

        Wallpapers shown are taken from r/Animewallpaper.

        Warning: Some Images Could Be Considered Nsfw In Some Servers.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.martinebot.com/v1/images/subreddit?name=Animewallpaper"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                author = data["author"]
                subreddit = data["subreddit"]
                sub_name = subreddit["name"]
                sub_url = subreddit["url"]
                title = data["title"]
                url = data["image_url"]
                link = data["post_url"]
                ups = data["upvotes"]
                comments = data["comments"]
                r_author = author["name"]
                r_author_url = author["url"]
                downvotes = data["downvotes"]
                created_at = data["created_at"]

        embed = discord.Embed(
            title=title,
            colour=discord.Colour.random(),
            description=(
                "**Post by:** [u/{}]({})\n"
                "**From:** [r/{}]({})\n"
                "**This post was created on:** <t:{}:F>"
            ).format(
                r_author,
                r_author_url,
                sub_name,
                sub_url,
                created_at,
            ),
            url=link,
        )
        embed.set_image(url=url)
        embed.set_footer(
            text="👍 {} • 👎 {} • 💬 {} • martinebot.com API".format(
                ups,
                downvotes,
                comments,
            ),
            icon_url=ctx.message.author.avatar_url,
        )
        await ctx.trigger_typing()
        await ctx.reply(
            embed=embed,
            mention_author=False,
        )

    @commands.command(name="randomavatar", aliases=["rav"])
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar_random(self, ctx: commands.Context):
        """Shows some anime profile pictures from reddit.

        Pictures shown are taken from r/AnimePFP.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.martinebot.com/v1/images/subreddit?name=AnimePFP"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                author = data["author"]
                subreddit = data["subreddit"]
                sub_name = subreddit["name"]
                sub_url = subreddit["url"]
                title = data["title"]
                url = data["image_url"]
                link = data["post_url"]
                ups = data["upvotes"]
                comments = data["comments"]
                r_author = author["name"]
                r_author_url = author["url"]
                downvotes = data["downvotes"]
                created_at = data["created_at"]

        embed = discord.Embed(
            title=title,
            colour=discord.Colour.random(),
            description=(
                "**Post by:** [u/{}]({})\n"
                "**From:** [r/{}]({})\n"
                "**This post was created on:** <t:{}:F>"
            ).format(
                r_author,
                r_author_url,
                sub_name,
                sub_url,
                created_at,
            ),
            url=link,
        )
        embed.set_image(url=url)
        embed.set_footer(
            text="👍 {} • 👎 {} • 💬 {} • martinebot.com API".format(
                ups,
                downvotes,
                comments,
            ),
            icon_url=ctx.message.author.avatar_url,
        )
        await ctx.trigger_typing()
        await ctx.reply(
            embed=embed,
            mention_author=False,
        )

    @commands.command()
    @commands.guild_only()
    async def neko(self, ctx):
        embed = discord.Embed(
            title="Neko's For You!",
            color=discord.Colour.random(),
            timestamp=ctx.message.created_at,
        )

        embed.set_footer(
            text="Powered by nekos.best",
            icon_url=ctx.message.author.avatar_url,
        )
        embed.set_author(name=self.bot.user.display_name,
                         icon_url=self.bot.user.avatar_url)

        embed.set_image(url=await api_call("https://nekos.best/nekos"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=["memes"])
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx: commands.Context):
        """Shows some memes from reddit.

        Memes shown are taken from r/memes, r/Animemes, r/dankmemes.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.martinebot.com/v1/images/memes"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                author = data["author"]
                subreddit = data["subreddit"]
                sub_name = subreddit["name"]
                sub_url = subreddit["url"]
                title = data["title"]
                url = data["image_url"]
                link = data["post_url"]
                ups = data["upvotes"]
                comments = data["comments"]
                r_author = author["name"]
                r_author_url = author["url"]
                downvotes = data["downvotes"]
                created_at = data["created_at"]

        embed = discord.Embed(
            title=title,
            colour=discord.Colour.random(),
            description=(
                "**Post by:** [u/{}]({})\n"
                "**From:** [r/{}]({})\n"
                "**This post was created on:** <t:{}:F>"
            ).format(
                r_author,
                r_author_url,
                sub_name,
                sub_url,
                created_at,
            ),
            url=link,
        )
        embed.set_image(url=url)
        embed.set_footer(
            text="👍 {} • 👎 {} • 💬 {} • martinebot.com API".format(
                ups,
                downvotes,
                comments,
            ),
            icon_url=ctx.message.author.avatar_url,
        )
        await ctx.trigger_typing()
        await ctx.reply(
            embed=embed,
            mention_author=False,
        )

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def space(self, ctx: commands.Context):
        """Shows some space images from reddit.

        Images shown are taken from r/spaceengine and r/LandscapeAstro.
        """
        SUBREDDITS = [
            "spaceengine",
            "LandscapeAstro"
        ]
        API = random.choice(SUBREDDITS)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.martinebot.com/v1/images/subreddit?name={API}"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                author = data["author"]
                subreddit = data["subreddit"]
                sub_name = subreddit["name"]
                sub_url = subreddit["url"]
                title = data["title"]
                url = data["image_url"]
                link = data["post_url"]
                ups = data["upvotes"]
                comments = data["comments"]
                r_author = author["name"]
                r_author_url = author["url"]
                downvotes = data["downvotes"]
                created_at = data["created_at"]

        embed = discord.Embed(
            title=title,
            colour=discord.Colour.random(),
            description=(
                "**Post by:** [u/{}]({})\n"
                "**From:** [r/{}]({})\n"
                "**This post was created on:** <t:{}:F>"
            ).format(
                r_author,
                r_author_url,
                sub_name,
                sub_url,
                created_at,
            ),
            url=link,
        )
        embed.set_image(url=url)
        embed.set_footer(
            text="👍 {} • 👎 {} • 💬 {} • martinebot.com API".format(
                ups,
                downvotes,
                comments,
            ),
            icon_url=ctx.message.author.avatar_url,
        )
        await ctx.trigger_typing()
        await ctx.reply(
            embed=embed,
            mention_author=False,
        )

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def moe(self, ctx: commands.Context):
        """Shows some moe images from reddit.

        Images shown are taken from:

        r/awwnime, r/animeboys, r/cuteanimeboys and r/CuteAnimeGirls.
        """
        SUBREDDITS = [
            "animeboys",
            "CuteAnimeGirlss",
            "cuteanimeboys",
            "awwnime"
        ]
        API = random.choice(SUBREDDITS)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.martinebot.com/v1/images/subreddit?name={API}"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                author = data["author"]
                subreddit = data["subreddit"]
                sub_name = subreddit["name"]
                sub_url = subreddit["url"]
                title = data["title"]
                url = data["image_url"]
                link = data["post_url"]
                ups = data["upvotes"]
                comments = data["comments"]
                r_author = author["name"]
                r_author_url = author["url"]
                downvotes = data["downvotes"]
                created_at = data["created_at"]

        embed = discord.Embed(
            title=title,
            colour=discord.Colour.random(),
            description=(
                "**Post by:** [u/{}]({})\n"
                "**From:** [r/{}]({})\n"
                "**This post was created on:** <t:{}:F>"
            ).format(
                r_author,
                r_author_url,
                sub_name,
                sub_url,
                created_at,
            ),
            url=link,
        )
        embed.set_image(url=url)
        embed.set_footer(
            text="👍 {} • 👎 {} • 💬 {} • martinebot.com API".format(
                ups,
                downvotes,
                comments,
            ),
            icon_url=ctx.message.author.avatar_url,
        )
        await ctx.trigger_typing()
        await ctx.reply(
            embed=embed,
            mention_author=False,
        )

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def scenery(self, ctx: commands.Context):
        """Shows some scenery from reddit.

        Images shown are taken from r/EarthPorn.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.martinebot.com/v1/images/subreddit?name=EarthPorn"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                author = data["author"]
                subreddit = data["subreddit"]
                sub_name = subreddit["name"]
                sub_url = subreddit["url"]
                title = data["title"]
                url = data["image_url"]
                link = data["post_url"]
                ups = data["upvotes"]
                comments = data["comments"]
                r_author = author["name"]
                r_author_url = author["url"]
                downvotes = data["downvotes"]
                created_at = data["created_at"]

        embed = discord.Embed(
            title=title,
            colour=discord.Colour.random(),
            description=(
                "**Post by:** [u/{}]({})\n"
                "**From:** [r/{}]({})\n"
                "**This post was created on:** <t:{}:F>"
            ).format(
                r_author,
                r_author_url,
                sub_name,
                sub_url,
                created_at,
            ),
            url=link,
        )
        embed.set_image(url=url)
        embed.set_footer(
            text="👍 {} • 👎 {} • 💬 {} • martinebot.com API".format(
                ups,
                downvotes,
                comments,
            ),
            icon_url=ctx.message.author.avatar_url,
        )
        await ctx.trigger_typing()
        await ctx.reply(
            embed=embed,
            mention_author=False,
        )

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unix(self, ctx: commands.Context):
        """Shows some unix images from reddit.

        Images shown are taken from r/UnixPorn.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.martinebot.com/v1/images/subreddit?name=UnixPorn"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                author = data["author"]
                subreddit = data["subreddit"]
                sub_name = subreddit["name"]
                sub_url = subreddit["url"]
                title = data["title"]
                url = data["image_url"]
                link = data["post_url"]
                ups = data["upvotes"]
                comments = data["comments"]
                r_author = author["name"]
                r_author_url = author["url"]
                downvotes = data["downvotes"]
                created_at = data["created_at"]

        embed = discord.Embed(
            title=title,
            colour=discord.Colour.random(),
            description=(
                "**Post by:** [u/{}]({})\n"
                "**From:** [r/{}]({})\n"
                "**This post was created on:** <t:{}:F>"
            ).format(
                r_author,
                r_author_url,
                sub_name,
                sub_url,
                created_at,
            ),
            url=link,
        )
        embed.set_image(url=url)
        embed.set_footer(
            text="👍 {} • 👎 {} • 💬 {} • martinebot.com API".format(
                ups,
                downvotes,
                comments,
            ),
            icon_url=ctx.message.author.avatar_url,
        )
        await ctx.trigger_typing()
        await ctx.reply(
            embed=embed,
            mention_author=False,
        )
