class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = [(player1_name, 0), (player2_name, 0)]

    def won_point(self, player_name):
        idx = list(map(lambda p: p[0], self.players)).index(player_name)
        self.players[idx] = (player_name, self.players[idx][1] + 1)

    def get_score(self):
        winning = max(self.players, key=lambda p: p[1])
        diff = abs(self.players[0][1] - self.players[1][1])
        if winning[1] < 4:
            if diff == 0:
                return f"{['Love', 'Fifteen', 'Thirty', 'Forty'][winning[1]]}-All"
            return "-".join([['Love', 'Fifteen', 'Thirty', 'Forty'][player[1]] for player in self.players])
        return f"Win for {winning[0]}" if diff > 1 else ["Deuce", f"Advantage {winning[0]}"][diff]
