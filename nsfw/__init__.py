from .nsfw import Nsfw


async def setup(bot):
    await bot.add_cog(Nsfw(bot))
