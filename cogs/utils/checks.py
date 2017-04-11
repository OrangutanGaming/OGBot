from discord.ext import commands
import BotIDs
import discord.utils

def is_owner_check(ctx):
    return ctx.author.id == BotIDs.ownerID

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx))

def is_dev_check(ctx):
    return ctx.author.id == BotIDs.dev_id

def is_dev():
    return commands.check(lambda ctx: is_dev_check(ctx))

def check_permissions(ctx, perms):
    msg = ctx.message
    if is_owner_check(msg):
        return True

    ch = msg.channel
    author = msg.author
    resolved = ch.permissions_for(author)
    return all(getattr(resolved, name, None) == value for name, value in perms.items())