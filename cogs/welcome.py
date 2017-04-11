from discord.ext import commands
import discord

class Welcome():
    def __init__(self, bot):
        self.bot = bot

    # welcome = False
    #
    # @commands.command()
    # async def welcome(self, ctx, welcome):
    #     welcome = not welcome
    #     await ctx.send(self.bot.blank + "Welcome is set to {}".format(welcome))
    #
    # async def on_member_join(self, member):
    #     if welcome:
    #         await member.guild.default_channel.send("{0.name} joined in {0.joined_at}".format(member))

def setup(bot):
    bot.add_cog(Welcome(bot))