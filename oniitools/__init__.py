from .oniitools import Oniitools


async def setup(bot):
    await bot.add_cog(Oniitools(bot))
