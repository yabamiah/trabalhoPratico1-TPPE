import unittest
import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from organizadorCampeonatoBrasileiro.placar import Placar


class TestPlacar(unittest.TestCase):
    """Testes para a classe Placar extraída da classe Partida.
    
    Esta classe testa a refatoração "Extrair Classe" aplicada à classe Partida.
    """

    def setUp(self):
        """Configura um placar para os testes."""
        self.placar = Placar()

    def test_placar_inicializado_vazio(self):
        """Testa se o placar é inicializado com valores zerados."""
        self.assertEqual(self.placar.gols_mandante, 0)
        self.assertEqual(self.placar.gols_visitante, 0)
        self.assertFalse(self.placar.finalizado)

    def test_registrar_placar_vitoria_mandante(self):
        """Testa o registro de um placar com vitória do mandante."""
        self.placar.registrar(3, 1)
        
        self.assertEqual(self.placar.gols_mandante, 3)
        self.assertEqual(self.placar.gols_visitante, 1)
        self.assertTrue(self.placar.finalizado)

    def test_registrar_placar_empate(self):
        """Testa o registro de um placar empatado."""
        self.placar.registrar(2, 2)
        
        self.assertEqual(self.placar.gols_mandante, 2)
        self.assertEqual(self.placar.gols_visitante, 2)
        self.assertTrue(self.placar.finalizado)

    def test_registrar_placar_vitoria_visitante(self):
        """Testa o registro de um placar com vitória do visitante."""
        self.placar.registrar(0, 3)
        
        self.assertEqual(self.placar.gols_mandante, 0)
        self.assertEqual(self.placar.gols_visitante, 3)
        self.assertTrue(self.placar.finalizado)

    def test_registrar_placar_ja_finalizado_deve_falhar(self):
        """Testa se tentar registrar novamente um placar já finalizado gera erro."""
        self.placar.registrar(2, 1)
        
        with self.assertRaises(ValueError) as context:
            self.placar.registrar(1, 0)
        
        self.assertIn("Placar já registrado", str(context.exception))

    def test_registrar_gols_negativos_deve_falhar(self):
        """Testa se gols negativos geram erro."""
        with self.assertRaises(ValueError) as context:
            self.placar.registrar(-1, 2)
        
        self.assertIn("Gols não podem ser negativos", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            self.placar.registrar(2, -1)
        
        self.assertIn("Gols não podem ser negativos", str(context.exception))

    def test_obter_resultado_vitoria(self):
        """Testa se o resultado é 'vitoria' quando mandante vence."""
        self.placar.registrar(3, 1)
        resultado = self.placar.obter_resultado()
        
        self.assertEqual(resultado, 'vitoria')

    def test_obter_resultado_empate(self):
        """Testa se o resultado é 'empate' quando há empate."""
        self.placar.registrar(2, 2)
        resultado = self.placar.obter_resultado()
        
        self.assertEqual(resultado, 'empate')

    def test_obter_resultado_derrota(self):
        """Testa se o resultado é 'derrota' quando mandante perde."""
        self.placar.registrar(1, 3)
        resultado = self.placar.obter_resultado()
        
        self.assertEqual(resultado, 'derrota')

    def test_obter_resultado_sem_finalizar_deve_falhar(self):
        """Testa se obter resultado sem finalizar o placar gera erro."""
        with self.assertRaises(ValueError) as context:
            self.placar.obter_resultado()
        
        self.assertIn("Placar não foi finalizado", str(context.exception))

    def test_obter_placar_formatado(self):
        """Testa a formatação do placar como string."""
        self.placar.registrar(3, 2)
        placar_formatado = self.placar.obter_placar_formatado()
        
        self.assertEqual(placar_formatado, "3x2")

    def test_total_gols(self):
        """Testa o cálculo do total de gols da partida."""
        self.placar.registrar(4, 3)
        total = self.placar.total_gols()
        
        self.assertEqual(total, 7)

    def test_total_gols_partida_sem_gols(self):
        """Testa o total de gols em uma partida sem gols."""
        self.placar.registrar(0, 0)
        total = self.placar.total_gols()
        
        self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()
