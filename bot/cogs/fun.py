"""GAME COMMANDS"""
import discord
from discord.ext import commands
import random


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #simple 8ball game 
    @commands.command(aliases=['8ball'])
    async def ball(self, ctx, *, arg):
        responses = [

            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don’t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'Yes – definitely.',
            'You may rely on it',

        ]

        await ctx.send(random.choice(responses))


def setup(client):
    client.add_cog(Fun(client))
