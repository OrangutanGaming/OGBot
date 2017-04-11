from discord.ext import commands
import discord
import asyncio

class Clears():
    def __init__(self, bot):
        self.bot= bot

    # @commands.command(pass_context=True, aliases=["del", "delete", "wipe"])
    # async def clear(self, ctx, amount = 100, user: discord.User = None, channel: discord.TextChannel = None):
    #     to_delete = []
    #     cutoff = datetime.datetime.now() - datetime.timedelta(days=14, seconds=-10)
    #     if not channel:
    #         channel = ctx.message.channel
    #     if amount > 100:
    #         amount = 100
    #     try:
    #         async for message in self.bot.logs_from(channel, after=cutoff, limit=amount):
    #             if user is None or message.author == user:
    #                 to_delete.append(message)
    #             if len(to_delete) >= amount:
    #                 break
    #
    #             count = len(to_delete)
    #
    #             while to_delete:
    #                 await ctx.channel.delete_messages(to_delete[:amount])
    #                 to_delete = to_delete[amount:]
    #
    #             await self.bot.say("Deleted {} messages".format(count), delete_after=3)
    #
    #     except discord.Forbidden as error:
    #         await self.bot.say("{} does not have permissions".format(self.bot.user.name), delete_after=3)

    @commands.command(aliases=["bclear"], no_pm=True, enabled=False, hidden=True)
    async def botclear(self, ctx, amount=100):

        def check_is_me(msg):
            return msg.author.id == self.bot.user.id

        if ctx.message.channel.permissions_for(ctx.message.author).manage_messages:

            try:
                deleted = await ctx.channel.purge(check=check_is_me, limit=amount)
                count = len(deleted)
                if count == 1:
                    tmp = await ctx.send(self.bot.blank + "Deleted {} message".format(count))
                else:
                    tmp = await ctx.send(self.bot.blank + "Deleted {} messages".format(count))
                await asyncio.sleep(3)
                await ctx.channel.delete_messages([tmp, ctx.message])
            except discord.Forbidden as error:
                await ctx.send(self.bot.blank + "{} does not have permissions".format(self.bot.user.name))

        else:
            await ctx.send(self.bot.blank + "You must have the `Manage Messages` permission in order to run that command")

    @commands.command(aliases=["del", "delete", "wipe"], no_pm=True)
    async def clear(self, ctx, amount=100, channel: discord.TextChannel = None, user: discord.User = None):
        """Deletes an amount of messages given in the channel given."""

        if ctx.message.channel.permissions_for(ctx.message.author).manage_messages:


            if not channel:
                channel = ctx.message.channel

            try:
                # async for message in channel.history(limit=amount, before=ctx.message, reverse=True):
                #     Time = message.created_at
                #     break
                #
                # timeMsg = datetime.date(Time)
                # Today = datetime.date.today()
                # Age = timeMsg - Today
                # if Age <= 14:
                # count = 0
                # async for message in channel.history(limit=amount, before=ctx.message):
                #     if not user:
                #         await message.delete()
                #         count += 1
                #     else:
                #         if message.author == user:
                #             await message.delete()
                #             count += 1
                #         else:
                #             continue
                # else:
                #     await ctx.send(self.bot.blank + "Those messages are too old")
                #     return

                deleted = await channel.purge(limit=amount, before=ctx.message)
                count = len(deleted)

                if count == 1:
                    tmp = await ctx.send(self.bot.blank + "Deleted {} message".format(count))
                else:
                    tmp = await ctx.send(self.bot.blank + "Deleted {} messages".format(count))
                await asyncio.sleep(3)
                await ctx.channel.delete_messages([tmp, ctx.message])


            except discord.Forbidden as error:
                await ctx.send(self.bot.blank + "{} does not have permissions".format(self.bot.user.name))

        else:
            await ctx.send(self.bot.blank + "You must have the `Manage Messages` permission in order to run that command")

def setup(bot):
    bot.add_cog(Clears(bot))