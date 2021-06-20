from .oniitools import Oniitools


def setup(bot):
    bot.add_cog(Oniitools(bot))