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
    # Current time (Used for cache busting character thumbnails).
    epoch_time = int(time.time())

    # If the author is the bot do nothing.
    if message.author == client.user:
        return

    if message.content.startswith('!armory token'):
        split = split_query(message.content, 'wow_token')
        region = split[0]
        info = await wow_token_price(region)

        # Returns a message to the channel if there's an error fetching.
        if info == 'not_found':
            msg = GOLD_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'connection_error':
            msg = CONNECTION_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'credential_error':
            msg = CREDENTIAL_ERROR.format(message)
            await client.send_message(message.channel, msg)

        else:
            msg = '`The current price of a WoW Token on %s realms is %s gold.` :moneybag:' % (region, info)
            await client.send_message(message.channel, msg)


    if message.content.startswith('!armory pve'):
        split = split_query(message.content, 'pve')

        # Assigns the 3rd index in the split to the region
        region = split[3]

        # Sends the returned data to the character_info function to build a character sheet.
        info = await character_info(split[0], split[1], split[2], region)

        # Returns a message to the channel if there's an error fetching.
        if info == 'not_found':
            msg = NOT_FOUND_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'connection_error':
            msg = CONNECTION_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'credential_error':
            msg = CREDENTIAL_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'unknown_error':
            msg = UNKNOWN_ERROR.format(message)
            await client.send_message(message.channel, msg)

        else:
            # Format the AOTC/CE strings if they exist.
            ud_feat = ''
            bod_feat = ''

            if info['ud_feat'] != '':
                ud_feat = '**`%s`**' % (info['ud_feat'])

            if info['bod_feat'] != '':
                bod_feat = '**`%s`**' % (info['bod_feat'])

            msg = discord.Embed(
                title='%s' % (info['name']),
                colour=discord.Colour(info['class_colour']),
                url='%s' % (info['armory']),
                description='%s %s %s %s' % (
                    info['level'], info['faction'], info['spec'], info['class_type']))
            msg.set_thumbnail(
                url='https://render-%s.worldofwarcraft.com/character/%s?_%s' % (
                    region, info['thumb'], epoch_time))
            msg.set_footer(
                text='!armory help | Feedback: https://github.com/JamesIves/discord-wow-armory-bot/issues',
                icon_url='https://raw.githubusercontent.com/JamesIves/discord-wow-armory-bot/master/assets/icon.png')
            msg.add_field(
                name='Character',
                value='**`Name`:** `%s`\n**`Realm`:** `%s (%s)`\n**`Item Level`:** `%s`' % (
                    info['name'], info['realm'], region.upper(), info['ilvl']),
                inline=True)
            msg.add_field(
                name='Keystone Achievements (Season 2)',
                value='**`Conqueror (+10)`: ** `%s`\n**`Master (+15)`: ** `%s` \n' % (
                    info['keystone_season_conqueror'], info['keystone_season_master']),
                inline=True)
            msg.add_field(
                name='Uldir',
                value='**`Normal`:** `%s/%s`\n**`Heroic`:** `%s/%s`\n**`Mythic`:** `%s/%s`\n%s' % (
                    info['uldir']['normal'], info['uldir']['bosses'],
                    info['uldir']['heroic'], info['uldir']['bosses'],
                    info['uldir']['mythic'], info['uldir']['bosses'],
                    ud_feat),
                inline=True)
            msg.add_field(
                name="Battle of Dazar'alor",
                value='**`Normal`:** `%s/%s`\n**`Heroic`:** `%s/%s`\n**`Mythic`:** `%s/%s`\n%s' % (
                    info['battle_of_dazaralor']['normal'], info['battle_of_dazaralor']['bosses'],
                    info['battle_of_dazaralor']['heroic'], info['battle_of_dazaralor']['bosses'],
                    info['battle_of_dazaralor']['mythic'], info['battle_of_dazaralor']['bosses'],
                    bod_feat),
                inline=True)

            await client.send_message(message.channel, embed=msg)


    # Same as before, except this time it's building data for PVP.
    if message.content.startswith('!armory pvp'):
        split = split_query(message.content, 'pvp')
        region = split[3]
        info = await character_info(split[0], split[1], split[2], split[3])

        if info == 'not_found':
            msg = NOT_FOUND_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'connection_error':
            msg = CONNECTION_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'credential_error':
            msg = CREDENTIAL_ERROR.format(message)
            await client.send_message(message.channel, msg)

        elif info == 'unknown_error':
            msg = UNKNOWN_ERROR.format(message)
            await client.send_message(message.channel, msg)

        else:
            msg = discord.Embed(
                title='%s' % (info['name']),
                colour=discord.Colour(info['class_colour']),
                url='%s' % (info['armory']),
                description='%s %s %s %s (BFA)' % (
                    info['level'], info['faction'], info['spec'], info['class_type']))
            msg.set_thumbnail(
                url='https://render-%s.worldofwarcraft.com/character/%s?_%s' % (
                    region, info['thumb'], epoch_time))
            msg.set_footer(
                text='!armory help | Feedback: https://github.com/JamesIves/discord-wow-armory-bot/issues',
                icon_url='https://github.com/JamesIves/discord-wow-armory-bot/blob/master/assets/icon.png?raw=true')
            msg.add_field(
                name='Character',
                value='**`Name`:** `%s`\n**`Realm`:** `%s (%s)`\n**`Battlegroup`:** `%s`\n**`Item Level`:** `%s`' % (
                    info['name'], info['realm'], region.upper(), info['battlegroup'], info['ilvl']),
                inline=True)
            msg.add_field(
                name='Arena Achievements',
                value='**`Challenger`:** `%s`\n**`Rival`:** `%s`\n**`Duelist`:** `%s`\n**`Gladiator`:** `%s`' % (
                    info['arena_challenger'], info['arena_rival'],
                    info['arena_duelist'], info['arena_gladiator']),
                inline=True)
            msg.add_field(
                name='RBG Achievements',
                value='**`%s`:** `%s`\n**`%s`:** `%s`\n**`%s`:** `%s`' % (
                    info['rbg_2400_name'], info['rbg_2400'],
                    info['rbg_2000_name'], info['rbg_2000'],
                    info['rbg_1500_name'], info['rbg_1500']),
                inline=True)
            msg.add_field(
                name='Rated 2v2',
                value='**`Rating`:** `%s`' % (
                    info['2v2']),
                inline=True)
            msg.add_field(
                name='Rated 3v3',
                value='**`Rating`:** `%s`' % (
                    info['3v3']),
                inline=True)
            msg.add_field(
                name='Rated Battlegrounds',
                value='**`Rating`:** `%s`' % (
                    info['rbg']),
                inline=True)
            msg.add_field(
                name='Skirmish 2v2',
                value='**`Rating`:** `%s`' % (
                    info['2v2s']),
                inline=True)
            msg.add_field(
                name='Lifetime Honorable Kills',
                value='`%s`' % (
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

            # Displays the WoW token price
            !armory token

            # You can also provide an optional region to each query to display players from other WoW regions outside of the bot default, for example EU, US, etc.
            !armory pve <name> <realm> <region>
            !armory pvp <armory-link> <region>
            !armory token <region>

            ```
            • Bot created by James Ives (https://jamesiv.es)
            • Feedback, Issues and Source: https://github.com/JamesIves/discord-wow-armory-bot/issues
            """

        msg = '%s'.format(message) % re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', msg, flags=re.M)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    if WOW_CLIENT_ID is None or WOW_CLIENT_ID == '' or WOW_CLIENT_SECRET is None or WOW_CLIENT_SECRET == '':
        print('Missing World of Warcraft Client ID/Secret. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')
        quit()

    if WOW_REGION is None or WOW_REGION == '':
        print('Missing World of Warcraft player region. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')
        quit()

    if LOCALE is None or LOCALE == '':
        print('Missing locale. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')
        quit()

    else:
        print('Launch Succesful! The bot is now listening for commands...')


if DISCORD_BOT_TOKEN is None or DISCORD_BOT_TOKEN == '':
    print('Missing Discord bot token. Please refer to https://github.com/JamesIves/discord-wow-armory-bot#configuration for more details')
    quit()

else:
    client.run(DISCORD_BOT_TOKEN)
