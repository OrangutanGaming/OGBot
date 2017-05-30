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
        async for log in channel.history(before=ctx.message, limit=999):
            if log.author == user:
                counter += 1
        await ctx.message.delete()
        if counter == 1000: # Max
            await tmp.edit(content=f"{user} has sent {counter} messages in {channel.mention}") # ~over 1000 (cap)
        elif counter == 1: # 0 before command
            await tmp.edit(content=f"{user} has sent 1 message in {channel.mention}") # No Plural
        elif counter <= 999 or counter == 0: # 2-999
            await tmp.edit(content=f"{user} has sent {counter} messages in {channel.mention}")
        else:
            await tmp.edit(content="Counter Bug") # Shouldn't be possible
    
    @commands.command(aliases=["amcount"], no_pm=True)
    async def amsgcount(self, ctx, channel: discord.TextChannel = None):
        """Counts the amount of messages in the channel given."""
        tmp = await ctx.send(self.bot.blank + "Counting messages...")
        if not channel:
            channel = ctx.message.channel
        history = await channel.history(before=ctx.message, limit=999).flatten()
        counter = len(history)
        await ctx.message.delete()
        counter += 1 # To include tmp. 1<=counter<=1000
        if counter == 1000: # Max
            await tmp.edit(content=f"There are now at least {counter} messages in {channel.mention}") # ~over 1000 (cap)
        elif counter == 1: # 0 before command
            await tmp.edit(content=f"There is now 1 message in {channel.mention}") # No Plural
        elif counter <= 999: # 2-999
            await tmp.edit(content=f"There are now {counter} messages in {channel.mention}")
        else:
            await tmp.edit(content="Counter Bug") # Shouldn't be possible

def setup(bot):
    bot.add_cog(Count(bot))