import discord
import asyncio
import random
from redbot.core import commands
from redbot.core.config import Group
import aiohttp

footer1 = text=f"Requested by {ctx.message.author.display_name}#{ctx.message.author.discriminator}", 
icon_url=ctx.message.author.avatar_url

class Wallpaper(commands.Cog):
    
    @commands.group(aliases=["wp"])
    async def wallpaper(self, ctx):
        """Wallpaper commands"""
        
    @wallpaper.group(aliases=["c"])
    async def character(self, ctx):
        """Wallpaper commands"""
    
    @character.command(aliases=["zen"], name="zenitsu")
    @commands.bot_has_permissions(embed_links=True)
    async def zenitsu(self, ctx): 
          embed=discord.Embed(color=0xFFF300)
          embed.add_field(name="Zenitsu", value="You asked for some Zenitsu wallpapers?", inline=False)
          embed.set_image(url = random.choice(("https://images2.alphacoders.com/100/thumb-1920-1007550.jpg", "https://cdn.discordapp.com/attachments/736113073328357386/813287821355778108/thumb-1920-1007788.jpg", "https://cdn.discordapp.com/attachments/736113073328357386/801781638991183903/thumb-1920-1026796.jpg", "https://www.enjpg.com/img/2020/zenitsu-12.jpg", "https://images.wallpapersden.com/image/download/breath-of-thunder-zenitsu-agatsuma_a21oameUmZqaraWkpJRobWllrWdma2U.jpg")))
          embed.set_footer(text=f"footer1")
          await ctx.reply(embed=embed, mention_author=False)
    
    @character.command(aliases=["nar"], name="naruto")
    @commands.bot_has_permissions(embed_links=True)
    async def naruto(self, ctx): 
          embed=discord.Embed(color=0xDC8D22)
          embed.add_field(name="Zenitsu", value="You asked for some Naruto wallpapers?", inline=False)
          embed.set_image(url = random.choice(("https://cdn.discordapp.com/attachments/736113073328357386/748994203110866944/thumb-1920-532559.jpg", "https://cdn.discordapp.com/attachments/736113073328357386/800950373233459210/thumb-1920-303042.png", "https://cdn.discordapp.com/attachments/742663617522040843/818725598041735168/d5be3a21870ee870bc4b45dd92e68297.jpg", "https://cdn.discordapp.com/attachments/736113073328357386/800950373233459210/thumb-1920-303042.png", "https://wallpaperaccess.com/full/4757768.jpg", "https://wallpaperaccess.com/full/677436.jpg", "https://cdn.hipwallpaper.com/i/47/31/sqE0Hc.jpg", "https://www.teahub.io/photos/full/62-625201_naruto-uzumaki-kurama-4k-naruto-and-kurama-wallpaper.jpg", "https://wallpaper.dog/large/5456675.jpg")))
          embed.set_footer(
                            text=f"Requested by {ctx.message.author.display_name}#{ctx.message.author.discriminator}", 
                            icon_url=ctx.message.author.avatar_url
          )
          await ctx.reply(embed=embed, mention_author=False)
            
    @character.command(aliases=["jiro"],  name="tanjiro")
    @commands.bot_has_permissions(embed_links=True)
    async def tanjiro(self, ctx):
          embed=discord.Embed(colour=0xFF9900)
          embed.add_field(name="Tanjiro", value="Behold Tanjiro!", inline=False)
          embed.set_image(url  =  random.choice(("https://wallpapercave.com/wp/wp4771870.jpg",  "https://wallpaperaccess.com/full/2661458.jpg",  "https://wallpapercave.com/wp/wp5194112.jpg")))
          embed.set_footer(text=f"footer1")
          await ctx.reply(embed=embed, mention_author=False)
                       
    
    
    @wallpaper.group(aliases=["a"])
    async def anime(self, ctx):
        """Wallpaper commands"""
        
    @anime.command(name="chibi")
    @commands.bot_has_permissions(embed_links=True)
    async def chibi(self, ctx):
          """Random cute wallpaper(Will contain characters from multiple anime's)"""
          embed=discord.Embed(colour=0xFF00AB)
          embed.add_field(name="Chibi", value="Aren't they cute?", inline=False)
          embed.set_image(url  =  random.choice(("https://cdn.discordapp.com/attachments/763154622675681331/836852290933489664/bg-01.png", "https://cdn.discordapp.com/attachments/763154622675681331/836908773146361906/bg-02.png")))
          embed.set_footer(text=f"footer1")
          await ctx.reply(embed=embed, mention_author=False)
    
    @anime.command(aliases=["rando"])
    @commands.bot_has_permissions(embed_links=True)
    async def random(self, ctx):
     async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/wallpapers') as r:
         res = await r.json()
         embed = discord.Embed(
          title = "Here's your random wallpaper!",
          footer = f"footer1",
          color = discord.Color.random() 
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed, mention_author=False)
        
    @anime.command(name="randomavatar", aliases=["rav"])
    @commands.bot_has_permissions(embed_links=True)
    async def avatar_random(self, ctx: commands.Context):
     async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/avatars') as r:
         res = await r.json()
         embed = discord.Embed(
          title = f"**Here's your anime avatar!**",
          footer = f"footer1",
          color = discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed, mention_author=False)
    
