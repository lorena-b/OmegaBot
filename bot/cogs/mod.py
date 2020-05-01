""" MODERATION COMMANDS """
import discord
from discord.ext import commands


class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    # return client ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Client Ping: {round(self.client.latency * 1000)} ms')

    # ban
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    # unban
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    # banlist
    @commands.command()
    async def banlist(self, ctx):
        banned_users = await ctx.guild.bans()

        if (banned_users != None):
            await ctx.send("BANNED USERS:\n")

            for ban_entry in banned_users:
                user = ban_entry.user
                await ctx.send(f"{user}\n")

        else:
            await ctx.send("There are no banned users.")

    # kick
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    # mute
    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        await member.mute(reason=reason)

    # unmute


def setup(client):
    client.add_cog(Mod(client))
