from discord.ext import commands
import discord

class Edit():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True, no_pm=True)
    async def edit(self, ctx, id, *, new: str):
        if ctx.guild.id == 166488311458824193 or ctx.guild.id == 291171882512678912:
            msg = await ctx.channel.get_message(id)
            if msg.author.id == 281486759332806658:
                await msg.edit(content=new)
                try: await ctx.message.delete()
                except discord.Forbidden: return
            else:
                try: await ctx.message.delete()
                except discord.Forbidden: return
                await ctx.send(self.bot.blank + "You can't give the ID of a message sent by another user!")



def setup(bot):
    bot.add_cog(Edit(bot))