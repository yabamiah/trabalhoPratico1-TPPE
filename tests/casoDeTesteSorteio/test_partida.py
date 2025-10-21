import unittest
import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import unittest
import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from organizadorCampeonatoBrasileiro.time import Time


class TestPartida(unittest.TestCase):
    def test_partida_criada_com_mandante_e_visitante(self):
        from organizadorCampeonatoBrasileiro.partida import Partida

        mandante = Time("Flamengo")
        visitante = Time("Palmeiras")
        partida = Partida(mandante, visitante)

        self.assertIs(partida.mandante, mandante)
        self.assertIs(partida.visitante, visitante)
        self.assertEqual(partida.gols_mandante, 0)
        self.assertEqual(partida.gols_visitante, 0)
        self.assertFalse(partida.finalizada)

    def test_registrar_placar_atualiza_times(self):
        from organizadorCampeonatoBrasileiro.partida import Partida

        mandante = Time("Flamengo")
        visitante = Time("Palmeiras")
        partida = Partida(mandante, visitante)

        partida.registrar_placar(2, 1)

        self.assertEqual(partida.gols_mandante, 2)
        self.assertEqual(partida.gols_visitante, 1)
        self.assertTrue(partida.finalizada)

        self.assertEqual(mandante.gols_marcados, 2)
        self.assertEqual(mandante.gols_sofridos, 1)
        self.assertEqual(mandante.vitorias, 1)
        self.assertEqual(mandante.pontos, 3)
        self.assertEqual(mandante.saldo_gols, 1)

        self.assertEqual(visitante.gols_marcados, 1)
        self.assertEqual(visitante.gols_sofridos, 2)
        self.assertEqual(visitante.vitorias, 0)
        self.assertEqual(visitante.pontos, 0)
        self.assertEqual(visitante.saldo_gols, -1)


if __name__ == "__main__":
    unittest.main()


