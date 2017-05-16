#!/usr/bin/python3
# -*- coding: utf-8 -*-
import discord
import os
import re
from wow import *


DISCORD_BOT_TOKEN = str(os.environ.get('DISCORD_BOT_TOKEN'))
client = discord.Client()


@client.event
async def on_message(message):
    """Listens for specific user messages."""

    # If the author is the bot do nothing.
    if message.author == client.user:
        return

    # If it's not the bot and the message starts with '!armory' process it.
    if message.content.startswith('!armory'):
        # Splits up the message, requires the user to type their message as '!wow Jimo burning-legion'.
        # Sends the second word (name) and third word (realm) to the characterInfo function to build a character sheet.
        split = message.content.split(" ")
        info = characterInfo(split[1], split[2])

        # If the returned data is an empty string send a message saying the player/realm couldn't be found.
        if info == '':
            msg = 'Could not find a player with that name/realm combination.'.format(message)

        # Otherwise respond with an incredibly long string of data holding all of the info.
        else:
            msg=discord.Embed(title="%s", url='%s', description="%s, Equipped Item Level %s") % (info['name'], info['armory'], info['realm'], info['ilvl'])
            msg.set_thumbnail(url='https://render-%s.worldofwarcraft.com/character/%s') % (WOW_REGION, info['thumbnail'])
            msg.add_field(name="Keystone Master", value="%s", inline=False) % (info['keystone_master'])
            msg.add_field(name="Keystone Conqueror", value="%s", inline=False) % (info['keystone_conqueror'])
            msg.add_field(name="EN Normal", value="%s", inline=True) % (info['emerald_nightmare']['normal'])
            msg.add_field(name="EN Heroic", value="%s", inline=True) % (info['emerald_nightmare']['heroic'])
            msg.add_field(name="EN Mythic", value="%s", inline=True) % (info['emerald_nightmare']['mythic'])
            msg.add_field(name="EN AOTC", value="%s", inline=True) % (info['aotc_en'])
            msg.add_field(name="TOV Normal", value="%s", inline=True) % (info['trial_of_valor']['normal'])
            msg.add_field(name="TOV Heroic", value="%s", inline=True) % (info['trial_of_valor']['heroic'])
            msg.add_field(name="TOV Mythic", value="%s", inline=True) % (info['trial_of_valor']['mythic'])
            msg.add_field(name="TOV AOTC", value="%s", inline=True) % (info['aotc_tov'])
            msg.add_field(name="NH Normal", value="%s", inline=True) % (info['the_nighthold']['normal'])
            msg.add_field(name="NH Heroic", value="%s", inline=True) % (info['the_nighthold']['heroic'])
            msg.add_field(name="NH Mythic", value="%s", inline=True) % (info['the_nighthold']['mythic'])
            msg.add_field(name="NH AOTC", value="%s", inline=True) % (info['aotc_nh'])
            await self.bot.say(embed=embed)

        await client.send_message(message.channel, msg)

client.run(DISCORD_BOT_TOKEN)
