from discord.ext import commands
import discord
import cogs.utils.checks as checks

class Moderation():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member = None, *, reason: str = None):
        if ctx.message.channel.permissions_for(ctx.message.author).kick_members or checks.is_dev_check(ctx):
            await member.kick(reason)
        else:
            await ctx.send("You need the permission `Kick Members` to run this command.")
            return

    @commands.command()
    @checks.has_permissions_owner(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason: str = None):
        if not member:
            await ctx.send("You must give a user!")
            return

        if member == ctx.guild.owner:
            await ctx.send("You can't ban the owner.")
            return

        print(reason)
        try: await member.ban(reason)
        except discord.Forbidden:
            await ctx.send("Error")
            return

    @commands.command(enabled=False)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.Member = None, *, reason: str = None):
        await member.kick(reason)


def setup(bot):
    bot.add_cog(Moderation(bot))