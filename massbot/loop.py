from datetime import datetime
from datetime import timedelta

import discord
from discord.ext import tasks

from .data import load_masstimes


REMIND_HOUR = 20
REMIND_MINUTE = 0


@tasks.loop(minutes=1)
async def reminder_check_loop(guilds: list[discord.Guild]):
    now = datetime.now()
    if now.time().hour != REMIND_HOUR or now.time().minute != REMIND_MINUTE:
        return
    masstimes = load_masstimes()
    for guild in guilds:
        for channel in guild.text_channels:
            try:
                for masstime in masstimes:
                    message = await channel.send(
                        f"{str(masstime)} {(now.date() + timedelta(days=1)).strftime('%b %d')}"
                    )
                    await message.add_reaction("🚗")
                    await message.add_reaction("🚶‍♂️")
            except discord.errors.Forbidden:
                continue
