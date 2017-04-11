import sqlite3
connect = sqlite3.connect("codes.db")
c = connect.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS codes"
#           "(platform text, code text, id text)")

# c.execute("INSERT INTO codes VALUES ('PC', 'code', 'NULL')")

# connect.commit()

from discord.ext import commands

class Glyph():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def glyph(self, ctx, platform):
        if not ctx.guild.id == 130805968681304064:
            return
        if not platform:
            tmp = await ctx.send(self.bot.blank + "State your platform: `PC`, `XBox` or `PS4`")
            return

        if platform.lower() == "pc":
            platform = "PC"
        elif platform.lower() == "xbox":
            platform = "XBox"
        elif platform.lower() == "ps4":
            platform = "PS4"
        else:
            tmp = await ctx.send(self.bot.blank + "State your platform: `PC`, `XBox` or `PS4`")
            return

        c.execute("SELECT code FROM codes WHERE id IS NULL AND platform={}".format(platform))
        if not c.fetchall():
            tmp = await ctx.author.send("There are no more {} codes.".format(platform))
        code = c.fetchall()
        c.execute("INSERT INTO codes (id) VALUES (?)", (ctx.author.id))
        connect.commit()
        c.close()
        connect.close()

        ctx.author.send("Your {} code is {}".format(platform, code))
        return

def setup(bot):
    bot.add_cog(Glyph(bot))