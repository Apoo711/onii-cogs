import discord
from redbot.core import commands
import aiohttp

async def api_call(call_uri, returnObj=False):
	async with aiohttp.ClientSession() as session:
		async with session.get(f"{call_uri}") as response:
			response = await response.json()
			if returnObj == False:
				return response["url"]
			elif returnObj == True:
				return response

class Perform(commands.Cog):
    """Perform different actions, like cuddle, poke etc."""
    def __init__(self, bot):
        self.bot = bot   
    
    @commands.cooldown(5, 7, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def cuddle(self, ctx):
          embed = discord.Embed(
				  title=f"**{ctx.author.name}** cuddled {'**{str(user.name)}**' if user else 'themselves'}!",
				  color=discord.Colour.random(),
          )

          embed.set_footer(
				  text=f"Requested by {ctx.message.author.display_name} | Powered by nekos.life",
				  icon_url=ctx.message.author.avatar_url,
          )
          embed.set_author(
				  name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url
          )

          embed.set_image(
				url=await api_call("https://nekos.life/api/v2/img/cuddle")
          )
          await ctx.reply(embed=embed)

    @commands.command(name="poke")
    @commands.bot_has_permissions(embed_links=True)
    async def poke(self, ctx: commands.Context):
     async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/poke') as r:
         em = discord.Embed(colour=discord.Colour.random(), title=f"**{ctx.author.name}** poked {'**{str(user.name)}**' if user else 'themselves'}!",)
         em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg", icon_url=ctx.author.avatar_url)
         em.set_image(url=res['url'])
         await ctx.reply(embed=em, mention_author=False)
        
    @commands.command(name="kiss")
    @commands.bot_has_permissions(embed_links=True)
    async def kiss(self, ctx: commands.Context):
     async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/kiss') as r:
         em = discord.Embed(colour=discord.Colour.random(), title=f"**{ctx.author.name}** just kissed {'**{str(user.name)}**' if user else 'themselves'}!",)
         em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg", icon_url=ctx.author.avatar_url)
         em.set_image(url=res['url'])
         await ctx.reply(embed=em, mention_author=False)

    @commands.command(name="hug")
    @commands.bot_has_permissions(embed_links=True)
    async def hug(self, ctx: commands.Context):
     async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/hug') as r:
         em = discord.Embed(colour=discord.Colour.random(), title=f"**{ctx.author.name}** just hugged {'**{str(user.name)}**' if user else 'themselves'}!",)
         em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg", icon_url=ctx.author.avatar_url)
         em.set_image(url=res['url'])
         await ctx.reply(embed=em, mention_author=False)

    @commands.command(name="pat")
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx: commands.Context):
     async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/pat') as r:
         em = discord.Embed(colour=discord.Colour.random(), title=f"**{ctx.author.name}** just patted {f'**{str(user.name)}**' if user else 'themselves'}!")
         em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg", icon_url=ctx.author.avatar_url)
         em.set_image(url=res['url'])
         await ctx.reply(embed=em, mention_author=False)

    @commands.command(name="tickle")
    @commands.bot_has_permissions(embed_links=True)
    async def tickle(self, ctx: commands.Context):
     async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/tickle') as r:
         em = discord.Embed(colour=discord.Colour.random(), title=f"**{ctx.author.name}** just tickled {'**{user.mention}**' if user else 'themselves'}!",)
         em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg", icon_url=ctx.author.avatar_url)
         em.set_image(url=res['url'])
         await ctx.reply(embed=em, mention_author=False)

    @commands.command(name="smug")
    @commands.bot_has_permissions(embed_links=True)
    async def smug(self, ctx: commands.Context):
     async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/smug') as r:
         em = discord.Embed(colour=discord.Colour.random(), title=f"**{ctx.author.name}** is acting all smug!")
         em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by shiro.gg", icon_url=ctx.author.avatar_url)
         em.set_image(url=res['url'])
         await ctx.reply(embed=em, mention_author=False)

