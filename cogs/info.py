from discord.ext import commands
import discord
import BotIDs
import cogs.utils.prefix as Prefix

class Info():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["uinfo"], no_pm=True)
    async def userinfo(self, ctx, member: discord.Member = None):
        """Shows the info on a user."""
        if not member:
            member = ctx.message.author
    
        embed = discord.Embed(title="User Info for {}".format(member),
                              colour=member.colour)
    
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=("Account Created at " + member.created_at.strftime("%A %d %B %Y, %H:%M:%S")))
    
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Member Since ",
                        value=member.joined_at.strftime("%A %d %B %Y, %H:%M:%S"))
    
        roleString = ""
        for role in member.roles:
            if role.name == "@everyone":
                continue
            roleString += role.name + ", "
        roleString = roleString[:-2]
    
        embed.add_field(name="Roles", value=roleString)

        if member.avatar_url:
            embed.set_image(url=member.avatar_url)
            embed.add_field(name="Avatar URL", value=member.avatar_url)
    
        await ctx.send(embed=embed)
    
    @commands.command()
    async def info(self, ctx):
        """Shows the bot's info."""
        server=ctx.message.guild
        membObj=server.me
        embed = discord.Embed(title="Information on {}".format(self.bot.user.name),
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

        embed.add_field(name="Owner", value="OGaming#7135")
        embed.add_field(name="Prefixes", value=Prefix.Prefix("`") + " `@OG_Bot`")
        embed.add_field(name="GitHub", value="https://github.com/OrangutanGaming/OG_Bot")
        embed.add_field(name="OAuth2", value=BotIDs.URL)
        embed.add_field(name="Server Count", value=str(len(self.bot.guilds)))
    
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["sinfo"], no_pm=True)
    async def serverinfo(self, ctx):
        """Shows the current server's info."""
        server = ctx.message.guild

        embed = discord.Embed(title="Server Info for {}".format(server.name), colour=0xffa500)

        embed.set_image(url=server.icon_url)
        embed.set_footer(text=("Server created at " + server.created_at.strftime("%A %d %B %Y, %H:%M:%S")))

        embed.add_field(name="ID", value=server.id)

        def Roles(server):
            counter = 0
            for role in server.roles:
                if role.name == "@everyone":
                    continue
                counter+=1
            return str(counter)

        def Bots(server):
            count=0
            for member in server.members:
                if member.bot:
                    count+=1
                else:
                    continue

            return str(count)

        embed.add_field(name="Roles", value=Roles(server))
        embed.add_field(name="Owner", value=server.owner)
        embed.add_field(name="Region", value=server.region)
        embed.add_field(name="Member Count", value=server.member_count)
        embed.add_field(name="Bot Count", value=Bots(server))
        embed.add_field(name="Text Channel Count", value=str(len(server.text_channels)))
        embed.add_field(name="Voice Channel Count", value=str(len(server.voice_channels)))
        embed.add_field(name="Total Channel Count", value=str(len(server.channels)))
        embed.add_field(name="Default Channel", value=server.default_channel.name)
        if server.icon_url:
            embed.set_image(url=server.icon_url)
            embed.add_field(name="Avatar URL", value=server.icon_url)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))