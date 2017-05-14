from discord.ext import commands
import time
import unicodedata
import inflect
import upsidedown
import asyncio
import discord
import cogs.utils.checks as checks
import cogs.stickers as Stickers
import cogs.glen as Glen
import random

class Fun():
    def __init__(self, bot):
        self.bot = bot

    def texttoemoji(self, text: str = None):
        if not text:
            return
        text = text.lower()
        msg = ""
        p = inflect.engine()
        chars = list(text)

        for char in chars:
            Int = char.isdigit()

            if Int:
                msg += f":{p.number_to_words(int(char))}: "
            else:
                msg += f":regional_indicator_{char}: "
                # " ".join(["   " if x==" " else ":regional_indicator_{}:".format(x) for x in "hm hm"])

        return msg

    def upsidedown(self, text: str):
        return upsidedown.transform(text)

    @commands.command()
    async def ping(self, ctx):
        """Shows the response time."""
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        pingT = (after - before) * 1000
        pingT = round(pingT)

        await ctx.send(self.bot.blank + "Pong. :ping_pong: **{}ms**".format(pingT))

    @commands.command()
    async def charinfo(self, ctx, *, characters: str):
        """Gives unicode info on an emoji."""

        if len(characters) > 15:
            await ctx.send(self.bot.blank + f"Too many characters ({len(characters)}/15)")
            return

        fmt = "`\\U{0:>08}`: {1} - {2} \N{EM DASH} <http://www.fileformat.info/info/unicode/char/{0}>"

        def to_string(c):
            digit = format(ord(c), "x")
            name = unicodedata.name(c, "Name not found.")
            return fmt.format(digit, name, c)

        await ctx.send(self.bot.blank + "\n".join(map(to_string, characters)))

    @commands.command(name="upsidedown")
    async def _upsidedown(self, ctx, *, text: str):
        """Makes any text given upside down."""
        await ctx.send(self.upsidedown(text))

    @commands.command()
    async def emojitext(self, ctx, *, text: str = None):
        """Converts text to emojis."""

        msg = self.texttoemoji(text)

        if not msg:
            await ctx.send(self.bot.blank + "No Text!")
            return

        await ctx.send(msg)

    @commands.command(no_pm=True)
    async def channels(self, ctx):
        """Shows all channels on the current server."""
        channels = []
        for channel in ctx.guild.text_channels:
            channels.append(channel.name.title())
        await ctx.send(self.bot.blank + f"All text channels on the server {ctx.guild.name}: " + ", ".join(channels))

    @commands.command(no_pm=True)
    async def roles(self, ctx):
        """Shows all roles on the current server."""
        roles = []
        for role in ctx.guild.roles:
            roles.append(role.name)
        await ctx.send(self.bot.blank + f"All roles on the server {ctx.guild.name}: " + "`" + "`, `".join(roles)+"`")

    @commands.command()
    @checks.is_owner()
    async def status(self, ctx, *, status: str):
        """Changes the bot's status (For Bot Owner only)"""
        status = status.strip("`")
        await self.bot.change_presence(game=discord.Game(name=status))
        await asyncio.sleep(1)
        await ctx.send(f"**Playing** {ctx.guild.me.game}")

    @commands.command(aliases=["stickers"])
    async def sticker(self, ctx, sticker: str = None):
        """Posts Star Wars stickers."""
        if not sticker:
            allStickers = "`"+"`, `".join(Stickers.stickers.keys())+"`"
            await ctx.send(content=f"All available stickers are: {allStickers}")
            return
        if not sticker.lower() in Stickers.stickers:
            await ctx.send(content=f"Can't find the emoji `{sticker}`.")
            return
        sticker = sticker.lower()
        url = Stickers.stickers[sticker]

        embed = discord.Embed(title=f"{sticker.title()}")
        embed.set_image(url=url)

        await ctx.send(embed=embed)

    @commands.command()
    async def glen(self, ctx, *, picChosen=None):
        """Posts a random Glen quote."""
        link=False
        if not picChosen:
            picName = random.choice(list(Glen.quotes.keys()))
        else:
            picChosen = picChosen.lower()
            if picChosen == "list":
                allQuotes = "`" + "` ,`".join(list(Glen.quotes.keys())) + "`"
                await ctx.send(f"All Glen quotes are: {allQuotes}. Use `link` to see the link for the album.")
                return
            elif picChosen == "link":
                await ctx.send(Glen.album)
                return
            elif "debug" in picChosen:
                link=True
                if picChosen.strip("debug ") in list(Glen.quotes.keys()):
                    picName = picChosen.strip("debug ")
                else:
                    picName = None
            elif not picChosen in list(Glen.quotes.keys()):
                picName = None
            else:
                picName = picChosen

        if picName:
            url = Glen.quotes[picName]

            embed = discord.Embed(title="Glen Quote")
            embed.set_image(url=url)

            await ctx.send(embed=embed)

            if link:
                await ctx.send(f"<{url}>")
        else:
            await ctx.send(f"Could not find the quote `{picChosen}`")
            return

    @commands.command(aliases=["bin"])
    async def binary(self, ctx, *, text = None):
        """Convert text to binary"""
        if not text:
            await ctx.send("`o!binary <text>`")
            return
        text_bytes = bytes(text, "ascii")
        await ctx.send(" ".join(["{0:b}".format(x) for x in text_bytes]))

def setup(bot):
    bot.add_cog(Fun(bot))