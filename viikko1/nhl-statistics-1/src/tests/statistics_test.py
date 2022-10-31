import unittest
from statistics import Statistics
from player_reader import PlayerReader
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_player_works(self):
        found = self.statistics.search("Kurri")
        self.assertNotEqual(found, None)
        self.assertEqual(found.name, "Kurri")
        self.assertEqual(found.team, "EDM")
        self.assertEqual(found.goals, 37)
        self.assertEqual(found.assists, 53)

        self.assertTrue(self.statistics.search("Something else") is None)

    def test_team(self):
        found = self.statistics.team("EDM")
        self.assertEqual(len(found), 3)

    def test_top(self):
        found = self.statistics.top(3)
        self.assertEqual(len(found), 4)
        self.assertEqual(found[0].name, "Gretzky")
