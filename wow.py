#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from settings import WOW_API_KEY, LOCALE
from constants import *


def get_data(name, realm, field, region):
    """Helper function that grabs data from the World of Warcraft API."""
    path = 'https://%s.api.battle.net/wow/character/%s/%s?fields=%s&locale=%s&apikey=%s' % (
        region, realm, name, field, LOCALE, WOW_API_KEY)

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


def character_achievements(achievement_data, faction):
    """Accepts achievement data json and a faction string,
    and returns notable achievement progress. """
    achievements = achievement_data['achievements']

    # Return In Progress or empty unless they are found.
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
    en_feat = ''
    tov_feat = ''
    nh_feat = ''
    tos_feat = ''
    atbt_feat = ''

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

    if AC_ARENA_RIVAL in achievements['achievementsCompleted']:
        arena_rival = 'Completed'

    if AC_ARENA_DUELIST in achievements['achievementsCompleted']:
        arena_duelist = 'Completed'

    if AC_ARENA_GLADIATOR in achievements['achievementsCompleted']:
        arena_gladiator = 'Completed'

    if AC_AOTC_EN in achievements['achievementsCompleted']:
        en_feat = 'Ahead of the Curve'

        # Checks to see if the user has completed tier 2 of the AOTC achievement.
        if AC_CE_EN in achievements['achievementsCompleted']:
            en_feat = 'Cutting Edge'

    if AC_AOTC_TOV in achievements['achievementsCompleted']:
        tov_feat = 'Ahead of the Curve'

        if AC_CE_TOV in achievements['achievementsCompleted']:
            tov_feat = 'Cutting Edge'

    if AC_AOTC_NH in achievements['achievementsCompleted']:
        nh_feat = 'Ahead of the Curve'

        if AC_CE_NH in achievements['achievementsCompleted']:
            nh_feat = 'Cutting Edge'

    if AC_AOTC_TOS in achievements['achievementsCompleted']:
        tos_feat = 'Ahead of the Curve'

        if AC_CE_TOS in achievements['achievementsCompleted']:
            tos_feat = 'Cutting Edge'

    if AC_AOTC_ATBT in achievements['achievementsCompleted']:
        atbt_feat = 'Ahead of the Curve'

        if AC_CE_ATBT in achievements['achievementsCompleted']:
            atbt_feat = 'Cutting Edge'


    # RBG achievements have a different id/name based on faction, checks these
    # based on function argument.
    if faction == 'Alliance':
        rbg_2400_name = AC_GRAND_MARSHALL_NAME
        rbg_2000_name = AC_LIEAUTENANT_COMMANDER_NAME
        rbg_1500_name = AC_SERGEANT_MAJOR_NAME

        if AC_GRAND_MARSHALL in achievements['achievementsCompleted']:
            rbg_2400 = 'Completed'

        if AC_LIEUTENANT_COMMANDER in achievements['achievementsCompleted']:
            rbg_2000 = 'Completed'

        if AC_SERGEANT_MAJOR in achievements['achievementsCompleted']:
            rbg_1500 = 'Completed'

    if faction == 'Horde':
        rbg_2400_name = AC_HIGH_WARLORD_NAME
        rbg_2000_name = AC_CHAMPION_NAME
        rbg_1500_name = AC_FIRST_SERGEANT_NAME

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
        'en_feat': en_feat,
        'tov_feat': tov_feat,
        'nh_feat': nh_feat,
        'tos_feat': tos_feat,
        'atbt_feat': atbt_feat
    }

    return achievement_list


def calculate_boss_kills(raid):
    """Accepts character raid data and figures out how many bosses
    the player has killed and at what difficulty."""

    # Initiate values at zero.
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


def character_progression(progression_data):
    """Accepts a JSON object containing raid data
    and returns the players current progression."""
    raids = progression_data['progression']['raids']

    for raid in raids:
        # Loop over the raids and filter the most recent.
        if raid['id'] == RAID_EN:
            emerald_nightmare = calculate_boss_kills(raid)

        if raid['id'] == RAID_TOV:
            trial_of_valor = calculate_boss_kills(raid)

        if raid['id'] == RAID_NH:
            the_nighthold = calculate_boss_kills(raid)

        if raid['id'] == RAID_TOS:
            tomb_of_sargeras = calculate_boss_kills(raid)

        if raid['id'] == RAID_ATBT:
            antorus_the_burning_throne = calculate_boss_kills(raid)

    raid_stats = {
        'emerald_nightmare': emerald_nightmare,
        'trial_of_valor': trial_of_valor,
        'the_nighthold': the_nighthold,
        'tomb_of_sargeras': tomb_of_sargeras,
        'antorus_the_burning_throne': antorus_the_burning_throne
    }

    return raid_stats


def character_arena_progress(pvp_data):
    """Accepts a JSON object containing pvp data
    and returns the players current arena/bg progression. """
    brackets = pvp_data['pvp']['brackets']

    two_v_two = brackets['ARENA_BRACKET_2v2']['rating']
    two_v_two_skirmish = brackets['ARENA_BRACKET_2v2_SKIRMISH']['rating']
    three_v_three = brackets['ARENA_BRACKET_3v3']['rating']
    rated_bg = brackets['ARENA_BRACKET_RBG']['rating']
    honorable_kills = pvp_data['totalHonorableKills']

    pvp_data = {
        '2v2': two_v_two,
        '2v2s': two_v_two_skirmish,
        '3v3': three_v_three,
        'rbg': rated_bg,
        'kills': honorable_kills
    }

    return pvp_data


def character_talents(talent_data):
    """Accepts a JSON object containing a players talents
    and returns the players current active specalization."""
    talents = talent_data['talents']

    # Starts empty just incase the player hasn't got a spec selected.
    active_spec = ''

    for talent in talents:
        # The API returns the selected key only if it's selected, therefore this check
        # makes sure we're not looking for something that doesn't exist.
        if 'selected' in talent.keys():
            if talent['selected'] == True:
                active_spec = talent['spec']['name']

    talent_data = {
        'active_spec': active_spec
    }

    return talent_data


def faction_details(faction_id):
    """Accepts a faction id and returns the name."""
    if faction_id == FACTION_HORDE:
        faction_name = FACTION_HORDE_NAME

    if faction_id == FACTION_ALLIANCE:
        faction_name = FACTION_ALLIANCE_NAME

    return faction_name


def class_details(class_type):
    """Accepts a class index and then determines the
    colour code and name for that class."""
    class_colour = ''
    class_name = ''

    # Warrior
    if class_type == CLASS_WARRIOR:
        class_colour = CLASS_WARRIOR_COLOUR
        class_name = CLASS_WARRIOR_NAME

    # Paladin
    if class_type == CLASS_PALADIN:
        class_colour = CLASS_PALADIN_COLOUR
        class_name = CLASS_PALADIN_NAME

    # Hunter
    if class_type == CLASS_HUNTER:
        class_colour = CLASS_HUNTER_COLOUR
        class_name = CLASS_HUNTER_NAME

    # Rogue
    if class_type == CLASS_ROGUE:
        class_colour = CLASS_ROGUE_COLOUR
        class_name = CLASS_ROGUE_NAME

    # Priest
    if class_type == CLASS_PRIEST:
        class_colour = CLASS_PRIEST_COLOUR
        class_name = CLASS_PRIEST_NAME

    # Death Knight
    if class_type == CLASS_DEATH_KNIGHT:
        class_colour = CLASS_DEATH_KNIGHT_COLOUR
        class_name = CLASS_DEATH_KNIGHT_NAME

    # Shaman
    if class_type == CLASS_SHAMAN:
        class_colour = CLASS_SHAMAN_COLOUR
        class_name = CLASS_SHAMAN_NAME

    # Mage
    if class_type == CLASS_MAGE:
        class_colour = CLASS_MAGE_COLOUR
        class_name = CLASS_MAGE_NAME

    # Warlock
    if class_type == CLASS_WARLOCK:
        class_colour = CLASS_WARLOCK_COLOUR
        class_name = CLASS_WARLOCK_NAME

    # Monk
    if class_type == CLASS_MONK:
        class_colour = CLASS_MONK_COLOUR
        class_name = CLASS_MONK_NAME

    # Druid
    if class_type == CLASS_DRUID:
        class_colour = CLASS_DRUID_COLOUR
        class_name = CLASS_DRUID_NAME

    # Demon Hunter
    if class_type == CLASS_DEMON_HUNTER:
        class_colour = CLASS_DEMON_HUNTER_COLOUR
        class_name = CLASS_DEMON_HUNTER_NAME

    class_data = {
        'colour': class_colour,
        'name': class_name
    }

    return class_data


def character_info(name, realm, query, region):
    """Main function which accepts a name/realm/query(pvp or pve).
    Builds a character sheet out of their name, realm,
    armory link, player thumbnail, ilvl, achievement and raid progress and more."""

    # Grabs overall character data including their ilvl.
    info = get_data(name, realm, 'items', region)

    # If the data returned isn't an empty string assume it found a character.
    if info != '':
        class_data = class_details(info['class'])
        faction_name = faction_details(info['faction'])

        # Gathers achievement data from the achievements API.
        achievement_data = get_data(name, realm, 'achievements', region)
        achievements = character_achievements(achievement_data, faction_name)

        # Gathers talent data
        talent_data = get_data(name, realm, 'talents', region)
        talents = character_talents(talent_data)

        # Builds a character sheet depending on the function argument.
        if query == 'pve':
            progression_data = get_data(name, realm, 'progression', region)
            progression = character_progression(progression_data)

            pve_character_sheet = {
                'name': info['name'],
                'level': info['level'],
                'realm': info['realm'],
                'faction': faction_name,
                'spec': talents['active_spec'],
                'battlegroup': info['battlegroup'],
                'class_colour': class_data['colour'],
                'class_type': class_data['name'],
                'armory': 'http://%s.battle.net/wow/en/character/%s/%s' % (
                   region, realm, name),
                'thumb': info['thumbnail'],
                'ilvl': info['items']['averageItemLevelEquipped'],
                'challenging_look': achievements['challenging_look'],
                'keystone_master': achievements['keystone_master'],
                'keystone_conqueror': achievements['keystone_conqueror'],
                'keystone_challenger': achievements['keystone_challenger'],
                'en_feat': achievements['en_feat'],
                'tov_feat': achievements['tov_feat'],
                'nh_feat': achievements['nh_feat'],
                'tos_feat': achievements['tos_feat'],
                'atbt_feat': achievements['atbt_feat'],
                'emerald_nightmare': progression['emerald_nightmare'],
                'trial_of_valor': progression['trial_of_valor'],
                'the_nighthold': progression['the_nighthold'],
                'tomb_of_sargeras': progression['tomb_of_sargeras'],
                'antorus_the_burning_throne': progression['antorus_the_burning_throne']
            }

            return pve_character_sheet

        if query == 'pvp':
            pvp_data = get_data(name, realm, 'pvp', region)
            pvp = character_arena_progress(pvp_data)

            pvp_character_sheet = {
                'name': info['name'],
                'level': info['level'],
                'realm': info['realm'],
                'faction': faction_name,
                'spec': talents['active_spec'],
                'battlegroup': info['battlegroup'],
                'class_colour': class_data['colour'],
                'class_type': class_data['name'],
                'armory': 'http://%s.battle.net/wow/en/character/%s/%s' % (
                    region, realm, name),
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
