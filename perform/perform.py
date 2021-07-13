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


async def api_call(call_uri, returnObj=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{call_uri}") as response:
            response = await response.json()
            if returnObj == False:
                return response["url"]
            elif returnObj == True:
                return response
    await session.close()

log = logging.getLogger("red.onii.perform")


class Perform(commands.Cog):
    """Perform different actions, like cuddle, poke etc."""

    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def cuddle(self, ctx, user: discord.User):
        embed = discord.Embed(
            description=f"**{ctx.author.mention}** cuddled {f'**{str(user.mention)}**' if user else 'themselves'}!",
            color=discord.Colour.random(),
        )

        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar_url,
        )
        embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )

        embed.set_image(
            url=await api_call(
                "https://nekos.life/api/v2/img/cuddle"
            )
        )
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="poke")
    @commands.bot_has_permissions(embed_links=True)
    async def poke(self, ctx, user: discord.User):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://shiro.gg/api/images/poke") as r:
                res = await r.json()
                em = discord.Embed(
                    colour=discord.Colour.random(),
                    description=f"**{ctx.author.mention}** poked {f'**{str(user.mention)}**' if user else 'themselves'}!",
                )
                em.set_footer(
                    text=f"Requested by: {str(ctx.author)}",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="kiss")
    @commands.bot_has_permissions(embed_links=True)
    async def kiss(self, ctx, user: discord.User):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://shiro.gg/api/images/kiss") as r:
                res = await r.json()
                em = discord.Embed(
                    colour=discord.Colour.random(),
                    description=f"**{ctx.author.mention}** just kissed {f'**{str(user.mention)}**' if user else 'themselves'}!",
                )
                em.set_footer(
                    text=f"Requested by: {str(ctx.author)}",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="hug")
    @commands.bot_has_permissions(embed_links=True)
    async def hug(self, ctx, user: discord.User):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://shiro.gg/api/images/hug") as r:
                res = await r.json()
                em = discord.Embed(
                    colour=discord.Colour.random(),
                    description=f"**{ctx.author.mention}** just hugged {f'**{str(user.mention)}**' if user else 'themselves'}!",
                )
                em.set_footer(
                    text=f"Requested by: {str(ctx.author)}",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="pat")
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx, user: discord.User):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://shiro.gg/api/images/pat") as r:
                res = await r.json()
                em = discord.Embed(
                    colour=discord.Colour.random(),
                    description=f"**{ctx.author.mention}** just patted {f'**{str(user.mention)}**' if user else 'themselves'}!",
                )
                em.set_footer(
                    text=f"Requested by: {str(ctx.author)}",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="tickle")
    @commands.bot_has_permissions(embed_links=True)
    async def tickle(self, ctx, user: discord.User):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://shiro.gg/api/images/tickle") as r:
                res = await r.json()
                em = discord.Embed(
                    colour=discord.Colour.random(),
                    description=f"**{ctx.author.mention}** just tickled {f'**{str(user.mention)}**' if user else 'themselves'}!",
                )
                em.set_footer(
                    text=f"Requested by: {str(ctx.author)}",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="smug")
    @commands.bot_has_permissions(embed_links=True)
    async def smug(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://shiro.gg/api/images/smug") as r:
                res = await r.json()
                em = discord.Embed(
                    colour=discord.Colour.random(),
                    description=f"**{ctx.author.mention}** is acting so smug!",
                )
                em.set_footer(
                    text=f"Requested by: {str(ctx.author)}",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)
