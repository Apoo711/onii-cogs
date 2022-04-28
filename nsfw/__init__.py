from .nsfw import Nsfw


def setup(bot):
    bot.add_cog(Nsfw(bot))
