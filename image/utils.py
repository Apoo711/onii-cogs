import discord
import aiohttp


async def reddit_embed(self, ctx, subr: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://api.martinebot.com/v1/images/subreddit?name={subr}"
        ) as resp:
            origin = await resp.json()
            data = origin["data"]
            url = data["image_url"]
            subreddit = data["subreddit"] or ""
            sub_name = subreddit["name"] or "Unknown"
            sub_url = subreddit["url"] or ""
            author = data["author"] or ""
            r_author = author["name"] or "Unknown"
            r_author_url = author["url"] or ""
            title = data["title"] or ""
            created_at = data["created_at"] or ""
            comments = data["comments"] or ""
            ups = data["upvotes"] or ""
            link = data["post_url"] or ""

            if data["nsfw"] and not ctx.channel.is_nsfw():
                return await ctx.send(
                    "Sorry the contents of this post are NSFW and this channel isn't set to allow NSFW content, please turn it on and try again later."
                )

    embed = discord.Embed(
        title="Here's a random image...:frame_photo:",
        colour=await ctx.embed_colour(),
        description=(
            "**Post by:** [u/{}]({})\n"
            "**From:** [{}]({})\n"
            "**This post was created on:** <t:{}:F>\n"
            "**Title:** [{}]({})"
        ).format(
            r_author,
            r_author_url,
            sub_name,
            sub_url,
            created_at,
            title,
            link,
        ),
    )
    embed.set_image(url=url)
    embed.set_footer(
        text="👍  {} • 💬  {} • martinebot.com API".format(
            ups,
            comments,
        ),
        icon_url=ctx.message.author.avatar.url,
    )

    await ctx.reply(embed=embed, mention_author=False)
