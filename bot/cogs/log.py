import discord
from discord.ext import commands


class Log(commands.Cog):
    def __init__(self, client):
        self.client = client

    #BOT JOIN 
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status = discord.Status.online, activity = discord.Game("!help"))
        print(f'{self.client.user} has connected to Discord!')

    #USER JOIN
    @commands.Cog.listener()
    async def on_member_join(self, member):
        


    #USER LEAVE

def setup(client):
    client.add_cog(Log(client))
