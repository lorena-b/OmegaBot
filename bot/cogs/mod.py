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
    @commands.has_guild_permissions(ban_members=True, administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    # unban
    @commands.command()
    @commands.has_guild_permissions(ban_members=True, administrator=True)
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
    @commands.has_guild_permissions(ban_members=True, administrator=True)
    async def banlist(self, ctx):
        banned_users = await ctx.guild.bans()

        if banned_users:
            await ctx.send("BANNED USERS:\n")

            for ban_entry in banned_users:
                user = ban_entry.user
                await ctx.send(f"{user}\n")
        else:
            await ctx.send("There are no banned users.")

    # kick
    @commands.command()
    @commands.has_guild_permissions(kick_members=True, administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    # text mute
    @commands.command()
    @commands.has_guild_permissions(mute_members=True, administrator=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):

        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if not role:  # if role doesn't already exist, create it
            muted = await ctx.guild.create_role(name="Muted")

            for channel in ctx.guild.channels:  # removes permission to send in all the channels
                await channel.set_permissions(muted, send_messages=False)

        await member.add_roles(muted)
        if (reason == None):
            await ctx.send(f'{member.mention} has been muted')
        else:
            await ctx.send(f'{member.mention} has been muted for reason: {reason}')

    # text unmute
    @commands.command()
    @commands.has_guild_permissions(mute_members=True, administrator=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        await ctx.send(f'{member.mention} has been unmuted.')


def setup(client):
    client.add_cog(Mod(client))
