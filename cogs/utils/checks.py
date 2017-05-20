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

def has_permissions_owner_check(ctx, perms):
    msg = ctx.message
    if is_owner_check(msg):
        return True

    channel = msg.channel
    author = msg.author
    resolved = channel.permissions_for(author)
    return all(getattr(resolved, name, None) == value for name, value in perms.items())

def has_permissions_owner(**perms):
    def predicate(ctx):
        return has_permissions_owner_check(ctx, perms)

    return commands.check(predicate)

def has_permissions(**perms):
    def predicate(ctx):
        msg = ctx.message
        ch = msg.channel
        permissions = ch.permissions_for(msg.author)
        return all(getattr(permissions, perm, None) == value for perm, value in perms.items())

    return commands.check(predicate)

# def has_permissions_owner(**perms):
#     if is_owner_check(ctx)
#
#     def predicate(ctx):
#         msg = ctx.message
#         ch = msg.channel
#         permissions = ch.permissions_for(msg.author)
#         return all(getattr(permissions, perm, None) == value for perm, value in perms.items())
#
#     return commands.check(predicate)