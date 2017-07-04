from discord.ext import commands
import discord
import BotIDs
import cogs.utils.prefix as Prefix
import psutil
import sys

class Info():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["uinfo"], no_pm=True)
    async def userinfo(self, ctx, user: discord.User = None):
        """Shows the info on a user."""
        if not user:
            user = ctx.message.author

        if user.status is discord.Status.online:
            status = "<:online:314134671791357954>"
        elif user.status is discord.Status.idle:
            status = "<:idle:314134671690563586>"
        elif user.status is discord.Status.do_not_disturb:
            status = "<:do_not_disturb:314134672101867520>"
        # elif member.status is discord.Status.streaming:
        #     status = "<:streaming:327122815394381824>"
        else:
            status = "<:offline:314134672126771200>"

        embed = discord.Embed(title=f"User Info for {status}{user}",
                              colour=user.colour)

        avatar_url = user.avatar_url.replace("webp", "png")
        embed.set_thumbnail(url=avatar_url.replace("size=1024", "size=256"))
        embed.set_footer(text=("Account Created at " + user.created_at.strftime("%A %d %B %Y, %H:%M:%S")))
        embed.set_author(name=f"{user}", url=avatar_url, icon_url=avatar_url)
    
        if user.game:
            embed.add_field(name="Status", value=f"**Playing** {user.game.name}")
        embed.add_field(name="ID", value=user.id)
        embed.add_field(name="Member Since ",
                        value=user.joined_at.strftime("%A %d %B %Y, %H:%M:%S"))
    
        roleString = ""
        for role in user.roles:
            if role.name == "@everyone":
                continue
            roleString += role.name + ", "
        roleString = roleString[:-2]
    
        embed.add_field(name="Roles", value=roleString)

        if user.avatar_url:
            embed.set_image(url=user.avatar_url)
            embed.add_field(name="Avatar URL", value=user.avatar_url)
    
        await ctx.send(embed=embed)
    
    @commands.command()
    async def info(self, ctx):
        """Shows the bot's info."""
        server=ctx.message.guild
        membObj=server.me
        embed = discord.Embed(title=f"Information on {self.bot.user.name}",
                              colour=0xfe8600)
        embed.set_image(url=self.bot.user.avatar_url)
        embed.set_footer(text=("Bot created at " + self.bot.user.created_at.strftime("%A %d %B %Y, %H:%M:%S")))
    
        embed.add_field(name="ID", value=self.bot.user.id)
        embed.add_field(name="Member Since ",
                        value=membObj.joined_at.strftime("%A %d %B %Y, %H:%M:%S"))
        roleString = ""
        for role in membObj.roles:
            if role.name == "@everyone":
                continue
            roleString += role.name + ", "
        roleString = roleString[:-2]
    
        embed.add_field(name="Roles", value=roleString)

        if self.bot.user.avatar_url:
            embed.set_image(url=self.bot.user.avatar_url)
            embed.add_field(name="Avatar URL", value=self.bot.user.avatar_url)

        embed.add_field(name="Owner", value=BotIDs.dev_name)
        embed.add_field(name="Prefixes", value=Prefix.Prefix("`") + " `@OG_Bot`")
        embed.add_field(name="GitHub", value="https://github.com/OrangutanGaming/OG_Bot")
        embed.add_field(name="OAuth2", value=BotIDs.URL)
        embed.add_field(name="Server Count", value=str(len(self.bot.guilds)))
        embed.add_field(name="CPU%", value=psutil.cpu_percent())
        embed.add_field(name="RAM%", value=psutil.virtual_memory().percent)
        pyVersion = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        embed.add_field(name="Python Version", value=f"{pyVersion} <:python:326405606225346560>")
        embed.add_field(name="Discord.py Version", value=f"{discord.__version__} discord.py")
    
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["sinfo"], no_pm=True)
    async def serverinfo(self, ctx):
        """Shows the current server's info."""
        server = ctx.message.guild

        embed = discord.Embed(title=f"Server Info for {server.name}", colour=0xffa500)

        embed.set_image(url=server.icon_url)
        embed.set_footer(text=("Server created at " + server.created_at.strftime("%A %d %B %Y, %H:%M:%S")))

        embed.add_field(name="ID", value=server.id)
        embed.add_field(name="Role Count", value=str(len(server.roles)-1))
        embed.add_field(name="Owner", value=f"{str(server.owner)} <@{server.owner.id}>")
        embed.add_field(name="Region", value=server.region)
        embed.add_field(name="Member Count", value=server.member_count)
        botCount = str(len([member.name for member in ctx.guild.members if member.bot]))
        embed.add_field(name="Bot Count", value=botCount)
        embed.add_field(name="Text Channel Count", value=str(len(server.text_channels)))
        embed.add_field(name="Voice Channel Count", value=str(len(server.voice_channels)))
        embed.add_field(name="Total Channel Count", value=str(len(server.channels)))
        embed.add_field(name="Default Channel", value="{0.mention} ({0.name})".format(server.default_channel))
        if server.icon_url:
            embed.set_image(url=server.icon_url)
            embed.add_field(name="Avatar URL", value=server.icon_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))