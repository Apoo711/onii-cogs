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

import random
import discord
import aiohttp

from redbot.core import commands
from io import BytesIO


class Oniitools(commands.Cog):
    """A random assortment of fun commands!"""

    def __init__(self, bot):
        self.bot = bot

    __author__ = ["Onii-chan"]
    __version__ = "1.0.0"

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    @commands.command()
    async def penis(self, ctx, user: discord.Member):
        """Detects user's penis length this is 100% accurate."""
        random.seed(user.id)
        p = "8" + "="*random.randint(0, 30) + "D"
        await ctx.reply("Size: " + p, mention_author=False)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def osu(ctx, self, player:str):
        """Osu stats for player"""
        async with aiohttp.ClientSession() as s:
            async with s.get(
                f"https://api.martinebot.com/v1/imagesgen/osuprofile?&player_username={player}"
            ) as resp:
                if resp.status in (200, 201):
                    f = discord.File(
                        fp=BytesIO(
                            await resp.read()
                        ), filename="osu.png"
                    )
                    emb = discord.Embed(
                        title=f"{player}'s Osu Stats",
                        colour=discord.Colour.random()
                    )
                    emb.set_image(url="attachment://osu.png")
                    emb.set_footer(text="Powered by martinebot.com API")
                    await ctx.send(file=f, embed=emb)
                    f.close()
                elif resp.status in (404, 410, 422):
                    await ctx.send((await resp.json())['message'])
                else:
                    await ctx.send("API is down currently, please try later")
