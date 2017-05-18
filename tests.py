import unittest
import requests
from constants import *
from wow import *

class BaseTest(unittest.TestCase):

    def test_for_class_details(self):
        """Makes sure that when a class id is passed we get the correct name/colour."""
        self.assertEqual(class_details(CLASS_WARRIOR),
        {'colour': 0xC79C6E, 'name': 'Warrior'})

        self.assertEqual(class_details(CLASS_PALADIN),
        {'colour': 0xF58CBA, 'name': 'Paladin'})

        self.assertEqual(class_details(CLASS_HUNTER),
        {'colour': 0xABD473, 'name': 'Hunter'})

        self.assertEqual(class_details(CLASS_ROGUE),
        {'colour': 0xFFF569, 'name': 'Rogue'})

        self.assertEqual(class_details(CLASS_PRIEST),
        {'colour': 0xFFFFFF, 'name': 'Priest'})

        self.assertEqual(class_details(CLASS_DEATH_KNIGHT),
        {'colour': 0xC41F3B, 'name': 'Death Knight'})

        self.assertEqual(class_details(CLASS_SHAMAN),
        {'colour': 0x0070DE, 'name': 'Shaman'})

        self.assertEqual(class_details(CLASS_MAGE),
        {'colour': 0x69CCF0, 'name': 'Mage'})

        self.assertEqual(class_details(CLASS_WARLOCK),
        {'colour': 0x9482C9, 'name': 'Warlock'})

        self.assertEqual(class_details(CLASS_MONK),
        {'colour': 0x00FF96, 'name': 'Monk'})

        self.assertEqual(class_details(CLASS_DRUID),
        {'colour': 0xFF7D0A, 'name': 'Druid'})

        self.assertEqual(class_details(CLASS_DEMON_HUNTER),
        {'colour': 0xA330C9, 'name': 'Demon Hunter'})


    def test_for_faction_name(self):
        """Makes sure that when a faction is passed we get the correct name."""
        self.assertEqual(faction_details(FACTION_ALLIANCE), 'Alliance')

        self.assertEqual(faction_details(FACTION_HORDE), 'Horde')


if __name__ == '__main__':
    unittest.main()
