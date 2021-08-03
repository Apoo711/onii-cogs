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
from redbot.core import Config, commands


async def api_call(call_uri, returnObj=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{call_uri}") as response:
            response = await response.json()
            if returnObj == False:
                return response["url"]
            elif returnObj == True:
                return response
    await session.close()

log = logging.getLogger("red.onii.image")


class Image(commands.Cog):
    """Get tons of memes or other images"""

    __author__ = ["Onii-chan"]
    __version__ = "3.3.0"

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    async def red_get_data_for_user(self, *, user_id: int):
        """
        This cog does not story any end user data.
        """
        return {}

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete.
        """
        return

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def naruto(self, ctx: commands.Context):
        """Shows some naruto wallpapers from reddit.

        Wallpapers shown are taken from r/narutowallpapers.
        """
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                        "https://api.martinebot.com/v1/images/subreddit?name=narutowallpapers"
                    ) as resp:
                origin = await resp.json()
                data = origin["data"]
                url = data["image_url"]
                subreddit = data["subreddit"] or ""
                sub_name = subreddit["name"] or "Unknown"
                sub_url = subreddit["url"] or ""
                author = data["author"] or ""
                r_author = author["name"] or "Unknown"
                r_author_url = author["url"] or ""
                title = data["title"] or ""
                created_at = data["created_at"] or ""
                downvotes = data["downvotes"] or ""
                comments = data["comments"] or ""
                ups = data["upvotes"] or ""
                link = data["post_url"] or ""

                if data["nsfw"] and not ctx.channel.is_nsfw():
                    return await ctx.send(
                        "Sorry the contents of this post are NSFW and this channel isn't set to allow NSFW content, please it on and try again later."
                    )
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
        try:
            await ctx.reply(
                embed=embed,
                mention_author=False,
            )
        except discord.HTTPException:
            await ctx.send("Something went wrong while posting an image.")

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def subr(self, ctx: commands.Context, reddit: str):
        """Shows some images form the specified subreddit.

        Warning: Some Images Could Be Considered Nsfw In Some Servers.
        """
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                        f"https://api.martinebot.com/v1/images/subreddit?name={reddit}"
                    ) as resp:
                origin = await resp.json()

                if not origin["success"]:
                    embed = discord.Embed(
                        title="That subreddit doesn't seem to exist...",
                        colour=discord.Colour.random(),
                        description=(
                            "**I did my best to find '{}', but my search yielded no results.**\n"
                            "**Please check for any mistakes in the name and try again.**"
                        ).format(
                            reddit
                            )
                    )
                    return await ctx.reply(embed=embed, mention_author=False)

                data = origin["data"]
                image_url = data["image_url"]
                subreddit = data["subreddit"] or ""
                sub_name = subreddit["name"] or "Unknown"
                sub_url = subreddit["url"] or ""
                author = data["author"] or ""
                r_author = author["name"] or "Unknown"
                r_author_url = author["url"] or ""
                title = data["title"] or ""
                created_at = data["created_at"] or ""
                downvotes = data["downvotes"] or ""
                comments = data["comments"] or ""
                ups = data["upvotes"] or ""
                link = data["post_url"] or ""

                if data["nsfw"] and not ctx.channel.is_nsfw():
                    return await ctx.send(
                        "Sorry the contents of this post are NSFW and this channel isn't set to allow NSFW content, please it on and try again later."
                    )

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
                embed.set_image(url=image_url)
                embed.set_footer(
                    text="👍  {} • 👎  {} • 💬  {} • martinebot.com API".format(
                        ups,
                        downvotes,
                        comments,
                    ),
                    icon_url=ctx.message.author.avatar_url,
                )

                return await ctx.reply(
                    embed=embed,
                    mention_author=False
                )

    @commands.command(name="randomwallpaper", aliases=["raw"])
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wallpaper_random(self, ctx: commands.Context):
        """Shows some anime wallpaper from reddit.

        Wallpapers shown are taken from random subreddits.

        Warning: Some Images Could Be Considered Nsfw In Some Servers.
        """
        await ctx.trigger_typing()
        SUBREDDITS = [
            "images/subreddits?name=Animewallpaper",
            "images/wallpaper"
        ]
        API = random.choice(SUBREDDITS)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                        f"https://api.martinebot.com/v1/{API}"
                    ) as resp:
                origin = await resp.json()
                data = origin["data"]
                url = data["image_url"]
                subreddit = data["subreddit"] or ""
                sub_name = subreddit["name"] or "Unknown"
                sub_url = subreddit["url"] or ""
                author = data["author"] or ""
                r_author = author["name"] or "Unknown"
                r_author_url = author["url"] or ""
                title = data["title"] or ""
                created_at = data["created_at"] or ""
                downvotes = data["downvotes"] or ""
                comments = data["comments"] or ""
                ups = data["upvotes"] or ""
                link = data["post_url"] or ""

                if data["nsfw"] and not ctx.channel.is_nsfw():
                    return await ctx.send(
                        "Sorry the contents of this post are NSFW and this channel isn't set to allow NSFW content, please it on and try again later."
                    )

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
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                        "https://api.martinebot.com/v1/images/subreddit?name=AnimePFP"
                    ) as resp:
                origin = await resp.json()
                data = origin["data"]
                url = data["image_url"]
                subreddit = data["subreddit"] or ""
                sub_name = subreddit["name"] or "Unknown"
                sub_url = subreddit["url"] or ""
                author = data["author"] or ""
                r_author = author["name"] or "Unknown"
                r_author_url = author["url"] or ""
                title = data["title"] or ""
                created_at = data["created_at"] or ""
                downvotes = data["downvotes"] or ""
                comments = data["comments"] or ""
                ups = data["upvotes"] or ""
                link = data["post_url"] or ""

                if data["nsfw"] and not ctx.channel.is_nsfw():
                    return await ctx.send(
                        "Sorry the contents of this post are NSFW and this channel isn't set to allow NSFW content, please it on and try again later."
                    )

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

        Memes shown are taken from the subreddit set by the admins.
        """
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                        "https://api.martinebot.com/v1/images/memes"
                    ) as resp:
                origin = await resp.json()
                data = origin["data"]
                url = data["image_url"]
                subreddit = data["subreddit"] or ""
                sub_name = subreddit["name"] or "Unknown"
                sub_url = subreddit["url"] or ""
                author = data["author"] or ""
                r_author = author["name"] or "Unknown"
                r_author_url = author["url"] or ""
                title = data["title"] or ""
                created_at = data["created_at"] or ""
                downvotes = data["downvotes"] or ""
                comments = data["comments"] or ""
                ups = data["upvotes"] or ""
                link = data["post_url"] or ""

                if data["nsfw"] and not ctx.channel.is_nsfw():
                    return await ctx.send(
                        "Sorry the contents of this post are NSFW and this channel isn't set to allow NSFW content."
                        " Please turn nsfw on and try again later."
                    )

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
        await ctx.trigger_typing()
        SUBREDDITS = [
            "spaceengine",
            "LandscapeAstro"
        ]
        API = random.choice(SUBREDDITS)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                        f"https://api.martinebot.com/v1/images/subreddit?name={API}"
                    ) as resp:
                origin = await resp.json()
                data = origin["data"]
                url = data["image_url"]
                subreddit = data["subreddit"] or ""
                sub_name = subreddit["name"] or "Unknown"
                sub_url = subreddit["url"] or ""
                author = data["author"] or ""
                r_author = author["name"] or "Unknown"
                r_author_url = author["url"] or ""
                title = data["title"] or ""
                created_at = data["created_at"] or ""
                downvotes = data["downvotes"] or ""
                comments = data["comments"] or ""
                ups = data["upvotes"] or ""
                link = data["post_url"] or ""

                if data["nsfw"] and not ctx.channel.is_nsfw():
                    return await ctx.send(
                        "Sorry the contents of this post are NSFW and this channel isn't set to allow NSFW content, please it on and try again later."
                    )

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
        await ctx.trigger_typing()
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
                origin = await resp.json()
                data = origin["data"]
                subreddit = data["subreddit"] or ""
                url = data["image_url"]
                sub_name = subreddit["name"] or "Unknown"
                sub_url = subreddit["url"] or ""
                author = data["author"] or ""
                r_author = author["name"] or "Unknown"
                r_author_url = author["url"] or ""
                title = data["title"] or ""
                created_at = data["created_at"] or ""
                downvotes = data["downvotes"] or ""
                comments = data["comments"] or ""
                ups = data["upvotes"] or ""
                link = data["post_url"] or ""

                if data["nsfw"] and not ctx.channel.is_nsfw():
                    return await ctx.send(
                        "Sorry the contents of this post are NSFW and this channel isn't set to allow NSFW content, please it on and try again later."
                    )

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

        try:
            await ctx.reply(
                embed=embed,
                mention_author=False,
            )
        except discord.HTTPException:
            await ctx.send("Something went wrong while posting an image.")

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def scenery(self, ctx: commands.Context):
        """Shows some scenery from reddit.

        Images shown are taken from r/EarthPorn.
        """
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                        "https://api.martinebot.com/v1/images/subreddit?name=EarthPorn"
                    ) as resp:
                origin = await resp.json()
                data = origin["data"]
                url = data["image_url"]
                subreddit = data["subreddit"] or ""
                sub_name = subreddit["name"] or "Unknown"
                sub_url = subreddit["url"] or ""
                author = data["author"] or ""
                r_author = author["name"] or "Unknown"
                r_author_url = author["url"] or ""
                title = data["title"] or ""
                created_at = data["created_at"] or ""
                downvotes = data["downvotes"] or ""
                comments = data["comments"] or ""
                ups = data["upvotes"] or ""
                link = data["post_url"] or ""

                if data["nsfw"] and not ctx.channel.is_nsfw():
                    return await ctx.send(
                        "Sorry the contents of this post are NSFW and this channel isn't set to allow NSFW content, please it on and try again later."
                    )

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
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                        "https://api.martinebot.com/v1/images/subreddit?name=UnixPorn"
                    ) as resp:
                origin = await resp.json()
                data = origin["data"]
                url = data["image_url"]
                subreddit = data["subreddit"] or ""
                sub_name = subreddit["name"] or "Unknown"
                sub_url = subreddit["url"] or ""
                author = data["author"] or ""
                r_author = author["name"] or "Unknown"
                r_author_url = author["url"] or ""
                title = data["title"] or ""
                created_at = data["created_at"] or ""
                downvotes = data["downvotes"] or ""
                comments = data["comments"] or ""
                ups = data["upvotes"] or ""
                link = data["post_url"] or ""

                if data["nsfw"] and not ctx.channel.is_nsfw():
                    return await ctx.send(
                        "Sorry the contents of this post are NSFW and this channel isn't set to allow NSFW content, please it on and try again later."
                    )

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

        await ctx.reply(
            embed=embed,
            mention_author=False,
        )

    @commands.command(aliases=["celeb"])
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def celebrity(self, ctx: commands.Context):
        """Shows some imagesof celebrities from reddit.

        Images shown are taken from:

        r/UltraHighResCelebs, r/HighResCelebs and r/UHQcelebs.
        """
        await ctx.trigger_typing()

        if not ctx.channel.is_nsfw():
            return await ctx.send("Sorry but this is nsfw")

        SUBREDDITS = [
            "UltraHighResCeleb",
            "HighResCelebs",
            "UHQcelebs",
        ]
        API = random.choice(SUBREDDITS)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.martinebot.com/v1/images/subreddit?name={API}"
            ) as resp:
                data = await resp.json()
                data = data["data"]
                url = data["image_url"]
                subreddit = data["subreddit"] or ""
                sub_name = subreddit["name"] or "Unknown"
                sub_url = subreddit["url"] or ""
                author = data["author"] or ""
                r_author = author["name"] or "Unknown"
                r_author_url = author["url"] or ""
                title = data["title"] or ""
                created_at = data["created_at"] or ""
                downvotes = data["downvotes"] or ""
                comments = data["comments"] or ""
                ups = data["upvotes"] or ""
                link = data["post_url"] or ""

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

        await ctx.reply(
            embed=embed,
            mention_author=False,
        )

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def test(self, ctx: commands.Context):
        """Shows some moe images from reddit.
        Images shown are taken from:
        r/awwnime, r/animeboys, r/cuteanimeboys and r/CuteAnimeGirls.
        """
        await ctx.trigger_typing()
        SUBREDDITS = [
            "animeboys",
            "CuteAnimeGirlss",
            "cuteanimeboys",
            "awwnime"
        ]
        API = random.choice(SUBREDDITS)
#        async with aiohttp.ClientSession() as session:
#            async with session.get(
#                        f"https://api.martinebot.com/v1/images/subreddit?name={API}"
#                    ) as resp:
#                origin = await resp.json()
#                data = origin["data"]
#                url = data["image_url"]
#                subreddit = data["subreddit"] or ""
#                sub_name = subreddit["name"] or "Unknown"
#                sub_url = subreddit["url"] or ""
#                author = data["author"] or ""
#                r_author = author["name"] or "Unknown"
#                r_author_url = author["url"] or ""
#                title = data["title"] or ""
#                created_at = data["created_at"] or ""
#                downvotes = data["downvotes"] or ""
#                comments = data["comments"] or ""
#                ups = data["upvotes"] or ""
#                link = data["post_url"] or ""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://www.reddit.com/{API}/new.json?sort=new"
            ) as resp:
                data = await resp.json()
                data1 = data["data"]
                children = data1["children"]
                post = random.choice(children)["data"]
                title = post["title"] or ""
                url = post["url_overridden_by_dest"] or ""
                link = f'https://reddit.com{post["permalink"]}' or ""
                ups = post["ups"] or ""
                comments = post["num_comments"] or ""
                subreddit = post["subreddit_name_prefixed"] or ""
                sub_name = post["subreddit"] or "Unknown"
                sub_url = f"https://reddit.com/{subreddit}/"
                author = post["author"] or ""
                r_author = post["author"] or "Unknown"
                r_author_url = f"https://reddit.com/u/{author}" or ""
                title = post["title"] or ""
                created_at = post["created_utc"] or ""
                downvotes = post["downs"] or ""

                if post["over_18"] is True and not ctx.channel.is_nsfw():
                    return await ctx.send(
                        "Sorry the contents of this post are NSFW and this channel isn't set to allow NSFW content, please it on and try again later."
                    )

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

        try:
            await ctx.reply(
                embed=embed,
                mention_author=False,
            )
        except discord.HTTPException:
            await ctx.send("Something went wrong while posting an image.")
