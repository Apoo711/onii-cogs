from .memes import Memes


async def setup(bot):
    await bot.add_cog(Memes(bot))
