#!/usr/bin/python3
# -*- coding: utf-8 -*-
import discord
import os
import re
from wow import *


DISCORD_BOT_TOKEN = str(os.getenv('DISORD_BOT_TOKEN'))
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
            data = """
                    `Character Name` | `%s`
                    `Realm` | `%s`
                    `Equipped Item Level` | `%s`

                    `Keystone Master` | `%s`
                    `Keystone Conqueror` | `%s`

                    `Emerald Nightmare Normal` | `%s/%s`
                    `Emerald Nightmare Heroic` | `%s/%s`
                    `Emerald Nightmare Mythic` | `%s/%s`
                    `Emerald Nightmare AOTC` | `%s`

                    `Trial of Valor Normal` | `%s/%s`
                    `Trial of Valor Heroic` | `%s/%s`
                    `Trial of Valor Mythic` | `%s/%s`
                    `Trial of Valor AOTC` | `%s`

                    `The Nighthold Normal` | `%s/%s`
                    `The Nighthold Heroic` | `%s/%s`
                    `The Nighthold Mythic` | `%s/%s`
                    `The Nighthold AOTC` | `%s`

                    %s""" % (info['name'], info['realm'], info['ilvl'], info['keystone_master'], \
                    info['keystone_conqueror'], info['emerald_nightmare']['normal'], info['emerald_nightmare']['bosses'], info['emerald_nightmare']['heroic'], info['emerald_nightmare']['bosses'], \
                    info['emerald_nightmare']['mythic'], info['emerald_nightmare']['bosses'], info['aotc_en'], \
                    info['trial_of_valor']['normal'], info['trial_of_valor']['bosses'], info['trial_of_valor']['heroic'], info['trial_of_valor']['bosses'], \
                    info['trial_of_valor']['mythic'], info['trial_of_valor']['bosses'], info['aotc_tov'], \
                    info['the_nighthold']['normal'], info['the_nighthold']['bosses'], info['the_nighthold']['heroic'], info['the_nighthold']['bosses'], \
                    info['the_nighthold']['mythic'], info['the_nighthold']['bosses'], info['aotc_nh'], info['armory'])

            # Uses re to strip white space caused by the string fomratting.
            msg = '%s'.format(message) % re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', data, flags=re.M)

        await client.send_message(message.channel, msg)

client.run(DISCORD_BOT_TOKEN)
