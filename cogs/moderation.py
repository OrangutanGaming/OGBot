from discord.ext import commands
import discord

class Moderation():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member = None, *, reason: str = None):
        if ctx.message.channel.permissions_for(ctx.message.author).kick_members:
            await member.kick(reason)
        else:
            await ctx.send("You need the permission `Kick Members` to run this command.")
            return

    @commands.command()
    async def ban(self, ctx, member: discord.Member = None, *, reason: str = None):
        if ctx.message.channel.permissions_for(ctx.message.author).ban_members:
            await member.ban(reason)
        else:
            await ctx.send("You need the permission `Ban Members` to run this command.")
            return

    @commands.command(enabled=False)
    async def unban(self, ctx, member: discord.Member = None, *, reason: str = None):
        if ctx.message.channel.permissions_for(ctx.message.author).kick_members:
            await member.kick(reason)
        else:
            await ctx.send("You need the permission `Kick Members` to run this command.")
            return

def setup(bot):
    bot.add_cog(Moderation(bot))