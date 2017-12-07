import discord
from discord.ext import commands
import BotIDs
import logging
import traceback
import cogs.utils.prefix as Prefixes
import cogs.utils.checks as checks
# import rethinkdb as r
import datetime
import os
from raven import Client
from raven_aiohttp import AioHttpTransport
import sys

sentryClient = Client(BotIDs.sentryDSN, transport=AioHttpTransport)

# r.connect("localhost", 28015).repl()

description = f"A bot built by Orangutan Gaming ({BotIDs.dev_name}, 150750980097441792). " \
              f"Discord Support link: https://discord.gg/duRB6Qg"

prefixes = Prefixes.prefixes
bot = commands.Bot(command_prefix=commands.when_mentioned_or(*prefixes), description=description)
# bot.remove_command("help")
bot.blank = "\u200B"
bot.config = BotIDs.settings
bot.prefixes = prefixes
bot.ready = False
bot.uptime = datetime.datetime.utcnow()

logger = logging.getLogger("discord")
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

startup_extensions = ["cogs.clear",
                      "cogs.dev",
                      "cogs.info",
                      "cogs.count",
                      "cogs.welcome",
                      "cogs.help",
                      "cogs.fun",
                      "cogs.utils.stats",
                      "cogs.eval",
                      "cogs.edit",
                      "cogs.messages",
                      "cogs.guildlogs",
                      "cogs.moderation",
                      "cogs.glyphpost"
                      ]

@bot.event
async def on_ready():
    gamename="with OG|o!help"
    await bot.change_presence(game=discord.Game(name=gamename))
    print("Logged in as")
    print("Name: " + str(bot.user))
    print("ID: " + str(bot.user.id))
    print("Playing", gamename)
    print(BotIDs.URL)
    print("Prefixes: " + Prefixes.Prefix('"'))
    bot.ready = True

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if not bot.ready:
        for prefix in prefixes:
            if message.content.startswith(prefix):
                await message.channel.send("I am still loading.")
                return
    # if message.content.endswith == "":
    #     await message.channel.send("What?")
    #     return
    # else:
    #     if message.content.startswith("\o\\"):
    #         await message.channel.send("/o/")
    #         return
    #     elif message.content.startswith("/o/"):
    #         await message.channel.send("\o\\")
    #         return
    #     elif message.content.startswith("\o/"):
    #         await message.channel.send("\o/")
    #         return
    await bot.process_commands(message)

@bot.command(hidden=True)
@checks.is_dev()
async def load(ctx, extension_name: str):
    """Loads a module."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send(bot.blank + "```py\n{}: {}\n```".format(type(e).__name__, str(e)), delete_after=3)
        return
    await ctx.send(bot.blank + "{} loaded.".format(extension_name), delete_after=3)

@bot.command(hidden=True)
@checks.is_dev()
async def unload(ctx, extension_name: str):
    """Unloads a module."""
    bot.unload_extension(extension_name)
    await ctx.send(bot.blank + "{} unloaded.".format(extension_name), delete_after=3)

@bot.command(name="reload", hidden=True)
@checks.is_dev()
async def _reload(ctx, *, module: str):
    """Reloads a module."""
    try:
        bot.unload_extension(module)
        bot.load_extension(module)
    except Exception as e:
        await ctx.send("{}: {}".format(type(e).__name__, e))
    else:
        await ctx.send(":thumbsup:")

@bot.command(hidden=True)
@checks.is_dev()
async def shutdown(ctx):
    """Shutdown"""
    try:
        await ctx.send("System Shutting down.")
        await bot.logout()
        await bot.close()
    except:
        await ctx.send("Error!")

@bot.command()
async def join(ctx):
    """Shows info on how to add the bot."""
    options=["This bot is currently a work in progress. It is not public yet. If you're interested in "
             f"helping with testing or have any ideas, PM {BotIDs.dev_name}",
             "Anyone with the permission `Manage server` can add me to a server using the following link: " + BotIDs.URL]
    DServer="https://discord.gg/duRB6Qg"
    await ctx.send(options[1]+"\nYou can also join the Discord channel at: " + DServer + "\nYou can also help "
                    "contribute to me at: "+BotIDs.GitHub)
    await ctx.send(bot.blank + "\nYou can also help support me at " + BotIDs.Patreon)

@bot.command()
async def support(ctx):
    """Shows the Patreon page link."""
    await ctx.send(bot.blank + "You can help support the bot with " + BotIDs.Patreon)

if BotIDs.GitHub:
    @bot.command()
    async def github(ctx):
        """Shows the GitHub link."""
        await ctx.send(bot.blank + "You can join the GitHub using {}".format(BotIDs.GitHub))
        return

# @bot.command()
# async def quote(channel, msgID):
#    async for message in bot.logs_from(channel):
#        if message.id == msgID:
#            quote = message
#            embed = discord.Embed(description=quote.content)
#            embed.set_author(name=quote.author.name, icon_url=quote.author.avatar_url)
#            embed.timestamp = quote.created_at
#            await ctx.message.delete()
#            await ctx.send(embed=embed)
#        if not quote:
#            continue

#
# @bot.command()
# @commands.has_permissions(manage_guild=True)
# async def giveaway(action):
#     if action == "enable":
#         r.db("OG_Bot")r.table("giveaway").insert([])
#     elif action == "disable":
#         #
#     elif action == "clear":
#         #

# @bot.command()
# async def enter():

# TODO RethinkDB

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))

@bot.event
async def on_command_error(ctx, error):
    blacklist = [commands.errors.CommandNotFound,
                 commands.MissingRequiredArgument,
                 commands.BadArgument,
                 commands.CheckFailure
                 ]

    # if type(error) not in blacklist:
    #     sentryClient.captureException()
        # try:
        #     print(f"{ctx.guild.name}, Owner: {str(ctx.guild.owner)}, "
        #           f"Author: {str(ctx.message.author)}, Command: {ctx.message.content}")
        # except:
        #     try:
        #         print(f"PM - Command: {ctx.message.content}")
        #     except:
        #         print("Error")

    if isinstance(error, commands.MissingRequiredArgument):
        try: await ctx.channel.send(error)
        except: return
    elif isinstance(error, commands.errors.CommandNotFound):
        try: await ctx.channel.send("`{}` is not a valid command".format(ctx.invoked_with))
        except: return
    elif isinstance(error, commands.errors.CommandInvokeError):
        print(f"In {ctx.command.qualified_name}:", file=sys.stderr)
        traceback.print_tb(error.original.__traceback__)
        print(f"{error}", file=sys.stderr)
    elif isinstance(error, discord.Forbidden):
        try: await ctx.channel.send("I do not have permissions")
        except: return
    elif isinstance(error, commands.errors.BadArgument):
        try: await ctx.channel.send(f"Bad Argument: {error}")
        except: return
    elif isinstance(error, commands.errors.CheckFailure):
        try: await ctx.channel.send(f"You do not have permission to use the command `{ctx.invoked_with}`.")
        except: return
    else:
        print(f"In {ctx.command.qualified_name}:", file=sys.stderr)
        traceback.print_tb(error.__traceback__)
        print(f"{error.__class__.__name__}: {error}", file=sys.stderr)

bot.run(BotIDs.token)
