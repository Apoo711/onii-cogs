from .game import Games


async def setup(bot):
    await bot.add_cog(Games(bot))
