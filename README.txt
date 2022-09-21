INFO for Discord.py 2.0

slashcmdbot-2 is an example code to make slash commands in discord.py bots in discord.py 2.0. This shows the non-complicated way. For Non-cog bots.
Although I quit making Discord bots, I might as well provide this for everyone since the intent is being enforced.

To create a slash command in discord.py 2.0 without cogs, use the example to get the on_ready event to sync the commands.
Not first, @client.command() is now @client.tree.command. Name and description format is same like discord.py 1.7.x
Now to send messages, await ctx.send is changed to interaction.response.send_message

==================================================================================
INFO for Discord.py 1.7.x

slashcmdbot-1.7.x.py is an example code to make Slash Commands in discord.py bots as the Message Content intent is being enforced.
I am providing the simple way. (For discord.py 1.7.x
Although I quit making Discord bots, I might as well provide this for everyone since the intent is being enforced.

PACKAGES REQUIRED (Discord.py v1.7.x version)
- discord.py
- discord-py-slash-command

Here is my video if you are not bothered to read the steps or confused on a step: https://www.youtube.com/watch?v=XvcmtE6yJLc

STEPS TO MAKE SLASH COMMANDS ON YOUR BOT:
1. Install the discord-py-slash-command package
2. Import the following: from discord_slash import SlashCommand
3. Add slash = SlashCommand(client, sync_commands=True) where we have client = commands.Bot(command_prefix= commands.when_mentioned_or('!')) and client.remove_command("help") at
(normally below the imports)

4. To make a slash command, @client.command() will be replaced with @slash.slash(name="cmdname", description='cmd description')
5. If you have regular commands with the same name with async def cmdname(ctx), then do async def _cmdname(ctx): for that part
- When you pull up /, the cmd name would be the name="cmdname" and the description would be description='cmd description'
- You can see this example in my video.
6. Error handling would be the same as with the @client.command()

See example in the slashcmdbot-1.7.x.py file

DISCLAIMER: THIS MAY NOT 100% WORK ALL THE TIME. USE AT YOUR OWN RISK!