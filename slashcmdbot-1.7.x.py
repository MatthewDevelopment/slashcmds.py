import discord
from discord.ext import commands
import aiohttp
from contextlib import redirect_stdout
from discord_slash import SlashCommand

client = commands.Bot(command_prefix= commands.when_mentioned_or('!'))
client.remove_command("help")
slash = SlashCommand(client, sync_commands=True)

@client.command()
async def ping(ctx):
    await ctx.send(f'PONG!\nLatency: {round(client.latency * 1000)}ms')

@slash.slash(name="ping", description='Checks the Latency of the Bot')
async def _ping(ctx):
    await ctx.send(f'PONG!\nLatency: {round(client.latency * 1000)}ms')



client.run("BOTTOKENHERE")
