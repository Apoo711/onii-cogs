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
from typing import List

import aiohttp
import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import box


async def api_call(call_uri, returnObj=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{call_uri}") as response:
            response = await response.json()
            if returnObj is False:
                return response["url"]
            elif returnObj is True:
                return response
    await session.close()


log = logging.getLogger("red.onii.nsfw")


class Nsfw(commands.Cog):
    """
    Nsfw commands, proceed with caution.
    """

    __author__ = ["Onii-chan"]
    __version__ = "2.1.0"

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    async def _version_msg(self, ctx: commands.Context, version: str, authors: List[str]):
        """Cog version message."""
        msg = box(
            ("Nsfw cog version: {version}\nAuthors: {authors}").format(
                version=version, authors=", ".join(authors)
            ),
            lang="py",
        )
        return await ctx.send(msg)

    @commands.command()
    async def nsfwversion(self, ctx):
        """Get the version of the installed Nsfw cog."""

        await self._version_msg(ctx, self.__version__, self.__author__)

    @commands.group()
    @commands.is_nsfw()
    async def hentai(self, ctx):
        """Hentai Commands"""

    @commands.group()
    @commands.is_nsfw()
    async def real(self, ctx):
        """Real Porn"""

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def erok(self, ctx):
        """Eroctic!"""
        embed = discord.Embed(
            title="Erok Kitsune !!!",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/erok"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def eroneko(self, ctx):
        """Eroctic nekos? what could be better?"""
        embed = discord.Embed(
            title="***ERO*** NEKO!",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/erokemo"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command(name="feet", aliases=["feetgif", "foot"])
    @commands.is_nsfw()
    async def feet(self, ctx):
        """Tasty feet"""
        embed = discord.Embed(
            title="***Feet***",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/feetg"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def cum(self, ctx):
        """Beautiful white cum"""
        embed = discord.Embed(
            title="***Sticky white stuff!***",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/cum"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command(name="nekofuck", aliases=["nekosex", "nekogif"])
    @commands.is_nsfw()
    async def nekofuck(self, ctx):
        """Fuck nekos!"""
        embed = discord.Embed(
            title="Catgirls!!!!",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/nsfw_neko_gif"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command(name="futanari")
    @commands.is_nsfw()
    async def futanari(self, ctx):
        """Futanari stuff."""
        embed = discord.Embed(
            title="",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/futanari"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command(name="boobs", aliases=["boob"])
    @commands.is_nsfw()
    async def _boobs(self, ctx):
        """Juicy tits"""
        embed = discord.Embed(
            title="**Titties**!!!!!",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/boobs"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command(name="blowjob")
    @commands.is_nsfw()
    async def blowjob(self, ctx):
        """Blowjobs"""
        embed = discord.Embed(
            title="Oh shit!",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/blowjob"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command(name="pussy")
    @commands.is_nsfw()
    async def _pussy(self, ctx):
        """Tight pussies"""
        embed = discord.Embed(
            title="Dang!",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/pussy"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def spank(self, ctx, user: commands.Greedy[discord.Member] = None):
        """Spank somebody"""
        if user is None:
            await ctx.message.reply("Please mention somebody to spank nex time.")
            return
        spanked_users = "".join(f"{users.mention} " for users in user)
        embed = discord.Embed(
            title="Oooof!",
            description="{} got spanked by {}".format(
                spanked_users,
                ctx.author.mention,
            ),
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/spank"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def lesbian(self, ctx):
        """Lesbian Hentai"""
        embed = discord.Embed(color=ctx.message.author.color)
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/les"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def trap(self, ctx):
        """Trapped"""
        embed = discord.Embed(color=ctx.message.author.color)
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/trap"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def hololewd(self, ctx):
        """hololewd stuff"""
        embed = discord.Embed(color=ctx.message.author.color)
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/hololewd"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def foxgirl(self, ctx):
        """Foxgirls!"""
        embed = discord.Embed(
            title="Foxy",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/fox_girl"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command(name="lewdkitsune", aliases=["lewdk"])
    @commands.is_nsfw()
    async def lewdkitsune(self, ctx):
        """Lewdkitsune hentai!"""
        embed = discord.Embed(
            title="Lewddd",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/lewdk"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def kuni(self, ctx):
        """Kuni Hentai!"""
        embed = discord.Embed(
            title="",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/kuni"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def femdom(self, ctx):
        """femdom hentai"""
        embed = discord.Embed(
            title="",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/femdom"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def erofeet(self, ctx):
        """Erofeet 3"""
        embed = discord.Embed(
            title="",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/erofeet"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def solo(self, ctx):
        """Solo Porn"""
        embed = discord.Embed(
            title="",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/solog"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command(name="gasm", aliases=["orgasm", "orgy"])
    @commands.is_nsfw()
    async def gasm(self, ctx):
        """Gasm Porn"""
        embed = discord.Embed(
            title="",
            color=ctx.message.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name}",
            icon_url=ctx.message.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/gasm"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    async def yuri(self, ctx):
        """Yuri Porn"""
        embed = discord.Embed(
            title="",
            color=ctx.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/yuri"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command(name="anal")
    @commands.is_nsfw()
    async def _anal(self, ctx):
        """Anal Hentai"""
        embed = discord.Embed(
            title="",
            color=ctx.author.color,
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/anal"))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(3, 7, commands.BucketType.user)
    @hentai.command(name="ass", aliases=["hentaiass", "hass"])
    @commands.is_nsfw()
    async def _ass(self, ctx):
        """Ass Hentai"""
        response = await api_call("https://nekobot.xyz/api/image?type=hass", True)
        embed = discord.Embed(
            title="Big ass",
            color=response["color"],
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=response["message"])
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(3, 7, commands.BucketType.user)
    @real.command(name="porn", aliases=["pgif"])
    @commands.is_nsfw()
    async def porn(self, ctx):
        """Just Porn"""
        response = await api_call("https://nekobot.xyz/api/image?type=pgif", True)
        embed = discord.Embed(
            title="Real porn",
            color=response["color"],
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=response["message"])
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(3, 7, commands.BucketType.user)
    @real.command(name="4k")
    @commands.is_nsfw()
    async def fourk(self, ctx):
        """Real 4K"""
        response = await api_call("https://nekobot.xyz/api/image?type=4k", True)
        embed = discord.Embed(
            title="The best quality",
            color=response["color"],
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=response["message"])
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(3, 7, commands.BucketType.user)
    @hentai.command(name="yaoi")
    @commands.is_nsfw()
    async def yaoi(self, ctx):
        """yaoi hentai"""
        response = await api_call("https://nekobot.xyz/api/image?type=yaoi", True)
        embed = discord.Embed(
            title="Yaoi",
            color=response["color"],
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=response["message"])
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(3, 7, commands.BucketType.user)
    @real.command(name="thigh", aliases=["thighs"])
    @commands.is_nsfw()
    async def thigh(self, ctx):
        """Real Thigh"""
        response = await api_call("https://nekobot.xyz/api/image?type=thigh", True)
        embed = discord.Embed(
            title="Them thic thighs",
            color=response["color"],
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=response["message"])
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(3, 7, commands.BucketType.user)
    @real.command()
    @commands.is_nsfw()
    async def pussy(self, ctx):
        """Real pussy"""
        response = await api_call("https://nekobot.xyz/api/image?type=pussy", True)
        embed = discord.Embed(
            title="Real pussy",
            color=response["color"],
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=response["message"])
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(3, 7, commands.BucketType.user)
    @real.command()
    @commands.is_nsfw()
    async def ass(self, ctx):
        """Real ass"""
        response = await api_call("https://nekobot.xyz/api/image?type=ass", True)
        embed = discord.Embed(
            title="Real ass",
            color=response["color"],
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=response["message"])
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(3, 7, commands.BucketType.user)
    @real.command()
    @commands.is_nsfw()
    async def anal(self, ctx):
        """Real anal"""
        response = await api_call("https://nekobot.xyz/api/image?type=anal", True)
        embed = discord.Embed(
            title="Real anal",
            color=response["color"],
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=response["message"])
        await ctx.reply(embed=embed, mention_author=False)

    @commands.cooldown(3, 7, commands.BucketType.user)
    @real.command(aliases=["tits"])
    @commands.is_nsfw()
    async def boobs(self, ctx):
        """Just Porn"""
        response = await api_call("https://nekobot.xyz/api/image?type=boobs", True)
        embed = discord.Embed(
            title="Real boobs",
            color=response["color"],
        )
        embed.set_footer(
            text=f"Requested by {ctx.author.display_name}",
            icon_url=ctx.author.avatar.url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url)
        embed.set_image(url=response["message"])
        await ctx.reply(embed=embed, mention_author=False)
