#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import discord
import re
import time
from wow import *
from util import *
from settings import *


client = discord.Client()

@client.event
async def on_message(message):
    """Listens for specific user messages."""
    bot_error = 'Could not find a player with that name, realm or region combination. Type `!armory help` for more a list of valid commands.'

    # If the author is the bot do nothing.
    if message.author == client.user:
        return

    # If the author is not the bot, and the message starts with '!armory pve', display the characters PVE data sheet.
    if message.content.startswith('!armory pve'):
        # Sends the query to be split via a utility function. Accepts either a character/realm, or an armory link.
        split = split_query(message.content, 'pve')

        # Assigns the 3rd index in the split to the region
        region = split[3]

        # Sends the returned data to the character_info function to build a character sheet.
        info = character_info(split[0], split[1], split[2], region)

        # If the returned data is an empty string send a message saying the player/realm/region couldn't be found.
        if info == '':
            msg = bot_error.format(message)
            await client.send_message(message.channel, msg)

        # Otherwise respond with an incredibly long string of data holding all of the info.
        else:
            # Current time (Used for cache busting character thumbnails).
            epoch_time = int(time.time())

            # Format the AOTC/CE strings if they exist.
            en_feat = ''
            tov_feat = ''
            nh_feat = ''
            tos_feat = ''
            atbt_feat = ''

            if info['en_feat'] != '':
                en_feat = '**`%s`**' % (info['en_feat'])

            if info['tov_feat'] != '':
                tov_feat = '**`%s`**' % (info['tov_feat'])

            if info['nh_feat'] != '':
                nh_feat = '**`%s`**' % (info['nh_feat'])

            if info['tos_feat'] != '':
                tos_feat = '**`%s`**' % (info['tos_feat'])

            if info['atbt_feat'] != '':
                atbt_feat = '**`%s`**' % (info['atbt_feat'])

            msg = discord.Embed(
                title="%s" % (info['name']),
                colour=discord.Colour(info['class_colour']),
                url="%s" % (info['armory']),
                description="%s %s %s %s" % (
                    info['level'], info['faction'], info['spec'], info['class_type']))
            msg.set_thumbnail(
                url="https://render-%s.worldofwarcraft.com/character/%s?_%s" % (
                    region, info['thumb'], epoch_time))
            msg.set_footer(
                text="!armory help | Feedback: https://github.com/JamesIves/discord-wow-armory-bot/issues",
                icon_url="https://raw.githubusercontent.com/JamesIves/discord-wow-armory-bot/master/assets/icon.png")
            msg.add_field(
                name="Character",
                value="**`Name`:** `%s`\n**`Realm`:** `%s (%s)`\n**`Item Level`:** `%s`\n**`Artifact Challenge`:** `%s`" % (
                    info['name'], info['realm'], region.upper(), info['ilvl'], info['challenging_look']),
                inline=True)
            msg.add_field(
                name="Keystone Achievements",
                value="**`Master(+15)`:** `%s`\n**`Conqueror(+10)`:** `%s` \n**`Challenger(+5)`:** `%s`" % (
                    info['keystone_master'], info['keystone_conqueror'],
                    info['keystone_challenger']),
                inline=True)
            msg.add_field(
                name="Emerald Nightmare",
                value="**`Normal`:** `%s/%s`\n**`Heroic`:** `%s/%s`\n**`Mythic`:** `%s/%s`\n%s" % (
                    info['emerald_nightmare']['normal'], info['emerald_nightmare']['bosses'],
                    info['emerald_nightmare']['heroic'], info['emerald_nightmare']['bosses'],
                    info['emerald_nightmare']['mythic'], info['emerald_nightmare']['bosses'],
                    en_feat),
                inline=True)
            msg.add_field(
                name="Trial of Valor",
                value="**`Normal`:** `%s/%s`\n**`Heroic`:** `%s/%s`\n**`Mythic`:** `%s/%s`\n%s" % (
                    info['trial_of_valor']['normal'], info['trial_of_valor']['bosses'],
                    info['trial_of_valor']['heroic'], info['trial_of_valor']['bosses'],
                    info['trial_of_valor']['mythic'], info['trial_of_valor']['bosses'],
                    tov_feat),
                inline=True)
            msg.add_field(
                name="The Nighthold",
                value="**`Normal`:** `%s/%s`\n**`Heroic`:** `%s/%s`\n**`Mythic`:** `%s/%s`\n%s" % (
                    info['the_nighthold']['normal'], info['the_nighthold']['bosses'],
                    info['the_nighthold']['heroic'], info['the_nighthold']['bosses'],
                    info['the_nighthold']['mythic'], info['the_nighthold']['bosses'],
                    nh_feat),
                inline=True)
            msg.add_field(
                name="Tomb of Sargeras",
                value="**`Normal`:** `%s/%s`\n**`Heroic`:** `%s/%s`\n**`Mythic`:** `%s/%s`\n%s" % (
                    info['tomb_of_sargeras']['normal'], info['tomb_of_sargeras']['bosses'],
                    info['tomb_of_sargeras']['heroic'], info['tomb_of_sargeras']['bosses'],
                    info['tomb_of_sargeras']['mythic'], info['tomb_of_sargeras']['bosses'],
                    tos_feat),
                inline=True)
            msg.add_field(
                name="Antorus, The Burning Throne",
                value="**`Normal`:** `%s/%s`\n**`Heroic`:** `%s/%s`\n**`Mythic`:** `%s/%s`\n%s" % (
                    info['antorus_the_burning_throne']['normal'], info['antorus_the_burning_throne']['bosses'],
                    info['antorus_the_burning_throne']['heroic'], info['antorus_the_burning_throne']['bosses'],
                    info['antorus_the_burning_throne']['mythic'], info['antorus_the_burning_throne']['bosses'],
                    atbt_feat),
                inline=True)

            await client.send_message(message.channel, embed=msg)


    # Same as before, except this time it's building data for PVP.
    if message.content.startswith('!armory pvp'):
        split = split_query(message.content, 'pvp')
        region = split[3]
        info = character_info(split[0], split[1], split[2], split[3])

        if info == '':
            msg = bot_error.format(message)
            await client.send_message(message.channel, msg)

        else:

            msg = discord.Embed(
                title="%s" % (info['name']),
                colour=discord.Colour(info['class_colour']),
                url="%s" % (info['armory']),
                description="%s %s %s %s" % (
                    info['level'], info['faction'], info['spec'], info['class_type']))
            msg.set_thumbnail(
                url="https://render-%s.worldofwarcraft.com/character/%s" % (
                    region, info['thumb']))
            msg.set_footer(
                text="!armory help | Feedback: https://github.com/JamesIves/discord-wow-armory-bot/issues",
                icon_url="https://github.com/JamesIves/discord-wow-armory-bot/blob/master/assets/icon.png?raw=true")
            msg.add_field(
                name="Character",
                value="**`Name`:** `%s`\n**`Realm`:** `%s (%s)`\n**`Battlegroup`:** `%s`\n**`Item Level`:** `%s`" % (
                    info['name'], info['realm'], region.upper(), info['battlegroup'], info['ilvl']),
                inline=True)
            msg.add_field(
                name="Arena Achievements",
                value="**`Challenger`:** `%s`\n**`Rival`:** `%s`\n**`Duelist`:** `%s`\n**`Gladiator`:** `%s`" % (
                    info['arena_challenger'], info['arena_rival'],
                    info['arena_duelist'], info['arena_gladiator']),
                inline=True)
            msg.add_field(
                name="RBG Achievements",
                value="**`%s`:** `%s`\n**`%s`:** `%s`\n**`%s`:** `%s`" % (
                    info['rbg_2400_name'], info['rbg_2400'],
                    info['rbg_2000_name'], info['rbg_2000'],
                    info['rbg_1500_name'], info['rbg_1500']),
                inline=True)
            msg.add_field(
                name="Rated 2v2",
                value="**`Rating`:** `%s`" % (
                    info['2v2']),
                inline=True)
            msg.add_field(
                name="Rated 3v3",
                value="**`Rating`:** `%s`" % (
                    info['3v3']),
                inline=True)
            msg.add_field(
                name="Rated Battlegrounds",
                value="**`Rating`:** `%s`" % (
                    info['rbg']),
                inline=True)
            msg.add_field(
                name="2v2 Skirmish",
                value="**`Rating`:** `%s`" % (
                    info['2v2s']),
                inline=True)
            msg.add_field(
                name="Lifetime Honorable Kills",
                value="**`Rating`:** `%s`" % (
                    info['kills']),
                inline=True)

            await client.send_message(message.channel, embed=msg)


    # Display a list of available commands and a set of credits.
    if message.content.startswith('!armory help'):
        msg = """The following commands can be entered:
            ```
            # Displays a players PVE progression, dungeon kills, keystone achievements, etc.
            !armory pve <name> <realm>
            !armory pve <armory-link>

            # Displays a players PVP progression, arena ratings, honorable kills, etc.
            !armory pvp <name> <realm>
            !armory pvp <armory-link>

            # You can also provide an optional region to each query to display players from other WoW regions outside of the bot default, for example EU, US, etc.
            !armory pve <name> <realm> <region>
            !armory pvp <armory-link> <region>

            ```
            • Bot created by James Ives (jamesives.co.uk)
            • Feedback, Issues and Source: https://github.com/JamesIves/discord-wow-armory-bot/issues
            """

        msg = '%s'.format(message) % re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', msg, flags=re.M)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    if WOW_API_KEY == '':
        print('Missing World of Warcraft API key. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')

    if WOW_REGION == '':
        print('Missing World of Warcraft player region. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')

    if LOCALE == '':
        print('Missing locale. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')

    if DISCORD_BOT_TOKEN == '':
        print('Missing Discord bot token. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')

    else:
        print('Launch Succesful! The bot is now listening for commands...')


client.run(DISCORD_BOT_TOKEN)
