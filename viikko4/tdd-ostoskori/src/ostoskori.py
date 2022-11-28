from tuote import Tuote
from ostos import Ostos
from typing import List


class Ostoskori:
    def __init__(self):
        self._ostokset: Dict[Tuote, List[Ostos]] = {}

    def tavaroita_korissa(self):
        return sum([x.lukumaara() for x in self._ostokset.values()])

    def hinta(self):
        return sum([x.hinta() for x in self._ostokset.values()])

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava in self._ostokset:
            self._ostokset[lisattava].muuta_lukumaaraa(1)
        else:
            self._ostokset[lisattava] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        if poistettava in self._ostokset:
            self._ostokset[poistettava].muuta_lukumaaraa(-1)

    def tyhjenna(self):
        self._ostokset = {}

    def ostokset(self) -> List[Ostos]:
        return [i for i in self._ostokset.values()]
