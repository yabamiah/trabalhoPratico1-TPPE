import unittest
import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from organizadorCampeonatoBrasileiro.time import Time


class TestTime(unittest.TestCase):
    def test_time_criado_com_nome(self):
        time = Time("Flamengo")
        self.assertEqual(time.nome, "Flamengo")


if __name__ == "__main__":
    unittest.main()