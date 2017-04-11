from discord.ext import commands
import discord

class Messages():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["recents", "last"], no_pm=True)
    async def recent(self, ctx, user: discord.Member = None, channel: discord.TextChannel = None):
        """Quotes a user's most recent message in the channel given."""
        if not channel:
            channel = ctx.message.channel
        if not user:
            user = ctx.message.author
        quote = None
        async for message in channel.history(before=ctx.message, limit=100):
            if message.author == user:
                quote = message
                embed = discord.Embed(description=quote.content)
                embed.set_author(name=quote.author.name, icon_url=quote.author.avatar_url)
                embed.set_footer(text=(quote.created_at))
                await ctx.message.delete()
                await ctx.send(embed=embed)
                return
            if not quote:
                continue
            embed = discord.Embed(description="No message found")
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return

    @commands.command(enabled=False, hidden=True)
    async def quote(self, ctx, channel: discord.TextChannel = None, id = None):
        """Quotes a user's message in the channel given."""
        if not channel:
            channel = ctx.message.channel
        quote = None
        async for message in channel.history(before=ctx.message, limit=100):
            if message.author == user:
                quote = message
                embed = discord.Embed(description=quote.content)
                embed.set_author(name=quote.author.name, icon_url=quote.author.avatar_url)
                embed.set_footer(text=(quote.created_at))
                await ctx.message.delete()
                await ctx.send(embed=embed)
                return
            if not quote:
                continue
            embed = discord.Embed(description="No message found")
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return

def setup(bot):
    bot.add_cog(Messages(bot))