KAPASITEETTI = 5
OLETUSKASVATUS = 5


def val_or_default(value, default):
    if value is None:
        return default
    elif not isinstance(value, int) or value < 0:
        raise Exception("Väärä arvo")  # heitin vaan jotain :D
    return value


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = val_or_default(kapasiteetti, KAPASITEETTI)
        self.kasvatuskoko = val_or_default(kasvatuskoko, OLETUSKASVATUS)

        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, numero):
        return self.lukujono[:self.alkioiden_lkm].count(numero) > 0

    def lisaa(self, numero):
        if self.kuuluu(numero):
            return False

        self.lukujono[self.alkioiden_lkm] = numero
        self.alkioiden_lkm += 1
        if self.alkioiden_lkm >= len(self.lukujono):
            self.lukujono.extend([0] * self.kasvatuskoko)
        return True

    def poista(self, numero):
        if self.kuuluu(numero):
            kohta = self.lukujono[:self.alkioiden_lkm].index(numero)
            uusi = self.lukujono[(kohta+1):self.alkioiden_lkm]
            for i in range(kohta, self.alkioiden_lkm):
                if len(uusi) > (i - kohta):
                    self.lukujono[i] = uusi[i - kohta]
                else:
                    self.lukujono[i] = 0
            self.alkioiden_lkm -= 1
            return True

        return False

    def suuruus(self):
        return self.alkioiden_lkm

    def to_list(self):
        return self.lukujono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        uusi_joukko = IntJoukko()
        for n in a.to_list() + b.to_list():
            uusi_joukko.lisaa(n)
        return uusi_joukko

    @staticmethod
    def leikkaus(a, b):
        uusi_joukko = IntJoukko()
        for n in a.to_list() + b.to_list():
            if a.kuuluu(n) and b.kuuluu(n):
                uusi_joukko.lisaa(n)
        return uusi_joukko

    @staticmethod
    def erotus(a, b):
        uusi_joukko = IntJoukko()
        for n in a.to_list():
            if not b.kuuluu(n):
                uusi_joukko.lisaa(n)
        return uusi_joukko

    def __str__(self):
        return f"{{{', '.join([str(x) for x in self.to_list()])}}}"
