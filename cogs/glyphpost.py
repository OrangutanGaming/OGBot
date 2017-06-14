from discord.ext import commands
import discord
import cogs.glyphs as Glyphs
import re

class GlyphPost():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["gp"])
    async def glyphpost(self, ctx, user=None, *, codes=None):
        async def sendUsage(ctx):
            await ctx.send("```q!glyphpost [user]"
                           "\nxxxx-xxxx-xxxx-xxxx"
                           "\nxxxx-xxxx-xxxx-xxxx```")

        def toLink(codes: list):
            final = []
            for code in codes:
                final.append(f"https://www.warframe.com/promocode?code={code}")
            return final

        platforms = ["PC",
                     "Xbox",
                     "PS4"]

        colours = {
            "PC": "0xFF00FF",  # 0xFFFFFF
            "Xbox": "0x46E300",
            "PS4": "0x0062FF"
        }

        if not codes:
            await sendUsage(ctx)
            return

        # if platform not in platforms:
        #     await ctx.send("Possible Platforms: " + " ,".join(platforms))
        #     return

        embed = discord.Embed(title=f"Glyphs"
        # f" for {platform}"
                                    f"")

        if user.lower() != "none":
            if not user.upper() in Glyphs.glyphs:
                await ctx.send(content=f"Can't find the glyph `{user}`.")
                return

            url = Glyphs.glyphs[user.upper()]

            embed.set_image(url=url)

        embed.set_footer(text=("Glyphs are the only endgame, Orangutan#9393"))

        codes = re.findall(r"([A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4})", codes)

        codesL = toLink(codes)
        for code in codesL:
            embed.add_field(name="Code Link", value=code)

        await ctx.send("@here", embed=embed)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(GlyphPost(bot))