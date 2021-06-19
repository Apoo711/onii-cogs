import aiohttp
import discord
import logging

from redbot.core import commands

async def api_call(call_uri, returnObj=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{call_uri}") as response:
            response = await response.json()
            if returnObj == False:
                return response["url"]
            elif returnObj == True:
                return response

log = logging.getLogger("red.onii.perform")
            
class Perform(commands.Cog):
    """Perform different actions, like cuddle, poke etc."""

    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(5, 7, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def cuddle(self, ctx, user: discord.User):
        embed = discord.Embed(
            description=f"**{ctx.author.mention}** cuddled {f'**{str(user.mention)}**' if user else 'themselves'}!",
            color=discord.Colour.random(),
        )

        embed.set_footer(
            text=f"Requested by {ctx.message.author.display_name} | Powered by nekos.life",
            icon_url=ctx.message.author.avatar_url,
        )
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url)

        embed.set_image(url=await api_call("https://nekos.life/api/v2/img/cuddle"))
        await ctx.reply(embed=embed)

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
                    text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)

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
                    text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)

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
                    text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)

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
                    text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)

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
                    text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)

    @commands.command(name="smug")
    @commands.bot_has_permissions(embed_links=True)
    async def smug(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://shiro.gg/api/images/smug") as r:
                res = await r.json()
                em = discord.Embed(
                    colour=discord.Colour.random(),
                    description=f"**{ctx.author.mention}** is acting all smug!",
                )
                em.set_footer(
                    text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg",
                    icon_url=ctx.author.avatar_url,
                )
                em.set_image(url=res["url"])
                await ctx.reply(embed=em, mention_author=False)
