slashcmdbot.py is an example code to make Slash Commands in discord.py bots as the Message Content intent is being enforced.
I am providing the simple way.

Although I quit making Discord bots, I might as well provide this for everyone since the intent is being enforced.

PACKAGES REQUIRED
- discord
- discord-py-slash-command

NOTES:
- Buttons are not known to work with discord.py yet.

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
6. Error handling would be the same as with the @client.command(



DISCLAIMER: THIS MAY NOT 100% WORK ALL THE TIME. USE AT YOUR OWN RISK!