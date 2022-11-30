## Historiasta löytyy luettavempi versio.
g = [['Love', 'Fifteen', 'Thirty', 'Forty'], 'Deuce', ['Advantage ', 'Win for ']]
class TennisGame:
    def __init__(self, player1_name, player2_name):
        [self.p, self.s] = [[player1_name, player2_name], [0, 0]]
    def won_point(self, pn):
        self.s[self.p.index(pn)] += 1
    def get_score(t):
        if max(t.s) < 4:
            return f"{[g[0][i] for i in t.s][0]}-All" if t.s[0] == t.s[1] else "-".join([g[0][i] for i in t.s])
        return g[1] if t.s[0] == t.s[1] else g[2][min(max(t.s) - min(t.s) - 1, 1)] + t.p[t.s.index(max(t.s))]
