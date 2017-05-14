from discord.ext import commands
import discord
import cogs.utils.checks as checks

class Edit():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True, no_pm=True)
    @checks.is_dev()
    async def edit(self, ctx, channel, id, *, new: str):
        if ctx.guild.id == 281968634086031363:
            msg = await self.bot.get_channel(int(channel)).get_message(id)
            if msg.author.id == self.bot.user.id:
                await msg.edit(content=new)
                try: await ctx.message.delete()
                except discord.Forbidden: return
            else:
                try: await ctx.message.delete()
                except discord.Forbidden: return
                await ctx.send(self.bot.blank + "You can't give the ID of a message sent by another user!")



def setup(bot):
    bot.add_cog(Edit(bot))