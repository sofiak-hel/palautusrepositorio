import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    # osa 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # osa 2
    def test_yhden_tuotteen_lisaaminen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # osa 3
    def test_yhden_tuotteen_lisaaminen_vaikuttaa_hintaan(self):
        tuotteen_hinta = 3
        maito = Tuote("Maito", tuotteen_hinta)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), tuotteen_hinta)

    # osa 4
    def test_eri_tuotteilla_maara_2(self):
        maito = Tuote("Maito", 3)
        suklaa = Tuote("Suklaa", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # osa 5
    def test_eri_tuotteilla_yhteinen_hinta(self):
        tuotteen_hinnat = [3, 5]
        yhteishinta = sum(tuotteen_hinnat)

        maito = Tuote("Maito", tuotteen_hinnat[0])
        suklaa = Tuote("Suklaa", tuotteen_hinnat[1])
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)
        self.assertEqual(self.kori.hinta(), yhteishinta)

    # osa 6
    def test_kahden_saman_tuotteen_lisaaminen_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # osa 7
    def test_kahden_saman_tuotteen_lisaaminen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)

    # osa 8
    def test_yhden_tuotteen_lisaaminen_ostokset_len(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    # osa 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.hinta(), 3)
        self.assertEqual(ostos.lukumaara(), 1)

    # osa 10
    def test_kahden__eri_tuotteen_lisaaminen_len(self):
        maito = Tuote("Maito", 3)
        suklaa = Tuote("Suklaa", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)
        self.assertEqual(len(self.kori.ostokset()), 2)
