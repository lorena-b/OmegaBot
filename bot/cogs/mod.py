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

    # unban

    # banlist 

    # kick

    # mute

    # unmute


def setup(client):
    client.add_cog(Mod(client))
