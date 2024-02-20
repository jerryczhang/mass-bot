from datetime import time

import discord
from discord import app_commands

from .data import append_masstime
from .data import MassTime
from .massbot import command_tree


@command_tree.error
async def on_error(
    interaction: discord.Interaction, error: app_commands.AppCommandError
):
    await interaction.response.send_message(str(error), ephemeral=True)


@command_tree.command()
@app_commands.describe(
    name="Church name",
    hour="Time (hour)",
    minute="Time (minute)",
)
async def add_masstime(
    interaction: discord.Interaction,
    name: str,
    hour: app_commands.Range[int, 0, 23],
    minute: app_commands.Range[int, 0, 59],
):
    """Add a new Mass time"""

    masstime = MassTime(name, time(hour, minute))
    append_masstime(masstime)
    await interaction.response.send_message(f"{str(masstime)} added!")
