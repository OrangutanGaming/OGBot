from discord.ext import commands
import cogs.utils.prefix as Prefix

class Help():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def help2(self, ctx):
        await ctx.send(self.bot.blank + "OG_Bot by Orangutan Gaming `(OGaming#7135)`"
                    f"\nPrefixes: `@{self.bot.user.name}`, {Prefix.Prefix('`')}"
                    "\n`<Mandatory Argument>`, `(Optional Argument)` `Alias 1`/`Alias 2` `[Permission Needed]`"
                    "\n`help`: Shows this message"
                    "\n`join`: Shows information on how to add me to your server"
                    "\n`msgcount`/`mcount` (user) (channel): Count how many messages in the channel the command was used "
                    "in or the channel given by the user given. If no user is given, it will use the person who uses the "
                    "command"
                    "\n`amsgcount`/`amcount` (channel): Count how many messages in the channel given. If no channel was"
                    "given, will use the channel the command was used in"
                    "\n`recent`/`recents`/`last` (user) (channel): Quotes the most recent message from the user and channel given."
                    "If no user is given, it will use the user using the command and if no channel is given it will use"
                    "the channel the command was used in."
                    "\n`userinfo` (user) gets the userinfo of the user given. If no user is given, it will use the"
                    "user using the command"
                    "\n`info`/`uinfo`: Displays Bot Info"
                    #"\n`botclear`/`bclear` (amount) [Manage Messages]: Deletes the amount of messages given by me in the "
                    #"current channel. Default: 100"
                    "\n`clear`/`del`/`delete`/`wipe` (amount) [Manage Messages]: Deletes the amount of messages given in "
                    "the current channel. Default: 100"
                    "\n`charinfo` <Emoji>: Gives the info for an emoji"
                    "\n`stickers`: Displays all the available stickers"
                    "\n`github`: Displays GitHub Link"
                    "\n`support`: Displays Patreon Link"
                    "\n`prefix`: Displays Prefixes")

    @commands.command()
    async def prefix(self, ctx):
        """Shows the bot's prefixes."""
        await ctx.send(self.bot.blank + f"Prefixes: `@{self.bot.user.name}`, " + Prefix.Prefix('`'))

    @commands.command(aliases=["scount", "guildcount", "gcount"])
    async def servercount(self, ctx):
        """Shows the server count of the bot."""
        await ctx.send(self.bot.blank + "Server Count: " + str(len(self.bot.guilds)))

def setup(bot):
    bot.add_cog(Help(bot))