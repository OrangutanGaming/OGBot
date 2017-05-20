from discord.ext import commands
import discord
import cogs.utils.checks as checks

class Moderation():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions_owner(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason: str = None):
        async def ban(self, ctx, member: discord.Member = None, *, reason: str = None):
            if not ctx.message.channel.permissions_for(ctx.guild.me).kick_members:
                await ctx.send("I need the permission `Ban Members`.")
                return

            if not member:
                await ctx.send("You must give a user!")
                return

            if member == ctx.guild.owner:
                await ctx.send("You can't kick the owner.")
                return

            try:
                await member.kick(reason=reason)
            except discord.Forbidden:
                await ctx.send("Error")
                return

    @commands.command()
    @checks.has_permissions_owner(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason: str = None):
        if not ctx.message.channel.permissions_for(ctx.guild.me).ban_members:
            await ctx.send("I need the permission `Kick Members`.")
            return


        if not member:
            await ctx.send("You must give a user!")
            return

        if member == ctx.guild.owner:
            await ctx.send("You can't ban the owner.")
            return

        try: await member.ban(reason=reason)
        except discord.Forbidden:
            await ctx.send("Error")
            return

    @commands.command(enabled=False)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.Member = None, *, reason: str = None):
        await member.kick(reason)


def setup(bot):
    bot.add_cog(Moderation(bot))