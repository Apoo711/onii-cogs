from .perform import Perform


async def setup(bot):
    global hug

    hug = bot.remove_command("hug")
    await bot.add_cog(Perform(bot))
