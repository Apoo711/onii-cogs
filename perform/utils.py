import aiohttp
import discord


async def api_call(call_uri, returnObj=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{call_uri}") as response:
            response = await response.json()
            if returnObj is False:
                return response["url"]
            elif returnObj is True:
                return response
    await session.close()


async def api_call2(call_uri, returnObj=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{call_uri}") as response:
            response = await response.json()
            if returnObj is False:
                return response["response"]
            elif returnObj is True:
                return response
    await session.close()


async def nekosembed(self, ctx, user, action: str, endpoint: str):
    embed = discord.Embed(
        description=f"**{ctx.author.mention}** {action} {f'**{str(user.mention)}**' if user else 'themselves'}!",
        color=discord.Colour.random(),
    )
    embed.set_footer(
        text=f"Requested by {ctx.message.author.display_name}",
        icon_url=ctx.message.author.avatar_url,
    )
    embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url)
    embed.set_image(url=await api_call("https://nekos.life/api/v2/img/" + endpoint))
    await ctx.reply(embed=embed, mention_author=False)


async def shiroembed(self, ctx, action: str, endpoint: str, user=None):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://shiro.gg/api/images/" + endpoint) as r:
            res = await r.json()
            if user is None:
                em = discord.Embed(
                    colour=discord.Colour.random(),
                    description=f"**{ctx.author.mention}** " + action,
                )
            else:
                em = discord.Embed(
                    colour=discord.Colour.random(),
                    description=f"**{ctx.author.mention}** {action} {f'**{str(user.mention)}**' if user else 'themselves'}!",
                )
            em.set_footer(
                text=f"Requested by: {str(ctx.author)}",
                icon_url=ctx.author.avatar_url,
            )
            em.set_image(url=res["url"])
            await ctx.reply(embed=em, mention_author=False)


async def kawaiiembed(self, ctx, action: str, endpoint: str, user=None):
    api_key = (await self.bot.get_shared_api_tokens("perform")).get("api_key")
    if not api_key:
        return await ctx.send(
            "Set a API token before using this command. If you are the bot owner, then use `[p]performapi` to see how to add the API."
        )
    if user is None:
        embed = discord.Embed(
            description=f"**{ctx.author.mention}** {action}",
            color=discord.Colour.random(),
        )
    else:
        embed = discord.Embed(
            description=f"**{ctx.author.mention}** {action} {f'**{str(user.mention)}**' if user else 'themselves'}!",
            color=discord.Colour.random(),
        )
    embed.set_footer(
        text=f"Requested by {ctx.message.author.display_name}",
        icon_url=ctx.message.author.avatar_url,
    )
    embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url)

    embed.set_image(
        url=await api_call2("https://kawaii.red/api/gif/" + endpoint + "/token=" + api_key)
    )
    await ctx.reply(embed=embed, mention_author=False)
