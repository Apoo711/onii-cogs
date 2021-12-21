import discord
from onii_images import memes as m
from redbot.core import commands


class Memes(commands.Cog):
    """Memes"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def drake(self, ctx, text: str):
        """Drake meme"""
        async with ctx.typing():
            if len(text.split(",")) < 2:
                return await ctx.send(
                    "You need to specify two pieces of text, split by a comma"
                )
            drake_text = text.split(",")
            await ctx.reply(
                file=discord.File(m.drake(drake_text[0], drake_text[1]))
            )

    @commands.command()
    async def disappointed(self, ctx, text: str):
        """Disappointed meme"""
        async with ctx.typing():
            if len(text.split(",")) < 2:
                return await ctx.send(
                    "You need to specify two pieces of text, split by a comma"
                )
            dis_text = text.split(",")
            await ctx.reply(
                file=discord.File(m.disappointed(dis_text[0], dis_text[1]))
            )

    @commands.command(name="flextape", aliases=["flex", "flext"])
    async def flex_tape(self, ctx, text: str):
        """Flex tape meme"""
        async with ctx.typing():
            if len(text.split(",")) < 2:
                return await ctx.send(
                    "You need to specify two pieces of text, split by a comma"
                )
            flextape_text = text.split(",")
            await ctx.reply(
                file=discord.File(
                    m.flex_tape(
                        flextape_text[0], flextape_text[1], ctx.author.name
                    )
                )
            )

    @commands.command()
    async def bernie(self, ctx, text: str):
        """Bernie meme"""
        async with ctx.typing():
            await ctx.reply(file=discord.File(m.bernie(text)))

    @commands.command()
    async def doge(self, ctx, text: str):
        """Doge meme"""
        async with ctx.typing():
            if len(text.split(",")) < 2:
                return await ctx.send(
                    "You need to specify two pieces of text, split by a comma"
                )
            doge_text = text.split(",")
            await ctx.reply(
                file=discord.File(m.doge(doge_text[0], doge_text[1]))
            )

    @commands.command()
    async def panik(self, ctx, panic: str, kalm: str, panik: str):
        """Panik... Kalm... PANIKK!!!"""
        async with ctx.typing():
            await ctx.reply(file=discord.File(m.panik(panic, kalm, panik)))

    @commands.command(name="myheart")
    async def my_heart(
        self, ctx, normal: str, slight_panic: str, ultra_panic: str
    ):
        """My heart meme"""
        async with ctx.typing():
            await ctx.reply(
                file=discord.File(
                    m.my_heart(normal, slight_panic, ultra_panic)
                )
            )


def setup(bot):
    bot.add_cog(Memes(bot))
