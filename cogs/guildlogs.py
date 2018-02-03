from discord.ext import commands
import discord
import datetime
import BotIDs
import cogs.utils.checks as checks


class GuildLogs():
    def __init__(self, bot):
        self.bot = bot

    async def on_guild_join(self, guild):
        try:
            # Send public log

            embed = discord.Embed(description=f"{self.bot.user.mention} joined the guild {guild.name} ({guild.id})")
            embed.add_field(name="Owner", value=f"{str(guild.owner)} ({guild.owner.id}) <@{guild.owner.id}>")
            embed.set_footer(
                text=("Server joined on " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S")))

            await self.bot.get_channel(315140647764099073).send(embed=embed)

            # Send all the server's info

            server = guild
            embed = discord.Embed(title=f"Server Info for {server.name}", colour=0xffa500)

            embed.set_footer(text=("Server created at " + server.created_at.strftime("%A %d %B %Y, %H:%M:%S")))

            embed.add_field(name="ID", value=server.id)
            embed.add_field(name="Role Count", value=str(len(server.roles) - 1))
            embed.add_field(name="Owner", value=f"{str(server.owner)} <@{server.owner.id}>")
            embed.add_field(name="Region", value=server.region)
            embed.add_field(name="Member Count", value=server.member_count)
            botCount = str(len([member.name for member in server.members if member.bot]))
            embed.add_field(name="Bot Count", value=botCount)
            embed.add_field(name="Text Channel Count", value=str(len(server.text_channels)))
            embed.add_field(name="Voice Channel Count", value=str(len(server.voice_channels)))
            embed.add_field(name="Total Channel Count", value=str(len(server.channels)))
            if server.icon_url:
                embed.set_image(url=server.icon_url)
                embed.add_field(name="Avatar URL", value=server.icon_url)

            await self.bot.get_channel(315420015040135178).send(embed=embed)


        except:
            pass

        # Update server count message

        channel = self.bot.get_channel(315428002034876416)
        message = await channel.get_message(315429055602360321)

        embed = discord.Embed(description=f"Current server count of {self.bot.user.mention}")
        embed.add_field(name="Server Count", value=str(len(self.bot.guilds)))
        embed.set_footer(text=("Server count since " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S")))

        await message.edit(embed=embed)

        # Update user count message

        channel = self.bot.get_channel(315428002034876416)
        message = await channel.get_message(319027169848197124)

        embed = discord.Embed(description=f"Current user count of {self.bot.user.mention}")
        embed.add_field(name="User Count", value=str(len(self.bot.users)))
        embed.set_footer(text=("User count since " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S"))
                              + " UTC")

        await message.edit(embed=embed)

    async def on_guild_remove(self, guild):
        embed = discord.Embed(description=f"{self.bot.user.mention} left the guild {guild.name} ({guild.id})")
        embed.add_field(name="Owner", value=f"{str(guild.owner)} ({guild.owner.id}) <@{guild.owner.id}>")
        embed.set_footer(text=("Server left on " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S")))

        await self.bot.get_channel(315140647764099073).send(embed=embed)

        # Update server count message

        channel = self.bot.get_channel(315428002034876416)
        message = await channel.get_message(315429055602360321)

        embed = discord.Embed(description=f"Current server count of {self.bot.user.mention}")
        embed.add_field(name="Server Count", value=str(len(self.bot.guilds)))
        embed.set_footer(text=("Server count since " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S")))

        await message.edit(embed=embed)

        # Update user count message

        channel = self.bot.get_channel(315428002034876416)
        message = await channel.get_message(319027169848197124)

        embed = discord.Embed(description=f"Current user count of {self.bot.user.mention}")
        embed.add_field(name="User Count", value=str(len(self.bot.users)))
        embed.set_footer(text=("User count since " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S"))
                              + " UTC")

        await message.edit(embed=embed)

    @commands.command(hidden=True)
    @checks.is_dev()
    async def servercountsend(self, ctx):
        embed = discord.Embed(description=f"Current server count of {self.bot.user.mention}")
        embed.add_field(name="Server Count", value=str(len(self.bot.guilds)))
        embed.set_footer(text=("Server count since " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S")))

        await self.bot.get_channel(315428002034876416).send(embed=embed)
        await ctx.send(":thumbsup:")

def setup(bot):
    bot.add_cog(GuildLogs(bot))




