from .image import Image


async def setup(bot):
    await bot.add_cog(Image(bot))
