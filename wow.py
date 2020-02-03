#!/usr/bin/python3
# -*- coding: utf-8 -*-
import aiohttp
from settings import WOW_CLIENT_ID, WOW_CLIENT_SECRET, LOCALE
from constants import *


async def get_data(region, access_token, **kwargs):
    """Helper function that grabs data from the World of Warcraft API."""

    if access_token == "credential_error":
        return access_token

    else:
        if region == "cn":
            base_api_path = "https://gateway.battlenet.com.cn"
        else:
            base_api_path = "https://%s.api.blizzard.com" % (region)

        try:
            async with aiohttp.ClientSession() as client:
                # Fires off a different API call depending on the type of requested content.
                if kwargs.get("field") == "wow_token":
                    api_path = (
                        "%s/data/wow/token/?namespace=dynamic-%s&access_token=%s"
                        % (base_api_path, region, access_token)
                    )

                else:
                    api_path = (
                        "%s/wow/character/%s/%s?fields=%s&locale=%s&access_token=%s"
                        % (
                            base_api_path,
                            kwargs.get("realm"),
                            kwargs.get("name"),
                            kwargs.get("field"),
                            LOCALE,
                            access_token,
                        )
                    )

                async with client.get(
                    api_path, headers={"Authorization": "Bearer %s" % (access_token)}
                ) as api_response:

                    if api_response.status == 200:
                        api_json = await api_response.json()
                        return api_json

                    elif api_response.status == 404:
                        print("Error: Character not found")

                        if kwargs.get("field") == "wow_token":
                            return "gold_error"

                        else:
                            return "not_found"

                    else:
                        raise

        except Exception as error:
            # Error receiving game data:
            print(error)
            print("Error: Connection error occurred when retrieving game data.")
            return "connection_error"


async def get_access_token(region):
    auth_path = "https://%s.battle.net/oauth/token" % (region)
    auth_credentials = aiohttp.BasicAuth(
        login=WOW_CLIENT_ID, password=WOW_CLIENT_SECRET
    )

    try:
        async with aiohttp.ClientSession(auth=auth_credentials) as client:
            async with client.get(
                auth_path, params={"grant_type": "client_credentials"}
            ) as auth_response:
                assert auth_response.status == 200
                auth_json = await auth_response.json()
                return auth_json["access_token"]

    except Exception as error:
        # Error receiving token:
        print("Error: Unable to retrieve auth token")
        return "credential_error"


def character_achievements(achievement_data, faction):
    """Accepts achievement data json and a faction string,
    and returns notable achievement progress. """
    achievements = achievement_data["achievements"]

    # Return In Progress or empty unless they are found.
    keystone_season_master = "In Progress"
    keystone_season_conqueror = "In Progress"
    arena_challenger = "In Progress"
    arena_rival = "In Progress"
    arena_duelist = "In Progress"
    arena_gladiator = "In Progress"
    rbg_2400 = "In Progress"
    rbg_2000 = "In Progress"
    rbg_1500 = "In Progress"
    ud_feat = ""
    bod_feat = ""
    cos_feat = ""
    tep_feat = ""
    nya_feat = ""

    if AC_SEASON_KEYSTONE_MASTER in achievements["achievementsCompleted"]:
        keystone_season_master = "Completed"

    if AC_SEASON_KEYSTONE_CONQUEROR in achievements["achievementsCompleted"]:
        keystone_season_conqueror = "Completed"

    if AC_ARENA_CHALLENGER in achievements["achievementsCompleted"]:
        arena_challenger = "Completed"

    if AC_ARENA_RIVAL in achievements["achievementsCompleted"]:
        arena_rival = "Completed"

    if AC_ARENA_DUELIST in achievements["achievementsCompleted"]:
        arena_duelist = "Completed"

    if AC_ARENA_GLADIATOR in achievements["achievementsCompleted"]:
        arena_gladiator = "Completed"

    if AC_AOTC_UD in achievements["achievementsCompleted"]:
        ud_feat = "Ahead of the Curve"

        # Checks to see if the user has completed tier 2 of the AOTC achievement.
        if AC_CE_UD in achievements["achievementsCompleted"]:
            ud_feat = "Cutting Edge"

    if AC_AOTC_BOD in achievements["achievementsCompleted"]:
        bod_feat = "Ahead of the Curve"

        if AC_CE_BOD in achievements["achievementsCompleted"]:
            bod_feat = "Cutting Edge"

    if AC_AOTC_COS in achievements["achievementsCompleted"]:
        cos_feat = "Ahead of the Curve"

        if AC_CE_COS in achievements["achievementsCompleted"]:
            cos_feat = "Cutting Edge"

    if AC_AOTC_TEP in achievements["achievementsCompleted"]:
        tep_feat = "Ahead of the Curve"

        if AC_CE_TEP in achievements["achievementsCompleted"]:
            tep_feat = "Cutting Edge"

    if AC_AOTC_NYA in achievements["achievementsCompleted"]:
        nya_feat = "Ahead of the Curve"

        if AC_CE_NYA in achievements["achievementsCompleted"]:
            nya_feat = "Cutting Edge"

    # RBG achievements have a different id/name based on faction, checks these
    # based on function argument.
    if faction == "Alliance":
        rbg_2400_name = AC_GRAND_MARSHALL_NAME
        rbg_2000_name = AC_LIEAUTENANT_COMMANDER_NAME
        rbg_1500_name = AC_SERGEANT_MAJOR_NAME

        if AC_GRAND_MARSHALL in achievements["achievementsCompleted"]:
            rbg_2400 = "Completed"

        if AC_LIEUTENANT_COMMANDER in achievements["achievementsCompleted"]:
            rbg_2000 = "Completed"

        if AC_SERGEANT_MAJOR in achievements["achievementsCompleted"]:
            rbg_1500 = "Completed"

    if faction == "Horde":
        rbg_2400_name = AC_HIGH_WARLORD_NAME
        rbg_2000_name = AC_CHAMPION_NAME
        rbg_1500_name = AC_FIRST_SERGEANT_NAME

        if AC_HIGH_WARLORD in achievements["achievementsCompleted"]:
            rbg_2400 = "Completed"

        if AC_CHAMPION in achievements["achievementsCompleted"]:
            rbg_2000 = "Completed"

        if AC_FIRST_SERGEANT in achievements["achievementsCompleted"]:
            rbg_1500 = "Completed"

    achievement_list = {
        "keystone_season_master": keystone_season_master,
        "keystone_season_conqueror": keystone_season_conqueror,
        "arena_challenger": arena_challenger,
        "arena_rival": arena_rival,
        "arena_duelist": arena_duelist,
        "arena_gladiator": arena_gladiator,
        "rbg_2400_name": rbg_2400_name,
        "rbg_2000_name": rbg_2000_name,
        "rbg_1500_name": rbg_1500_name,
        "rbg_2400": rbg_2400,
        "rbg_2000": rbg_2000,
        "rbg_1500": rbg_1500,
        "ud_feat": ud_feat,
        "bod_feat": bod_feat,
        "cos_feat": cos_feat,
        "tep_feat": tep_feat,
        "nya_feat": nya_feat
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

    for boss in raid["bosses"]:
        if boss["lfrKills"] > 0:
            lfr_kills = lfr_kills + 1

        if boss["normalKills"] > 0:
            normal_kills = normal_kills + 1

        if boss["heroicKills"] > 0:
            heroic_kills = heroic_kills + 1

        if boss["mythicKills"] > 0:
            mythic_kills = mythic_kills + 1

        # Determines how many bosses are actually part of this raid.
        bosses = bosses + 1

    raid_data = {
        "lfr": lfr_kills,
        "normal": normal_kills,
        "heroic": heroic_kills,
        "mythic": mythic_kills,
        "bosses": bosses,
    }

    return raid_data


def character_progression(progression_data):
    """Accepts a JSON object containing raid data
    and returns the players current progression."""
    raids = progression_data["progression"]["raids"]

    for raid in raids:
        # Loop over the raids and filter the most recent.
        if raid["id"] == RAID_UD:
            uldir = calculate_boss_kills(raid)

        if raid["id"] == RAID_BOD:
            battle_of_dazaralor = calculate_boss_kills(raid)

        if raid["id"] == RAID_COS:
            crucible_of_storms = calculate_boss_kills(raid)

        if raid["id"] == RAID_TEP:
            the_eternal_palace = calculate_boss_kills(raid)

        if raid["id"] == RAID_NYA:
            nyalotha = calculate_boss_kills(raid)

    raid_stats = {
        "uldir": uldir,
        "battle_of_dazaralor": battle_of_dazaralor,
        "crucible_of_storms": crucible_of_storms,
        "the_eternal_palace": the_eternal_palace,
        "nyalotha": nyalotha
    }

    return raid_stats


def character_arena_progress(pvp_data):
    """Accepts a JSON object containing pvp data
    and returns the players current arena/bg progression. """
    brackets = pvp_data["pvp"]["brackets"]

    two_v_two = brackets["ARENA_BRACKET_2v2"]["rating"]
    two_v_two_skirmish = brackets["ARENA_BRACKET_2v2_SKIRMISH"]["rating"]
    three_v_three = brackets["ARENA_BRACKET_3v3"]["rating"]
    rated_bg = brackets["ARENA_BRACKET_RBG"]["rating"]
    honorable_kills = pvp_data["totalHonorableKills"]

    pvp_data = {
        "2v2": two_v_two,
        "2v2s": two_v_two_skirmish,
        "3v3": three_v_three,
        "rbg": rated_bg,
        "kills": honorable_kills,
    }

    return pvp_data


def character_talents(talent_data):
    """Accepts a JSON object containing a players talents
    and returns the players current active specalization."""
    talents = talent_data["talents"]

    # Starts empty just incase the player hasn't got a spec selected.
    active_spec = ""

    for talent in talents:
        # The API returns the selected key only if it's selected, therefore this check
        # makes sure we're not looking for something that doesn't exist.
        if "selected" in talent.keys():
            if talent["selected"] == True:
                active_spec = talent["spec"]["name"]

    talent_data = {"active_spec": active_spec}

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
    class_colour = ""
    class_name = ""

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

    class_data = {"colour": class_colour, "name": class_name}

    return class_data


async def character_info(name, realm, query, region):
    """Main function which accepts a name/realm/query (pvp or pve).
    Builds a character sheet out of their name, realm,
    armory link, player thumbnail, ilvl, achievement and raid progress and more."""

    # Grabs overall character data including their ilvl.
    access_token = await get_access_token(region)
    info = await get_data(region, access_token, name=name, realm=realm, field="items")

    if info == "not_found" or info == "connection_error" or info == "credential_error":
        return info

    # If the data returned isn't an error string assume it found a character.
    else:
        try:
            class_data = class_details(info["class"])
            faction_name = faction_details(info["faction"])

            # Gathers achievement data from the achievements API.
            achievement_data = await get_data(
                region, access_token, name=name, realm=realm, field="achievements"
            )
            achievements = character_achievements(achievement_data, faction_name)

            # Gathers talent data
            talent_data = await get_data(
                region, access_token, name=name, realm=realm, field="talents"
            )
            talents = character_talents(talent_data)

            # Builds a character sheet depending on the function argument.
            if query == "pve":
                progression_data = await get_data(
                    region, access_token, name=name, realm=realm, field="progression"
                )
                progression = character_progression(progression_data)

                pve_character_sheet = {
                    "name": info["name"],
                    "level": info["level"],
                    "realm": info["realm"],
                    "faction": faction_name,
                    "spec": talents["active_spec"],
                    "battlegroup": info["battlegroup"],
                    "class_colour": class_data["colour"],
                    "class_type": class_data["name"],
                    "armory": "http://%s.battle.net/wow/en/character/%s/%s"
                    % (region, realm, name),
                    "thumb": info["thumbnail"],
                    "ilvl": info["items"]["averageItemLevelEquipped"],
                    "keystone_season_master": achievements["keystone_season_master"],
                    "keystone_season_conqueror": achievements[
                        "keystone_season_conqueror"
                    ],
                    "ud_feat": achievements["ud_feat"],
                    "uldir": progression["uldir"],
                    "bod_feat": achievements["bod_feat"],
                    "battle_of_dazaralor": progression["battle_of_dazaralor"],
                    "cos_feat": achievements["cos_feat"],
                    "crucible_of_storms": progression["crucible_of_storms"],
                    "tep_feat": achievements["tep_feat"],
                    "the_eternal_palace": progression["the_eternal_palace"],
                    "nyalotha": progression["nyalotha"],
                    "nya_feat": achievements["nya_feat"]
                }

                return pve_character_sheet

            if query == "pvp":
                pvp_data = await get_data(
                    region, access_token, name=name, realm=realm, field="pvp"
                )
                print(pvp_data)
                pvp = character_arena_progress(pvp_data)

                pvp_character_sheet = {
                    "name": info["name"],
                    "level": info["level"],
                    "realm": info["realm"],
                    "faction": faction_name,
                    "spec": talents["active_spec"],
                    "battlegroup": info["battlegroup"],
                    "class_colour": class_data["colour"],
                    "class_type": class_data["name"],
                    "armory": "http://%s.battle.net/wow/en/character/%s/%s"
                    % (region, realm, name),
                    "thumb": info["thumbnail"],
                    "ilvl": info["items"]["averageItemLevelEquipped"],
                    "arena_challenger": achievements["arena_challenger"],
                    "arena_rival": achievements["arena_rival"],
                    "arena_duelist": achievements["arena_duelist"],
                    "arena_gladiator": achievements["arena_gladiator"],
                    "2v2": pvp["2v2"],
                    "2v2s": pvp["2v2s"],
                    "3v3": pvp["3v3"],
                    "rbg": pvp["rbg"],
                    "kills": pvp["kills"],
                    "rbg_2400_name": achievements["rbg_2400_name"],
                    "rbg_2400": achievements["rbg_2400"],
                    "rbg_2000_name": achievements["rbg_2000_name"],
                    "rbg_2000": achievements["rbg_2000"],
                    "rbg_1500_name": achievements["rbg_1500_name"],
                    "rbg_1500": achievements["rbg_1500"],
                }

                return pvp_character_sheet

        except Exception as error:
            # Catches any generic errors during character sheet generation,
            # returns an unknown error.
            print("Error: ", error)
            return "unknown_error"


async def wow_token_price(region):
    """Gets the current price for the WoW token based on
    the specified region."""

    access_token = await get_access_token(region)
    info = await get_data(region, access_token, field="wow_token")

    if info == "gold_error" or info == "connection_error" or info == "credential_error":
        return info

    # Formats the token price before returning
    return "{:,}".format(info["price"] / 10000)

