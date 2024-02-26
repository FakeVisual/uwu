import requests
import json
import inspect
import sys
import os
from colorama import Fore, Style, just_fix_windows_console
from keep_alive import keep_alive
import discord
from discord import app_commands, Intents, Client, Interaction
print("wasssssssssssssup")


class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        """ This is called when the bot boots, to setup the global commands """
        await self.tree.sync()


# Variable to store the bot class and interact with it
# Since this is a simple bot to run 1 command over slash commands
# We then do not need any intents to listen to events
client = FunnyBadge(intents=Intents.none())


@client.event
async def on_ready():
    """
    This is called when the bot is ready and has a connection with Discord
    It also prints out the bot's invite URL that automatically uses your
    Client ID to make sure you invite the correct bot with correct scopes.
    """
    if not client.user:
        raise RuntimeError("on_ready() somehow got called before Client.user was set!")

    print(inspect.cleandoc(f"""
        Logged in as {client.user} (ID: {client.user.id})

        Use this URL to invite {client.user} to your server:
        {Fore.LIGHTBLUE_EX}https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot{Fore.RESET}
    """), end="\n\n")


@client.tree.command()
async def hello(interaction: Interaction):
    """ Says hello or something """
    # Responds in the console that the command has been ran
    print(f"> {Style.BRIGHT}{interaction.user}{Style.RESET_ALL} used the command.")

    # Then responds in the channel with this message
    await interaction.response.send_message(inspect.cleandoc(f"""
        Hi **{interaction.user}**, thank you for saying hello to me.

        > __**Where's my badge?**__
        > Eligibility for the badge is checked by Discord in intervals,
        > at this moment in time, 24 hours is the recommended time to wait before trying.

        > __**It's been 24 hours, now how do I get the badge?**__
        > If it's already been 24 hours, you can head to
        > https://discord.com/developers/active-developer and fill out the 'form' there.

        > __**Active Developer Badge Updates**__
        > Updates regarding the Active Developer badge can be found in the
        > Discord Developers server -> https://discord.gg/discord-developers - in the #active-dev-badge channel.
    """))

keep_alive()
client.run(token)
