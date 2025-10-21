import unittest

from organizadorCampeonatoBrasileiro.time import Time


class TestTime(unittest.TestCase):
    def test_time_criado_com_nome(self):
        time = Time("Flamengo")
        self.assertEqual(time.nome, "Flamengo")


if __name__ == "__main__":
    unittest.main()