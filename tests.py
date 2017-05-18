import unittest
import requests
from constants import *
from wow import *

class BaseTest(unittest.TestCase):
    """Base test cases to make sure things are returning accurate data."""

    def test_for_class_detils(self):
        # Make sure when the Warrior id is passed we get the correct data
        self.assertEqual(class_details(CLASS_WARRIOR),
        {'colour': CLASS_WARRIOR_COLOUR, 'name': CLASS_WARRIOR_NAME})

    def test_for_paladin_class(self):
        # Make sure when the Paladin id is passed we get the correct data
        self.assertEqual(class_details(CLASS_PALADIN),
        {'colour': CLASS_PALADIN_COLOUR, 'name': CLASS_PALADIN_NAME})

    def test_for_hunter_class(self):
        # Make sure when the Hunter id is passed we get the correct data
        self.assertEqual(class_details(CLASS_HUNTER),
        {'colour': CLASS_HUNTER_COLOUR, 'name': CLASS_HUNTER_NAME})

    def test_for_rogue_class(self):
        # Make sure when the Rogue id is passed we get the correct data
        self.assertEqual(class_details(CLASS_ROGUE),
        {'colour': CLASS_ROGUE_COLOUR, 'name': CLASS_ROGUE_NAME})

    def test_for_death_knight_class(self):
        # Make sure when the Death Knight id is passed we get the correct data
        self.assertEqual(class_details(CLASS_DEATH_KNIGHT),
        {'colour': CLASS_DEATH_KNIGHT_COLOUR, 'name': CLASS_DEATH_KNIGHT_NAME})

    def test_for_shaman_class(self):
        # Make sure when the Shaman id is passed we get the correct data
        self.assertEqual(class_details(CLASS_SHAMAN),
        {'colour': CLASS_SHAMAN_COLOUR, 'name': CLASS_SHAMAN_NAME})

    def test_for_mage_class(self):
        # Make sure when the Mage id is passed we get the correct data
        self.assertEqual(class_details(CLASS_MAGE),
        {'colour': CLASS_MAGE_COLOUR, 'name': CLASS_MAGE_NAME})

    def test_for_warlock_class(self):
        # Make sure when the Warlock id is passed we get the correct data
        self.assertEqual(class_details(CLASS_WARLOCK),
        {'colour': CLASS_WARLOCK_COLOUR, 'name': CLASS_WARLOCK_NAME})

    def test_for_monk_class(self):
        # Make sure when the Monk id is passed we get the correct data
        self.assertEqual(class_details(CLASS_WARLOCK),
        {'colour': CLASS_WARLOCK_COLOUR, 'name': CLASS_WARLOCK_NAME})

    def test_for_druid_class(self):
        # Make sure when the Druid id is passed we get the correct data
        self.assertEqual(class_details(CLASS_DRUID),
        {'colour': CLASS_DRUID_COLOUR, 'name': CLASS_DRUID_NAME})

    def test_for_demon_hunter_class(self):
        # Make sure when the Demon Hunter id is passed we get the correct data
        self.assertEqual(class_details(CLASS_DEMON_HUNTER),
        {'colour': CLASS_DEMON_HUNTER_COLOUR, 'name': CLASS_DEMON_HUNTER_NAME})

    def test_for_alliance_faction_name(self):
        # Makes sure that when the Alliance id is passed it gets 'Alliance' as the name.
        self.assertEqual(faction_details(FACTION_ALLIANCE), 'Alliance')

    def test_for_horde_faction_name(self):
        # Makes sure that when the Horde id is passed it gets 'Horde' as the name.'
        self.assertEqual(faction_details(FACTION_HORDE), 'Horde')


if __name__ == '__main__':
    unittest.main()
