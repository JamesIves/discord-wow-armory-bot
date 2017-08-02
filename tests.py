import unittest
from constants import *
from wow import *
from util import *

class BaseTest(unittest.TestCase):

    def test_for_normal_query_split(self):
        # Tests to ensure that the query gets split properly when the bot gets a message.
        # Example query: '!armory pve/pvp <name> <realm> <region>'
        sample_query = '!armory pve jimo burning-legion us'

        self.assertEqual(split_query(sample_query, 'pve'), ['jimo', 'burning-legion', 'pve', 'us'])


    def test_for_url_query_split(self):
        # Tests to ensure that the query string gets split properly when the bot gets a url based message.
        # Example query: '!armory pve/pvp <armory-link> <region>' (Accepts either a world of warcraft or battle net link)
        sample_wow_url = '!armory pve https://worldofwarcraft.com/en-us/character/burning-legion/jimo us'
        sample_battlenet_url = '!armory pve http://us.battle.net/wow/en/character/burning-legion/jimo/advanced us'

        self.assertEqual(split_query(sample_wow_url, 'pve'), ['jimo', 'burning-legion', 'pve', 'us'])
        self.assertEqual(split_query(sample_battlenet_url, 'pvp'), ['jimo', 'burning-legion', 'pvp', 'us'])


    def test_for_warrior_class(self):
        # Makes sure that when the id for the Warrior class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_WARRIOR),
        {'colour': 0xC79C6E, 'name': 'Warrior'})


    def test_for_paladin_class(self):
        # Makes sure that when the id for the Paladin class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_PALADIN),
        {'colour': 0xF58CBA, 'name': 'Paladin'})


    def test_for_hunter_class(self):
        # Makes sure that when the id for the Hunter class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_HUNTER),
        {'colour': 0xABD473, 'name': 'Hunter'})


    def test_for_rogue_class(self):
        # Makes sure that when the id for the Rogue class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_ROGUE),
        {'colour': 0xFFF569, 'name': 'Rogue'})


    def test_for_priest_class(self):
        # Makes sure that when the id for the Priest class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_PRIEST),
        {'colour': 0xFFFFFF, 'name': 'Priest'})


    def test_for_death_knight_class(self):
        # Makes sure that when the id for the Death Knight class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_DEATH_KNIGHT),
        {'colour': 0xC41F3B, 'name': 'Death Knight'})


    def test_for_shaman_class(self):
        # Makes sure that when the id for the Shaman class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_SHAMAN),
        {'colour': 0x0070DE, 'name': 'Shaman'})


    def test_for_mage_class(self):
        # Makes sure that when the id for the Mage class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_MAGE),
        {'colour': 0x69CCF0, 'name': 'Mage'})


    def test_for_warlock_class(self):
        # Makes sure that when the id for the Warlock class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_WARLOCK),
        {'colour': 0x9482C9, 'name': 'Warlock'})


    def test_for_monk_class(self):
        # Makes sure that when the id for the Monk class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_MONK),
        {'colour': 0x00FF96, 'name': 'Monk'})


    def test_for_druid_class(self):
        # Makes sure that when the id for the Druid class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_DRUID),
        {'colour': 0xFF7D0A, 'name': 'Druid'})


    def test_for_demon_hunter_class(self):
        # Makes sure that when the id for the Demon Hunter class is passed we get the
        # correct name and colour.
        self.assertEqual(class_details(CLASS_DEMON_HUNTER),
        {'colour': 0xA330C9, 'name': 'Demon Hunter'})


    def test_for_faction_name(self):
        # Makes sure that when the id for either the Horde or Alliance faction is
        # passsed we get the correct name in return.
        self.assertEqual(faction_details(FACTION_ALLIANCE), 'Alliance')
        self.assertEqual(faction_details(FACTION_HORDE), 'Horde')


    def test_for_achievement_progress(self):
        # Passes in some mock API data and expects it to return as completed.
        # Tests for accuracy on each id check, not API data.
        self.maxDiff = None
        input_data_horde_sample = {
            "achievements": {
                "achievementsCompleted": [11611, 11162, 11185, 11184, 2090, 2093,
                    2092, 2091, 11194, 11581, 11195, 11874, 5356, 5353, 5349, 11191, 11192, 11874]
            }
        }

        input_data_alliance_sample = {
            "achievements": {
                "achievementsCompleted": [11611, 11162, 11185, 11184, 2090, 2093,
                    2092, 2091, 11194, 11581, 11195, 11874, 5343, 5339, 5334, 11192, 11874, 11875]
            }
        }

        expected_horde_data = {
            'challenging_look': 'Completed',
            'keystone_master': 'Completed',
            'keystone_conqueror': 'Completed',
            'keystone_challenger': 'Completed',
            'arena_challenger': 'Completed',
            'arena_rival': 'Completed',
            'arena_duelist': 'Completed',
            'arena_gladiator': 'Completed',
            'rbg_2400_name': AC_HIGH_WARLORD_NAME,
            'rbg_2000_name': AC_CHAMPION_NAME,
            'rbg_1500_name': AC_FIRST_SERGEANT_NAME,
            'rbg_2400': 'Completed',
            'rbg_2000': 'Completed',
            'rbg_1500': 'Completed',
            'en_feat': 'Cutting Edge',
            'tov_feat': 'Ahead of the Curve',
            'nh_feat': 'Cutting Edge',
            'tos_feat': 'Ahead of the Curve'
        }

        expected_alliance_data = {
            'challenging_look': 'Completed',
            'keystone_master': 'Completed',
            'keystone_conqueror': 'Completed',
            'keystone_challenger': 'Completed',
            'arena_challenger': 'Completed',
            'arena_rival': 'Completed',
            'arena_duelist': 'Completed',
            'arena_gladiator': 'Completed',
            'rbg_2400_name': AC_GRAND_MARSHALL_NAME,
            'rbg_2000_name': AC_LIEAUTENANT_COMMANDER_NAME,
            'rbg_1500_name': AC_SERGEANT_MAJOR_NAME,
            'rbg_2400': 'Completed',
            'rbg_2000': 'Completed',
            'rbg_1500': 'Completed',
            'en_feat': 'Ahead of the Curve',
            'tov_feat': 'Ahead of the Curve',
            'nh_feat': 'Cutting Edge',
            'tos_feat': 'Cutting Edge'
        }

        self.assertEqual(character_achievements(input_data_horde_sample, 'Horde'), expected_horde_data)
        self.assertEqual(character_achievements(input_data_alliance_sample, 'Alliance'), expected_alliance_data)

    def test_pvp_progression(self):
        # Passes in some mock API data and expects it to return an object with the correct data.
        # Tests for accuracy on each data check, not API data.
        self.maxDiff = None
        sample_data = {
           "pvp": {
                "brackets": {
                    "ARENA_BRACKET_2v2": {
                        "rating": 5928,
                    },
                    "ARENA_BRACKET_3v3": {
                        "rating": 1858,
                    },
                    "ARENA_BRACKET_RBG": {
                        "rating": 5999,
                    },
                    "ARENA_BRACKET_2v2_SKIRMISH": {
                        "rating": 2985,
                    }
                }
            },
            "totalHonorableKills": 888399
        }

        expected_data = {
            '2v2': 5928,
            '2v2s': 2985,
            '3v3': 1858,
            'rbg': 5999,
            'kills': 888399
        }

        self.assertEqual(character_arena_progress(sample_data), expected_data)

    def test_pve_progression(self):
        # Passes in some mock API data and expects it to return an object with the correct data.
        # Tests for accuracy on each data check, not API data.
        self.maxDiff = None
        sample_data = {
            "progression": {
                "raids": [
                    {
                    "id": 8026,
                    "bosses": [{
                        "lfrKills": 19,
                        "normalKills": 8,
                        "heroicKills": 5,
                        "mythicKills": 3,
                        },
                        {
                        "lfrKills": 3,
                        "normalKills": 7,
                        "heroicKills": 3,
                        "mythicKills": 2,
                        }]
                    },
                    {
                    "id": 8440,
                    "bosses": [{
                        "lfrKills": 7,
                        "normalKills": 1,
                        "heroicKills": 1,
                        "mythicKills": 0,
                        }]
                    },
                    {
                    "id": 8524,
                    "bosses": [{
                        "lfrKills": 3,
                        "normalKills": 2,
                        "heroicKills": 4,
                        "mythicKills": 1,
                        }]
                    },
                    {
                    "id": 8025,
                    "bosses": [{
                        "lfrKills": 3,
                        "normalKills": 2,
                        "heroicKills": 1,
                        "mythicKills": 0,
                        },
                        {
                        "lfrKills": 5,
                        "normalKills": 2,
                        "heroicKills": 2,
                        "mythicKills": 0,
                        }]
                    }]
                }
            }

        expected_data = {
            'emerald_nightmare':{
                  'lfr':2,
                  'normal':2,
                  'heroic':2,
                  'mythic':2,
                  'bosses':2
               },
               'trial_of_valor':{
                  'lfr':1,
                  'normal':1,
                  'heroic':1,
                  'mythic':0,
                  'bosses':1
               },
               'the_nighthold':{
                  'lfr':2,
                  'normal':2,
                  'heroic':2,
                  'mythic':0,
                  'bosses':2
               },
               'tomb_of_sargeras': {
                  'lfr':1,
                  'normal':1,
                  'heroic':1,
                  'mythic':1,
                  'bosses':1
               }
        }

        self.assertEqual(character_progression(sample_data), expected_data)

    def test_player_talents(self):
        # Passes in some mock API data and expects it to return an object with the correct data.
        # Tests for accuracy on each data check, not API data.

        sample_data = {
            'talents': [
            {
                'selected':True,
                'spec':{
                    'name':'Holy',
                    'role':'HEALING'
                }
            },
            {
                'spec':{
                    'name':'Shadow',
                    'role': 'DAMAGE'
                }
            },
            {
                'spec':{
                    'name':'Discipline',
                    'role':'HEALING'
                }
            }
        ]}

        expected_data = {
            'active_spec': 'Holy'
        }

        self.assertEqual(character_talents(sample_data), expected_data)


if __name__ == '__main__':
    unittest.main()
