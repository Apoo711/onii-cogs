"""
Copyright 2021 Onii-chan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


from random import randint

import discord
from redbot.core import Config, commands

from .utils import get_hook, kawaiiembed, nekosembed, shiroembed
import logging


log = logging.getLogger("red.onii.perform")


class Perform(commands.Cog):
    """Perform different actions, like cuddle, poke etc."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=8423644625413, force_registration=True)
        default_global = {
            "feed": [
                "https://media1.tenor.com/images/93c4833dbcfd5be9401afbda220066ee/tenor.gif?itemid=11223742",
                "https://media1.tenor.com/images/33cfd292d4ef5e2dc533ff73a102c2e6/tenor.gif?itemid=12165913",
                "https://media1.tenor.com/images/72268391ffde3cd976a456ee2a033f46/tenor.gif?itemid=7589062",
                "https://media1.tenor.com/images/4b48975ec500f8326c5db6b178a91a3a/tenor.gif?itemid=12593977",
                "https://media1.tenor.com/images/187ff5bc3a5628b6906935232898c200/tenor.gif?itemid=9340097",
                "https://media1.tenor.com/images/15e7d9e1eb0aad2852fabda1210aee95/tenor.gif?itemid=12005286",
                "https://media1.tenor.com/images/d08d0825019c321f21293c35df8ed6a9/tenor.gif?itemid=9032297",
                "https://media1.tenor.com/images/571da4da1ad526afe744423f7581a452/tenor.gif?itemid=11658244",
                "https://media1.tenor.com/images/6bde17caa5743a22686e5f7b6e3e23b4/tenor.gif?itemid=13726430",
                "https://media1.tenor.com/images/fd3616d34ade61e1ac5cd0975c25a917/tenor.gif?itemid=13653906",
                "https://imgur.com/v7jsPrv",
            ],
            "spank": [
                "https://media1.tenor.com/images/ef5f040254c2fbf91232088b91fe2341/tenor.gif?itemid=13569259",
                "https://media1.tenor.com/images/fa2472b2cca1e4a407b7772b329eafb4/tenor.gif?itemid=21468457",
                "https://media1.tenor.com/images/2eb222b142f24be14ea2da5c84a92b08/tenor.gif?itemid=15905904",
                "https://media1.tenor.com/images/86b5a47d495c0e8c5c3a085641a91aa4/tenor.gif?itemid=15964704",
                "https://media1.tenor.com/images/31d58e53313dc9bbd6435d824d2a5933/tenor.gif?itemid=11756736",
                "https://media1.tenor.com/images/97624764cb41414ad2c60d2028c19394/tenor.gif?itemid=16739345",
                "https://media1.tenor.com/images/f21c5c56e36ce0dfcdfe7c7993578c46/tenor.gif?itemid=21371415",
                "https://media1.tenor.com/images/58f5dcc2123fc73e8fb6b76f149441bc/tenor.gif?itemid=12086277",
                "https://media1.tenor.com/images/eafb13b900645ddf3b30cf9cc28e9f91/tenor.gif?itemid=4603671",
                "https://media1.tenor.com/images/be2bb9db1c8b8dc2194ec6a1b3d96b89/tenor.gif?itemid=18811244",
                "https://media.giphy.com/media/OoCuLoM6iEhYk/giphy.gif",
                "https://media.giphy.com/media/Qo3qovmbqaKT6/giphy.gif",
            ],
        }
        default_member = {
            "cuddle_s": 0,
            "poke_s": 0,
            "kiss_s": 0,
            "hug_s": 0,
            "slap_s": 0,
            "pat_s": 0,
            "tickle_s": 0,
            "smug_s": 0,
            "lick_s": 0,
            "cry": 0,
            "sleep": 0,
            "spank_s": 0,
            "pout": 0,
            "blush": 0,
            "feed_s": 0,
            "punch_s": 0,
            "confused": 0,
            "amazed": 0,
            "highfive_s": 0,
            "plead_s": 0,
            "clap": 0,
            "facepalm": 0,
            "facedesk": 0,
            "kill_s": 0,
            "love_s": 0,
            "hide": 0,
            "laugh": 0,
            "lurk": 0,
            "bite_s": 0,
            "dance": 0,
            "yeet_s": 0,
            "dodge": 0,
            "happy": 0,
            "cute": 0,
            "lonely": 0,
            "mad": 0,
            "nosebleed": 0,
            "protect_s": 0,
            "run": 0,
            "scared": 0,
            "shrug": 0,
            "scream": 0,
            "stare": 0,
            "wave_s": 0,
        }
        default_target = {
            "cuddle_r": 0,
            "poke_r": 0,
            "kiss_r": 0,
            "hug_r": 0,
            "slap_r": 0,
            "pat_r": 0,
            "tickle_r": 0,
            "smug_r": 0,
            "lick_r": 0,
            "spank_r": 0,
            "feed_r": 0,
            "punch_r": 0,
            "highfive_r": 0,
            "plead_r": 0,
            "kill_r": 0,
            "love_r": 0,
            "bite_r": 0,
            "yeet_r": 0,
            "protect_r": 0,
            "wave_r": 0,
        }
        self.config.register_global(**default_global)
        self.config.register_user(**default_member)
        self.config.init_custom("Target", 2)
        self.config.register_custom("Target", **default_target)
        self.cache = {}

    __author__ = ["Onii-chan", "sravan"]
    __version__ = "5.4.1"  # idk what im doing with version

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    def cog_unload(self):
        global hug
        if hug:
            try:
                self.bot.remove_command("hug")
            except Exception as e:
                log.info(e)
            self.bot.add_command(hug)
        # This is worse case scenario but still important to check for
        if self.startup_task:
            self.startup_task.cancel()

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def cuddle(self, ctx, user: discord.Member):
        """Cuddle a user!"""
        embed = await nekosembed(self, ctx, user, "cuddled", "cuddle")
        target = await self.config.custom("Target", ctx.author.id, user.id).cuddle_r()
        used = await self.config.user(ctx.author).cuddle_s()
        embed.set_footer(text=f"{ctx.author.name}'s total cuddles: {used + 1} | {ctx.author.name} has cuddled {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).cuddle_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).cuddle_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="poke")
    @commands.bot_has_permissions(embed_links=True)
    async def poke(self, ctx, user: discord.Member):
        """Poke a user!"""
        embed = await shiroembed(self, ctx, "poked", "poke", user)
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        target = await self.config.custom("Target", ctx.author.id, user.id).poke_r()
        used = await self.config.user(ctx.author).poke_s()
        embed.set_footer(text=f"{ctx.author.name}'s total pokes: {used + 1} | {ctx.author.name} has poked {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).poke_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).poke_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="kiss")
    @commands.bot_has_permissions(embed_links=True)
    async def kiss(self, ctx, user: discord.Member):
        """Kiss a user!"""
        embed = await shiroembed(self, ctx, "just kissed", "kiss", user)
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        target = await self.config.custom("Target", ctx.author.id, user.id).kiss_r()
        used = await self.config.user(ctx.author).kiss_s()
        embed.set_footer(text=f"{ctx.author.name}'s total kisses: {used + 1} | {ctx.author.name} has kissed {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).kiss_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).kiss_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="hug")
    @commands.bot_has_permissions(embed_links=True)
    async def hug(self, ctx, user: discord.Member):
        """Hugs a user!"""
        embed = await shiroembed(self, ctx, "just hugged", "hug", user)
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        target = await self.config.custom("Target", ctx.author.id, user.id).hug_r()
        used = await self.config.user(ctx.author).hug_s()
        embed.set_footer(text=f"{ctx.author.name}'s total hugs: {used + 1} | {ctx.author.name} has hugged {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).hug_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).hug_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="pat")
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx, user: discord.Member):
        """Pats a user!"""
        embed = await shiroembed(self, ctx, "just patted", "pat", user)
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        target = await self.config.custom("Target", ctx.author.id, user.id).pat_r()
        used = await self.config.user(ctx.author).pat_s()
        embed.set_footer(text=f"{ctx.author.name}'s total pats: {used + 1} | {ctx.author.name} has patted {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).pat_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).pat_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="tickle")
    @commands.bot_has_permissions(embed_links=True)
    async def tickle(self, ctx, user: discord.Member):
        """Tickles a user!"""
        embed = await shiroembed(self, ctx, "just tickled", "tickle", user)
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        target = await self.config.custom("Target", ctx.author.id, user.id).tickle_r()
        used = await self.config.user(ctx.author).tickle_s()
        embed.set_footer(text=f"{ctx.author.name}'s total tickles: {used + 1} | {ctx.author.name} has tickled {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).tickle_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).tickle_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="smug")
    @commands.bot_has_permissions(embed_links=True)
    async def smug(self, ctx):
        """Be smug towards someone!"""
        embed = await shiroembed(self, ctx, "is acting so smug!", "smug")
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        used = await self.config.user(ctx.author).smug()
        embed.set_footer(text=f"{ctx.author.name}'s total smugs: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).smug.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="lick")
    @commands.bot_has_permissions(embed_links=True)
    async def lick(self, ctx, user: discord.Member):
        """Licks a user!"""
        embed = await shiroembed(self, ctx, "just licked", "lick", user)
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        target = await self.config.custom("Target", ctx.author.id, user.id).lick_r()
        used = await self.config.user(ctx.author).lick_s()
        embed.set_footer(text=f"{ctx.author.name}'s total licks: {used + 1} | {ctx.author.name} has licked {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).lick_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).lick_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="slap")
    @commands.bot_has_permissions(embed_links=True)
    async def slap(self, ctx, user: discord.Member):
        """Slaps a user!"""
        embed = await shiroembed(self, ctx, "just slapped", "slap", user)
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        target = await self.config.custom("Target", ctx.author.id, user.id).slap_r()
        used = await self.config.user(ctx.author).slap_s()
        embed.set_footer(text=f"{ctx.author.name}'s total slaps: {used + 1} | {ctx.author.name} has slapped {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).slap_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).slap_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="cry")
    @commands.bot_has_permissions(embed_links=True)
    async def cry(self, ctx):
        """Start crying!"""
        embed = await shiroembed(self, ctx, "is crying!", "cry")
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        used = await self.config.user(ctx.author).cry()
        embed.set_footer(text=f"{ctx.author.name}'s total cries: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).cry.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="sleep")
    @commands.bot_has_permissions(embed_links=True)
    async def sleep(self, ctx):
        """Act sleepy!"""
        embed = await shiroembed(self, ctx, "is sleepy!, sleep")
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        used = await self.config.user(ctx.author).sleep()
        embed.set_footer(text=f"{ctx.author.name}'s total sleeps: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).sleep.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="spank")
    @commands.bot_has_permissions(embed_links=True)
    async def spank(self, ctx, user: discord.Member):
        """Spanks a user!"""

        images = await self.config.spank()

        mn = len(images)
        i = randint(0, mn - 1)

        em = discord.Embed(
            colour=discord.Colour.random(),
            description=f"**{ctx.author.mention}** just spanked {f'**{str(user.mention)}**' if user else 'themselves'}!",
        )
        em.set_image(url=images[i])
        target = await self.config.custom("Target", ctx.author.id, user.id).spank_r()
        used = await self.config.user(ctx.author).spank_s()
        em.set_footer(text=f"{ctx.author.name}'s total spanks: {used + 1} | {ctx.author.name} has spanked {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=em
                    )
            except discord.Forbidden:
                await ctx.reply(embed=em, mention_author=False)
        else:
            await ctx.reply(embed=em, mention_author=False)
        await self.config.user(ctx.author).spank_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).spank_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="pout")
    @commands.bot_has_permissions(embed_links=True)
    async def pout(self, ctx):
        """Act pout!"""
        embed = await shiroembed(self, ctx, "is acting pout!", "pout")
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        used = await self.config.user(ctx.author).pout()
        embed.set_footer(text=f"{ctx.author.name}'s total pouts: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).pout.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="blush")
    @commands.bot_has_permissions(embed_links=True)
    async def blush(self, ctx):
        """Act blush!"""
        embed = await shiroembed(self, ctx, "is blushing!", "blush")
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        used = await self.config.user(ctx.author).blush()
        embed.set_footer(text=f"{ctx.author.name}'s total blushes: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).blush.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="feed")
    @commands.bot_has_permissions(embed_links=True)
    async def feed(self, ctx, user: discord.Member):
        """Feeds a user!"""

        images = await self.config.feed()

        mn = len(images)
        i = randint(0, mn - 1)

        em = discord.Embed(
            colour=discord.Colour.random(),
            description=f"**{ctx.author.mention}** feeds {f'**{str(user.mention)}**' if user else 'themselves'}!",
        )
        em.set_image(url=images[i])
        target = await self.config.custom("Target", ctx.author.id, user.id).feed_r()
        used = await self.config.user(ctx.author).feed_s()
        em.set_footer(text=f"{ctx.author.name}'s total feeds: {used + 1} | {ctx.author.name} has feeded {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=em
                    )
            except discord.Forbidden:
                await ctx.reply(embed=em, mention_author=False)
        else:
            await ctx.reply(embed=em, mention_author=False)
        await self.config.user(ctx.author).feed_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).feed_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="punch")
    @commands.bot_has_permissions(embed_links=True)
    async def punch(self, ctx, user: discord.Member):
        """Punch a user!"""
        embed = await shiroembed(self, ctx, "just punched", "punch", user)
        if embed is False:
            return await ctx.send("shiro.gg api is down")
        target = await self.config.custom("Target", ctx.author.id, user.id).punch_r()
        used = await self.config.user(ctx.author).punch_s()
        embed.set_footer(text=f"{ctx.author.name}'s total punxhes: {used + 1} | {ctx.author.name} has punxhed {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).punch_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).punch_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="confuse", aliases=["confused"])
    @commands.guild_only()
    async def confuse(self, ctx):
        """Act confused!"""
        embed = await kawaiiembed(self, ctx, "is confused!", "confused")
        used = await self.config.user(ctx.author).confuse()
        embed.set_footer(text=f"{ctx.author.name}'s total confusions: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).confuse.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="amazed", aliases=["amazing"])
    @commands.guild_only()
    async def amazed(self, ctx):
        """Act amazed!"""
        embed = await kawaiiembed(self, ctx, "is amazed!", "amazing")
        used = await self.config.user(ctx.author).amazed()
        embed.set_footer(text=f"{ctx.author.name}'s total amazes: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).amazed.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def highfive(self, ctx, user: discord.Member):
        """Highfive a user!"""
        embed = await kawaiiembed(self, ctx, "highfived", "highfive", user)
        target = await self.config.custom("Target", ctx.author.id, user.id).highfive_r()
        used = await self.config.user(ctx.author).highfive_s()
        embed.set_footer(text=f"{ctx.author.name}'s total highfives: {used + 1} | {ctx.author.name} has highfived {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).highfive_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).highfive_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="plead", aliases=["ask"])
    @commands.guild_only()
    async def plead(self, ctx, user: discord.Member):
        """Asks a user!"""
        embed = await kawaiiembed(self, ctx, "is pleading", "ask", user)
        target = await self.config.custom("Target", ctx.author.id, user.id).plead_r()
        used = await self.config.user(ctx.author).plead_s()
        embed.set_footer(text=f"{ctx.author.name}'s total pleads: {used + 1} | {ctx.author.name} has pleaded {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).plead_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).plead_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="clap")
    @commands.guild_only()
    async def clap(self, ctx):
        """Clap for someone!"""
        embed = await kawaiiembed(self, ctx, "is clapping!", "clap")
        used = await self.config.user(ctx.author).clap()
        embed.set_footer(text=f"{ctx.author.name}'s total claps: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).clap.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="facepalm")
    @commands.guild_only()
    async def facepalm(self, ctx):
        """Do a facepalm!"""
        embed = await kawaiiembed(self, ctx, "is facepalming!", "facepalm")
        used = await self.config.user(ctx.author).facepalm()
        embed.set_footer(text=f"{ctx.author.name}'s total facepalms: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).facepalm.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="headdesk", aliases=["facedesk"])
    @commands.guild_only()
    async def facedesk(self, ctx):
        """Do a facedesk!"""
        embed = await kawaiiembed(self, ctx, "is facedesking!", "facedesk")
        used = await self.config.user(ctx.author).facedesk()
        embed.set_footer(text=f"{ctx.author.name}'s total facedesks: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).facedesk.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def kill(self, ctx, user: discord.Member):
        """Kill a user!"""
        embed = await kawaiiembed(self, ctx, "killed", "kill", user)
        target = await self.config.custom("Target", ctx.author.id, user.id).kill_r()
        used = await self.config.user(ctx.author).kill_s()
        embed.set_footer(text=f"{ctx.author.name}'s total kills: {used + 1} | {ctx.author.name} has killed {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).kill_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).kill_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def love(self, ctx, user: discord.Member):
        """Love a user!"""
        embed = await kawaiiembed(self, ctx, "loves", "love", user)
        target = await self.config.custom("Target", ctx.author.id, user.id).love_r()
        used = await self.config.user(ctx.author).love_s()
        embed.set_footer(text=f"{ctx.author.name}'s total loves: {used + 1} | {ctx.author.name} has loved {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).love_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).love_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="hide")
    @commands.guild_only()
    async def hide(self, ctx):
        """Hide yourself!"""
        embed = await kawaiiembed(self, ctx, "is hideing!", "hide")
        used = await self.config.user(ctx.author).hide()
        embed.set_footer(text=f"{ctx.author.name}'s total hides: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).hide.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="laugh")
    @commands.guild_only()
    async def laugh(self, ctx):
        """Start laughing!"""
        embed = await kawaiiembed(self, ctx, "is laughing!", "laugh")
        used = await self.config.user(ctx.author).laugh()
        embed.set_footer(text=f"{ctx.author.name}'s total laughs: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).laugh.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="peek", aliases=["lurk"])
    @commands.guild_only()
    async def lurk(self, ctx):
        """Start lurking!"""
        embed = await kawaiiembed(self, ctx, "is lurking!", "peek")
        used = await self.config.user(ctx.author).lurk()
        embed.set_footer(text=f"{ctx.author.name}'s total lurks: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).lurk.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def bite(self, ctx, user: discord.Member):
        """Bite a user!"""
        embed = await kawaiiembed(self, ctx, "is biting", "bite", user)
        target = await self.config.custom("Target", ctx.author.id, user.id).bite_r()
        used = await self.config.user(ctx.author).bite_s()
        embed.set_footer(text=f"{ctx.author.name}'s total bites: {used + 1} | {ctx.author.name} has bitten {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).bite_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).bite_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="dance")
    @commands.guild_only()
    async def dance(self, ctx):
        """Start dancing!"""
        embed = await kawaiiembed(self, ctx, "is dancing", "dance")
        used = await self.config.user(ctx.author).dance()
        embed.set_footer(text=f"{ctx.author.name}'s total dances: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).dance.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def yeet(self, ctx, user: discord.Member):
        """Yeet someone!"""
        embed = await kawaiiembed(self, ctx, "yeeted", "yeet", user)
        target = await self.config.custom("Target", ctx.author.id, user.id).yeet_r()
        used = await self.config.user(ctx.author).yeet_s()
        embed.set_footer(text=f"{ctx.author.name}'s total yeets: {used + 1} | {ctx.author.name} has yeeted {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).yeet_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).yeet_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="dodge")
    @commands.guild_only()
    async def dodge(self, ctx):
        """Dodge something!"""
        embed = await kawaiiembed(self, ctx, "is dodging!", "dodge")
        used = await self.config.user(ctx.author).dodge()
        embed.set_footer(text=f"{ctx.author.name}'s total dodges: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).dodge.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="happy")
    @commands.guild_only()
    async def happy(self, ctx):
        """Act happy!"""
        embed = await kawaiiembed(self, ctx, "is happy!", "happy")
        used = await self.config.user(ctx.author).happy()
        embed.set_footer(text=f"{ctx.author.name}'s total happiness: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).happy.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="cute")
    @commands.guild_only()
    async def cute(self, ctx):
        """Act cute!"""
        embed = await kawaiiembed(self, ctx, "is acting cute!", "cute")
        used = await self.config.user(ctx.author).cute()
        embed.set_footer(text=f"{ctx.author.name}'s total cuteness: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).cute.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="lonely", aliases=["alone"])
    @commands.guild_only()
    async def lonely(self, ctx):
        """Act lonely!"""
        embed = await kawaiiembed(self, ctx, "is lonely!", "lonely")
        used = await self.config.user(ctx.author).lonely()
        embed.set_footer(text=f"{ctx.author.name}'s total loneliness: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).lonely.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="mad", aliases=["angry"])
    @commands.guild_only()
    async def mad(self, ctx):
        """Act angry!"""
        embed = await kawaiiembed(self, ctx, "is angry!", "mad")
        used = await self.config.user(ctx.author).mad()
        embed.set_footer(text=f"{ctx.author.name}'s total angriness: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).mad.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="nosebleed")
    @commands.guild_only()
    async def nosebleed(self, ctx):
        """Start bleeding from nose!"""
        embed = await kawaiiembed(self, ctx, "'s nose is bleeding!", "nosebleed")
        used = await self.config.user(ctx.author).nosebleed()
        embed.set_footer(text=f"{ctx.author.name}'s total nosebleeds: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).nosebleed.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    @commands.guild_only()
    async def protect(self, ctx, user: discord.Member):
        """Protech someone!"""
        embed = await kawaiiembed(self, ctx, "is protecting!", "protect", user)
        target = await self.config.custom("Target", ctx.author.id, user.id).protect_r()
        used = await self.config.user(ctx.author).protect_s()
        embed.set_footer(text=f"{ctx.author.name}'s total protects: {used + 1} | {ctx.author.name} has protected {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).protect_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).protect_r.set(target + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="run")
    @commands.guild_only()
    async def run(self, ctx):
        """Start running!"""
        embed = await kawaiiembed(self, ctx, "is running!", "run")
        used = await self.config.user(ctx.author).run()
        embed.set_footer(text=f"{ctx.author.name}'s total runs: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).run.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="scared")
    @commands.guild_only()
    async def scared(self, ctx):
        """Act scared!"""
        embed = await kawaiiembed(self, ctx, "is scared!", "scared")
        used = await self.config.user(ctx.author).scared()
        embed.set_footer(text=f"{ctx.author.name}'s total scares: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).scared.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="shrug")
    @commands.guild_only()
    async def shrug(self, ctx):
        """Start shrugging!"""
        embed = await kawaiiembed(self, ctx, "is shrugging!", "shrug")
        used = await self.config.user(ctx.author).shrug()
        embed.set_footer(text=f"{ctx.author.name}'s total shrugs: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).shrug.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="scream")
    @commands.guild_only()
    async def scream(self, ctx):
        """Start screaming!"""
        embed = await kawaiiembed(self, ctx, "is screaming!", "scream")
        used = await self.config.user(ctx.author).scream()
        embed.set_footer(text=f"{ctx.author.name}'s total screams: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).scream.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="stare")
    @commands.guild_only()
    async def stare(self, ctx):
        """Stare someone!"""
        embed = await kawaiiembed(self, ctx, "is stareing!", "stare")
        used = await self.config.user(ctx.author).stare()
        embed.set_footer(text=f"{ctx.author.name}'s total stares: {used + 1}")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).stare.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(aliases=["welcome"])
    @commands.guild_only()
    async def wave(self, ctx, user: discord.Member):
        """Wave to someone!"""
        embed = await kawaiiembed(self, ctx, "is waving", "wave", user)
        target = await self.config.custom("Target", ctx.author.id, user.id).wave_r()
        used = await self.config.user(ctx.author).wave_s()
        embed.set_footer(text=f"{ctx.author.name}'s total waves: {used + 1} | {ctx.author.name} has waved {user.name} {target + 1} times")
        if ctx.channel.permissions_for(ctx.channel.guild.me).manage_webhooks is True:
            try:
                hook = await get_hook(self, ctx)
                await hook.send(
                    username=ctx.author.display_name,
                    avatar_url=ctx.author.avatar_url,
                    embed=embed
                    )
            except discord.Forbidden:
                await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(embed=embed, mention_author=False)
        await self.config.user(ctx.author).wave_s.set(used + 1)
        await self.config.custom("Target", ctx.author.id, user.id).wave_r.set(target + 1)

    @commands.is_owner()
    @commands.command()
    async def performapi(self, ctx):
        """Steps to get the API token needed for few commands."""
        embed = discord.Embed(
            title="How to set API for perform cog",
            description=(
                "1. Go to https://kawaii.red/\n"
                "2. Login using your discord account\n"
                "3. Click on dashboard and copy your token\n"
                "4. Use `[p]set api perform api_key <token>`",
            )
        )
        await ctx.send(embed=embed)

def setup(bot):
    global hug

    hug = bot.remove_command("hug")
    bot.add_cog(Perform(bot))
