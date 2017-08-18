from discord.ext import commands
import discord
import cogs.glyphs as Glyphs
import re

class GlyphPost():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["gp"])
    async def glyphpost(self, ctx, *, codes=None):
        usage = "```o!glyphpost \nxxxx-xxxx-xxxx-xxxx\nxxxx-xxxx-xxxx-xxxx```"

        def toLink(codes: list):
            final = []
            for code in codes:
                final.append(f"https://www.warframe.com/promocode?code={code}")
            return final

        if not codes:
            await ctx.send(usage)
            return

        # glyphs = Glyphs.fetchGlyphs()
        embed = discord.Embed(title=f"Glyphs"
        # f" for {platform}"
                                    f"")

        embed.set_footer(text=(f"Glyphs are the only endgame, Orangutan#9393. Posted by {ctx.message.author}"))

        codes = re.findall(r"([A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4})", codes)

        codesL = toLink(codes)
        for code in codesL:
            embed.add_field(name="Code Link", value=code)

        await ctx.send("@here", embed=embed)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(GlyphPost(bot))