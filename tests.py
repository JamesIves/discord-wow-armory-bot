import unittest
from constants import *
from wow import *

class BaseTest(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
