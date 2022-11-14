import requests


class Player:
    def __init__(self, player_dict: dict):
        self.name: str = player_dict['name']
        self.nationality: str = player_dict['nationality']
        self.assists: int = player_dict['assists']
        self.goals: int = player_dict['goals']
        self.penalties: int = player_dict['penalties']
        self.team: str = player_dict['team']
        self.games: int = player_dict['games']

    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {self.goals + self.assists:2}"


class PlayerReader:
    def __init__(self, url="https://studies.cs.helsinki.fi/nhlstats/2021-22/players"):
        url = url
        response = requests.get(url).json()
        self.players = []
        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)


class PlayerStats:
    def __init__(self, reader=PlayerReader()):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        return [x for x in self.reader.players if x.nationality == nationality]
