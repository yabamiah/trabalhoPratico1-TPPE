import unittest
import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from organizadorCampeonatoBrasileiro.time import Time
from organizadorCampeonatoBrasileiro.classificacao import ordenar_classificacao


class TestClassificacao(unittest.TestCase):
    def test_ordenacao_por_pontuacao(self):
        time_a = Time("Time A")
        time_a.pontos = 45
        
        time_b = Time("Time B")
        time_b.pontos = 38
        
        time_c = Time("Time C")
        time_c.pontos = 50
        
        times = [time_a, time_b, time_c]
        
        classificacao = ordenar_classificacao(times)
        
        self.assertEqual(classificacao[0].nome, "Time C")
        self.assertEqual(classificacao[1].nome, "Time A")
        self.assertEqual(classificacao[2].nome, "Time B")
    
    def test_desempate_por_vitorias(self):
        time_a = Time("Time A")
        time_a.pontos = 45
        time_a.vitorias = 14
        
        time_b = Time("Time B")
        time_b.pontos = 45
        time_b.vitorias = 12
        
        times = [time_b, time_a]
        
        classificacao = ordenar_classificacao(times)
        
        self.assertEqual(classificacao[0].nome, "Time A")
        self.assertEqual(classificacao[1].nome, "Time B")
    
    def test_classificacao_combinada(self):
        time_a = Time("Time A")
        time_a.pontos = 45
        time_a.vitorias = 14
        
        time_b = Time("Time B")
        time_b.pontos = 38
        time_b.vitorias = 11
        
        time_c = Time("Time C")
        time_c.pontos = 50
        time_c.vitorias = 16
        
        time_d = Time("Time D")
        time_d.pontos = 45
        time_d.vitorias = 13
        
        time_e = Time("Time E")
        time_e.pontos = 38
        time_e.vitorias = 12
        
        times = [time_b, time_d, time_a, time_e, time_c]
        
        classificacao = ordenar_classificacao(times)
        
        self.assertEqual(classificacao[0].nome, "Time C")
        self.assertEqual(classificacao[1].nome, "Time A")
        self.assertEqual(classificacao[2].nome, "Time D")
        self.assertEqual(classificacao[3].nome, "Time E")
        self.assertEqual(classificacao[4].nome, "Time B")


if __name__ == "__main__":
    unittest.main()
