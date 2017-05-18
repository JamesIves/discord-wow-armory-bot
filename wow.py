#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import os
import json

def get_data(name, realm, field):
    """Helper function that grabs data from the World of Warcraft API."""
    path = 'https://%s.api.battle.net/wow/character/%s/%s?fields=%s&locale=%s&apikey=%s' % (
        WOW_REGION, realm, name, field, LOCALE, WOW_API_KEY)

    request = requests.get(path)
    request_json = request.json()

    try:
        request = requests.get(path)
        # Make sure the request doesn't error.
        request.raise_for_status()
        request_json = request.json()

    except requests.exceptions.RequestException as error:
        # If there's an issue or a character doesn't exist, return an empty
        # string.
        request_json = ''
        print(error)

    return request_json


def character_achievements(name, realm, faction):
    """Accepts a name/realm/faction, and returns notable achievement progress.
    Tracks Ahead of the Curve for NH, EN, TOV, and Keystone Conqueror/Master"""
    info = get_data(name, realm, 'achievements')
    achievements = info['achievements']

    # Return In Progress/Incomplete unless they are found.
    keystone_master = 'In Progress'
    keystone_conqueror = 'In Progress'
    keystone_challenger = 'In Progress'
    challenging_look = 'In Progress'
    arena_challenger = 'In Progress'
    arena_rival = 'In Progress'
    arena_duelist = 'In Progress'
    arena_gladiator = 'In Progress'
    rbg_2400 = 'In Progress'
    rbg_2000 = 'In Progress'
    rbg_1500 = 'In Progress'
    aotc_en = 'Incomplete'
    aotc_tov = 'Incomplete'
    aotc_nh = 'Incomplete'

    if AC_CHALLENGING_LOOK in achievements['achievementsCompleted']:
        challenging_look = 'Completed'

    if AC_KEYSTONE_MASTER in achievements['achievementsCompleted']:
        keystone_master = 'Completed'

    if AC_KEYSTONE_CONQUEROR in achievements['achievementsCompleted']:
        keystone_conqueror = 'Completed'

    if AC_KEYSTONE_CHALLENGER in achievements['achievementsCompleted']:
        keystone_challenger = 'Completed'

    if AC_ARENA_CHALLENGER in achievements['achievementsCompleted']:
        arena_challenger = 'Completed'

    if AC_ARENA_RIVA in achievements['achievementsCompleted']:
        arena_rival = 'Completed'

    if AC_ARENA_DUELIST in achievements['achievementsCompleted']:
        arena_duelist = 'Completed'

    if AC_ARENA_GLADIATOR in achievements['achievementsCompleted']:
        arena_gladiator = 'Completed'

    if AC_AOTC_EN in achievements['achievementsCompleted']:
        aotc_en = 'Completed'

    if AC_AOTC_TOV in achievements['achievementsCompleted']:
        aotc_tov = 'Completed'

    if AC_AOTC_NH in achievements['achievementsCompleted']:
        aotc_nh = 'Completed'

    # RBG achievements have a different id/name based on faction, checks these
    # based on function arg.
    if faction == 'Alliance':
        rbg_2400_name = 'Grand Marshall'
        rbg_2000_name = 'Lieutenant Commander'
        rbg_1500_name = 'Sergeant Major'

        if AC_GRAND_MARSHALL in achievements['achievementsCompleted']:
            rbg_2400 = 'Completed'

        if AC_LIEUTENANT_COMMANDER in achievements['achievementsCompleted']:
            rbg_2000 = 'Completed'

        if AC_SERGEANT_MAJOR in achievements['achievementsCompleted']:
            rbg_1500 = 'Completed'

    if faction == 'Horde':
        rbg_2400_name = 'High Warlord'
        rbg_2000_name = 'Champion'
        rbg_1500_name = 'First Sergeant'

        if AC_HIGH_WARLORD in achievements['achievementsCompleted']:
            rbg_2400 = 'Completed'

        if AC_CHAMPION in achievements['achievementsCompleted']:
            rbg_2000 = 'Completed'

        if AC_FIRST_SERGEANT in achievements['achievementsCompleted']:
            rbg_1500 = 'Completed'

    achievement_list = {
        'challenging_look': challenging_look,
        'keystone_master': keystone_master,
        'keystone_conqueror': keystone_conqueror,
        'keystone_challenger': keystone_challenger,
        'arena_challenger': arena_challenger,
        'arena_rival': arena_rival,
        'arena_duelist': arena_duelist,
        'arena_gladiator': arena_gladiator,
        'rbg_2400_name': rbg_2400_name,
        'rbg_2000_name': rbg_2000_name,
        'rbg_1500_name': rbg_1500_name,
        'rbg_2400': rbg_2400,
        'rbg_2000': rbg_2000,
        'rbg_1500': rbg_1500,
        'aotc_en': aotc_en,
        'aotc_tov': aotc_tov,
        'aotc_nh': aotc_nh
    }

    return achievement_list


def calculate_boss_kills(raid):
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


def character_progression(name, realm):
    """Accepts a name/realm and determines the players players
    current progression."""
    info = get_data(name, realm, 'progression')
    raids = info['progression']['raids']

    for raid in raids:
        # Loop over the raids and filter the most recent.
        if raid['id'] == RAID_EN:
            emerald_nightmare = calculate_boss_kills(raid)

        if raid['id'] == RAID_TOV:
            trial_of_valor = calculate_boss_kills(raid)

        if raid['id'] == RAID_NH:
            the_nighthold = calculate_boss_kills(raid)

    raid_stats = {
        'emerald_nightmare': emerald_nightmare,
        'trial_of_valor': trial_of_valor,
        'the_nighthold': the_nighthold
    }

    return raid_stats


def characterArenaProgress(name, realm):
    """Accepts a name/realm and determines the players players
    current arena/bg progression. """
    info = get_data(name, realm, 'pvp')
    brackets = info['pvp']['brackets']

    two_v_two = brackets['ARENA_BRACKET_2v2']['rating']
    two_v_two_skirmish = brackets['ARENA_BRACKET_2v2_SKIRMISH']['rating']
    three_v_three = brackets['ARENA_BRACKET_3v3']['rating']
    rated_bg = brackets['ARENA_BRACKET_RBG']['rating']
    honorable_kills = info['totalHonorableKills']

    pvp_data = {
        '2v2': two_v_two,
        '2v2s': two_v_two_skirmish,
        '3v3': three_v_three,
        'rbg': rated_bg,
        'kills': honorable_kills
    }

    return pvp_data


def faction_details(faction_id):
    """Accepts a faction id and returns the name."""
    if faction_id == FACTION_HORDE:
        faction_name = 'Horde'

    if faction_id == FACTION_ALLIANCE:
        faction_name = 'Alliance'

    return faction_name


def class_details(class_type):
    """Accepts a class index and then determines the
    colour code and name for that class."""
    class_colour = ''
    class_name = ''

    # Warrior
    if class_type == CLASS_WARRIOR:
        class_colour = 0xC79C6E
        class_name = 'Warrior'

    # Paladin
    if class_type == CLASS_PALADIN:
        class_colour = 0xF58CBA
        class_name = 'Paladin'

    # Hunter
    if class_type == CLASS_HUNTER:
        class_colour = 0xABD473
        class_name = 'Hunter'

    # Rogue
    if class_type == CLASS_ROGUE:
        class_colour = 0xFFF569
        class_name = 'Rogue'

    # Priest
    if class_type == CLASS_PRIEST:
        class_colour = 0xFFFFFF
        class_name = 'Priest'

    # Death Knight
    if class_type == CLASS_DEATH_KNIGHT:
        class_colour = 0xC41F3B
        class_name = 'Death Knight'

    # Shaman
    if class_type == CLASS_SHAMAN:
        class_colour = 0x0070DE
        class_name = 'Shaman'

    # Mage
    if class_type == CLASS_MAGE:
        class_colour = 0x69CCF0
        class_name = 'Mage'

    # Warlock
    if class_type == CLASS_WARLOCK:
        class_colour = 0x9482C9
        class_name = 'Warlock'

    # Monk
    if class_type == CLASS_MONK:
        class_colour = 0x00FF96
        class_name = 'Monk'

    # Druid
    if class_type == CLASS_DRUID:
        class_colour = 0xFF7D0A
        class_name = 'Druid'

    # Demon Hunter
    if class_type == CLASS_DEMON_HUNTER:
        class_colour = 0xA330C9
        class_name = 'Demon Hunter'

    class_data = {
        'colour': class_colour,
        'name': class_name
    }

    return class_data


def character_info(name, realm, query):
    """Main function which accepts a name/realm.
    Builds a character sheet out of their name, realm,
    armory link, player thumbnail, ilvl, achievement and raid progress."""
    name = name
    realm = realm

    # Grabs overall character data including their ilvl.
    info = get_data(name, realm, 'items')

    # If the data returned isn't an empty string assume it found a character.
    if info != '':
        class_data = class_details(info['class'])
        faction_name = faction_details(info['faction'])
        achievements = character_achievements(name, realm, faction_name)

        # Builds a character sheet depending on the function argument.
        if query == 'pve':
            progression = character_progression(name, realm)

            pve_character_sheet = {
                'name': info['name'],
                'level': info['level'],
                'realm': info['realm'],
                'faction': faction_name,
                'battlegroup': info['battlegroup'],
                'class_colour': class_data['colour'],
                'class_type': class_data['name'],
                'armory': 'http://%s.battle.net/wow/en/character/%s/%s' % (
                    WOW_REGION, realm, name),
                'thumb': info['thumbnail'],
                'ilvl': info['items']['averageItemLevelEquipped'],
                'challenging_look': achievements['challenging_look'],
                'keystone_master': achievements['keystone_master'],
                'keystone_conqueror': achievements['keystone_conqueror'],
                'keystone_challenger': achievements['keystone_challenger'],
                'aotc_en': achievements['aotc_en'],
                'aotc_tov': achievements['aotc_tov'],
                'aotc_nh': achievements['aotc_nh'],
                'emerald_nightmare': progression['emerald_nightmare'],
                'trial_of_valor': progression['trial_of_valor'],
                'the_nighthold': progression['the_nighthold']
            }

            return pve_character_sheet

        if query == 'pvp':
            pvp = characterArenaProgress(name, realm)

            pvp_character_sheet = {
                'name': info['name'],
                'level': info['level'],
                'realm': info['realm'],
                'faction': faction_name,
                'battlegroup': info['battlegroup'],
                'class_colour': class_data['colour'],
                'class_type': class_data['name'],
                'armory': 'http://%s.battle.net/wow/en/character/%s/%s' % (
                    WOW_REGION, realm, name),
                'thumb': info['thumbnail'],
                'ilvl': info['items']['averageItemLevelEquipped'],
                'arena_challenger': achievements['arena_challenger'],
                'arena_rival': achievements['arena_rival'],
                'arena_duelist': achievements['arena_duelist'],
                'arena_gladiator': achievements['arena_gladiator'],
                '2v2': pvp['2v2'],
                '2v2s': pvp['2v2s'],
                '3v3': pvp['3v3'],
                'rbg': pvp['rbg'],
                'kills': pvp['kills'],
                'rbg_2400_name': achievements['rbg_2400_name'],
                'rbg_2400': achievements['rbg_2400'],
                'rbg_2000_name': achievements['rbg_2000_name'],
                'rbg_2000': achievements['rbg_2000'],
                'rbg_1500_name': achievements['rbg_1500_name'],
                'rbg_1500': achievements['rbg_1500'],
            }

            return pvp_character_sheet

    else:
        # Otherwise return another empty string so the calling function knows
        # how to handle it.
        return ''
