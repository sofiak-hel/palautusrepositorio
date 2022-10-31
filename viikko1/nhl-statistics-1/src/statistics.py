from player_reader import PlayerReader
from player import SortBy


def sort_by_points(player, sort_criteria=None):
    if sort_criteria is SortBy.ASSISTS:
        return player.assists
    if sort_criteria is SortBy.GOALS:
        return player.goals
    return player.points


class Statistics:
    def __init__(self, reader):
        self.reader = reader

        self._players = self.reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_criteria=None):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda player: sort_by_points(player, sort_criteria)
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
