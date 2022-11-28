from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self._ostokset = []

    def tavaroita_korissa(self):
        return len(self._ostokset)

    def hinta(self):
        return sum([x.hinta() for x in self._ostokset])

    def lisaa_tuote(self, lisattava: Tuote):
        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
