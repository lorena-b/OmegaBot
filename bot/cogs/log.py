"""DISPLAY JOIN/LEAVE MESSAGES + MANAGE BOT STATUS"""
import discord
from discord.ext import commands


class Log(commands.Cog):
    def __init__(self, client,):
        self.client = client

    # BOT JOIN
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game("!help"))
        print(f'{self.client.user} has connected to Discord!')

    # USER JOIN
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.mention}!')

    # USER LEAVE
    async def on_member_leave(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'{member.mention} has left.')


def setup(client):
    client.add_cog(Log(client))
