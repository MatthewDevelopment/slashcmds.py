import discord
from discord.ext import commands
import aiohttp
from contextlib import redirect_stdout

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix= commands.when_mentioned_or('!'), intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"myself be one with the bin"))
    print("BOT IS ONLINE")
    try:
        synced = await client.tree.sync()
        print(f"{len(synced)} Slash Commands successfully Synced")
    except Exception as e:
        print(e)


@client.command()
async def ping(ctx):
    await ctx.send(f'PONG!\nLatency: {round(client.latency * 1000)}ms')

@client.tree.command(name="ping", description='Checks the Latency of the Bot')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("PONG!\nLatency: {round(client.latency * 1000)}ms", ephemeral=True)



client.run("BOTTOKENHERE")
