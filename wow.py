#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import os
import json


WOW_API_KEY = str(os.environ.get('WOW_API_KEY'))
WOW_REGION = str(os.environ.get('WOW_REGION'))
LOCALE = str(os.environ.get('LOCALE'))


def getData(name, realm, field):
    """Helper function that grabs data from the World of Warcraft API."""
    path = 'https://%s.api.battle.net/wow/character/%s/%s?fields=%s&locale=%s&apikey=%s' % (WOW_REGION, realm, name, field, LOCALE, WOW_API_KEY)

    request = requests.get(path)
    request_json = request.json()

    try:
        request = requests.get(path)
        # Make sure the request doesn't error.
        request.raise_for_status()
        request_json = request.json()

    except requests.exceptions.RequestException as error:
        # If there's an issue or a character doesn't exist, return an empty string.
        request_json = ''
        print (error)

    return request_json


def characterAchievements(name, realm, content):
    """Accepts a name/realm, and returns notable achievement progress.
    Tracks Ahead of the Curve for NH, EN, TOV, and Keystone Conqueror/Master"""
    info = getData(name, realm, 'achievements')

    if content == 'pve':
        # Return In Progress/Incomplete unless they are found.
        keystone_master = 'In Progress'
        keystone_conqueror = 'In Progress'
        aotc_en = 'Incomplete'
        aotc_tov = 'Incomplete'
        aotc_nh = 'Incomplete'

        if 11162 in info['achievements']['achievementsCompleted']:
            keystone_master = 'Completed +15'

        if 11185 in info['achievements']['achievementsCompleted']:
            keystone_conqueror = 'Completed +10'

        if 11194 in info['achievements']['achievementsCompleted']:
            aotc_en = 'Completed'

        if 11581 in info['achievements']['achievementsCompleted']:
            aotc_tov = 'Completed'

        if 11195 in info['achievements']['achievementsCompleted']:
            aotc_nh = 'Completed'

        return [keystone_master, keystone_conqueror, aotc_en, aotc_tov, aotc_nh]

    if content == 'pvp':
        return


def calculateBossKills(raid):
    """Accepts character raid data and figures out how many bosses
    the player has killed and at what difficulty."""

    # Initiate values at zero.
    raid_name = raid['name']
    lfr_kills = 0
    normal_kills = 0
    heroic_kills = 0
    mythic_kills = 0
    bosses = 0

    for boss in raid['bosses']:
        if boss['lfrKills'] > 0:
            lfr_kills = lfr_kills + 1

        if boss['normalKills'] > 0:
            normal_kills = normal_kills + 1

        if boss['heroicKills'] > 0:
            heroic_kills = heroic_kills + 1

        if boss['mythicKills'] > 0:
            mythic_kills = mythic_kills + 1

        # Determines how many bosses are actually part of this raid.
        bosses = bosses + 1

    raid_data = {
        'lfr': lfr_kills,
        'normal': normal_kills,
        'heroic': heroic_kills,
        'mythic': mythic_kills,
        'bosses': bosses
    }

    return raid_data


def characterProgression(name, realm):
    """Accepts a name/realm and determines the players players current progression.
    Sends current raid data to the calculateBossKills function. """
    info = getData(name, realm, 'progression')

    for raid in info['progression']['raids']:
        # Loop over the raids and filter the most recent.
        if raid['id'] == 8026:
            emerald_nightmare = calculateBossKills(raid)

        if raid['id'] == 8440:
            trial_of_valor = calculateBossKills(raid)

        if raid['id'] == 8025:
            the_nighthold = calculateBossKills(raid)

    return [emerald_nightmare, trial_of_valor, the_nighthold]


def characterArenaProgress(name, realm)
    info = getData(name, realm, 'pvp')
    
    two_v_two = 0
    two_v_two_skirmish = 0
    three_v_three = 0
    rated_bg = 0
    honorable_kills = info['totalHonorableKills']

    for bracket in info['pvp']['brackets']:
        if bracket['slug'] == '2v2':
            two_v_two = bracket['rating']

        if bracket['slug'] == '2v2s':
            two_v_two_skirmish = bracket['rating']

        if bracket['slug'] == '3v3':
            three_v_three = bracket['rating']

        if bracket['slug'] == 'rbg':
            rated_bg = bracket['rating']

    pvp_data = {
        '2v2': two_v_two,
        '2v2s': two_v_two_skirmish,
        '3v3': three_v_three,
        'rbg': rated_bg,
        'kills': honorable_kills
    }

    return pvp_data


def classDetails(class_type):
    """Accepts a class index and then determines the colour code and name for that class."""
    class_colour = ''
    class_name = ''

    # Warrior
    if class_type == 1:
        class_colour = 0xC79C6E
        class_name = 'Warrior'

    # Paladin
    if class_type == 2:
        class_colour = 0xF58CBA
        class_name = 'Paladin'

    # Hunter
    if class_type == 3:
        class_colour = 0xABD473
        class_name = 'Hunter'

    # Rogue
    if class_type == 4:
        class_colour = 0xFFF569
        class_name = 'Rogue'

    # Priest
    if class_type == 5:
        class_colour = 0xFFFFFF
        class_name = 'Priest'

    # Death Knight
    if class_type == 6:
        class_colour = 0xC41F3B
        class_name = 'Death Knight'

    # Shaman
    if class_type == 7:
        class_colour = 0x0070DE
        class_name = 'Shaman'

    # Mage
    if class_type == 8:
        class_colour = 0x69CCF0
        class_name = 'Mage'

    # Warlock
    if class_type == 9:
        class_colour = 0x9482C9
        class_name = 'Warlock'

    # Monk
    if class_type == 10:
        class_colour = 0x00FF96
        class_name = 'Monk'

    # Druid
    if class_type == 11:
        class_colour = 0xFF7D0A
        class_name = 'Druid'

    # Demon Hunter
    if class_type == 12:
        class_colour = 0xA330C9
        class_name = 'Demon Hunter'

    return [class_colour, class_name]


def characterInfo(name, realm, query):
    """Main function which accepts a name/realm. Builds a character sheet out of their
    name, realm, armory link, player thumbnail, ilvl, achievement and raid progress."""
    name = name
    realm = realm

    # Grabs overall character data including their ilvl.
    info = getData(name, realm, 'items')

    # If the data returned isn't an empty string assume it found a character.
    if info != '':
        class_data = classDetails(info['class'])

        if query == 'pve':
            achievements = characterAchievements(name, realm, 'pve')
            progression = characterProgression(name, realm)

            pve_character_sheet = {
                'name': info["name"],
                'level': info["level"],
                'realm': info["realm"],
                'battlegroup': info["battlegroup"],
                'class_colour': class_data[0],
                'class_type': class_data[1],
                'armory': 'http://%s.battle.net/wow/en/character/%s/%s' % (WOW_REGION, realm, name),
                'thumb': info["thumbnail"],
                'ilvl': info["items"]["averageItemLevelEquipped"],
                'keystone_master': achievements[0],
                'keystone_conqueror': achievements[1],
                'aotc_en': achievements[2],
                'aotc_tov': achievements[3],
                'aotc_nh': achievements[4],
                'emerald_nightmare': progression[0],
                'trial_of_valor': progression[1],
                'the_nighthold': progression[2]
            }

            return pve_character_sheet

        if query == 'pvp':
            achievements = characterAchievements(name, realm, 'pvp')
            pvp = characterArenaProgress(name, realm)

            pvp_character_sheet = {
                'name': info["name"],
                'level': info["level"],
                'realm': info["realm"],
                'battlegroup': info["battlegroup"],
                'class_colour': class_data[0],
                'class_type': class_data[1],
                'armory': 'http://%s.battle.net/wow/en/character/%s/%s' % (WOW_REGION, realm, name),
                'thumb': info["thumbnail"],
                'ilvl': info["items"]["averageItemLevelEquipped"],
                '2v2': pvp["2v2"],
                '2v2s': pvp["2v2s"],
                '3v3': pvp["3v3"],
                'rbg': pvp["rbg"],
                'kills': pvp["kills"]
            }

            return pve_character_sheet

    else:
        # Otherwise return another empty string.
        return ''
