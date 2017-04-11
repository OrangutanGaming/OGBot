from discord.ext import commands
import discord

class Count():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["mcount"], no_pm=True)
    async def msgcount(self, ctx, user: discord.Member = None, channel: discord.TextChannel = None):
        """Counts the amount of messages sent in the channel given by the user given."""
        counter = 0
        tmp = await ctx.send(self.bot.blank + "Counting messages...")
        if not user:
            user = ctx.message.author
        if not channel:
            channel = ctx.message.channel
        async for log in channel.history(limit=99, before=ctx.message):
            if log.author == user:
                counter += 1
        await ctx.message.delete()
        counter += 1
        if counter == 100:
            await tmp.edit(content="{} has at least {} messages in {}".format(user, counter, channel.mention))
        elif counter == 1:
            await tmp.edit(content="{} has 1 message in {}".format(user, channel.mention))
        elif counter <= 99:
            await tmp.edit(content="{} has {} messages in {}".format(user, counter, channel.mention))
        else:
            await tmp.edit(content="Counter Bug")
    
    @commands.command(aliases=["amcount"], no_pm=True)
    async def amsgcount(self, ctx, channel: discord.TextChannel = None):
        """Counts the amount of messages in the channel given."""
        counter = 0
        tmp = await ctx.send(self.bot.blank + "Counting messages...")
        if not channel:
            channel = ctx.message.channel
        async for message in channel.history(before=ctx.message, limit=99):
            counter += 1
        await ctx.message.delete()
        counter += 1
        if counter == 100:
            await tmp.edit(content="There are now at least {} messages in {}".format(counter, channel.mention))
        elif counter == 1:
            await tmp.edit(content="There is now 1 message in {}".format(channel.mention))
        elif counter <= 99:
            await tmp.edit(content="There are now {} messages in {}".format(counter, channel.mention))
        else:
            await tmp.edit(content="Counter Bug")

def setup(bot):
    bot.add_cog(Count(bot))