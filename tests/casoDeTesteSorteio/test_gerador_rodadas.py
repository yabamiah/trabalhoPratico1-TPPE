import unittest
import sys
import os

# Adiciona o diretório pai ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from organizadorCampeonatoBrasileiro.campeonato import Campeonato


class TestGeradorRodadas(unittest.TestCase):
    """Testes para validar a lógica de geração de rodadas do campeonato."""

    def setUp(self):
        """Configuração inicial para os testes."""
        self.times_teste = [
            "Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Grêmio", "Internacional",
            "Atlético-MG", "Cruzeiro", "Fluminense", "Vasco", "Botafogo", "Santos",
            "Bahia", "Vitória", "Mirassol", "Juventude", "Bragantino", "Ceará",
            "Fortaleza", "Sport Recife"
        ]
        self.campeonato = Campeonato(self.times_teste)

    def test_gera_exatamente_38_rodadas(self):
        """Teste que verifica se o algoritmo gera exatamente 38 rodadas."""
        self.campeonato.gerar_rodadas()
        
        # O campeonato deve ter 38 rodadas (19 do turno + 19 do returno)
        self.assertEqual(len(self.campeonato.jogos), 38, 
                        "O campeonato deve ter exatamente 38 rodadas")

    def test_cada_rodada_contem_10_partidas_com_todos_os_times(self):
        """Teste para garantir que cada rodada contenha 10 partidas, envolvendo todos os 20 times."""
        self.campeonato.gerar_rodadas()
        
        for i, rodada in enumerate(self.campeonato.jogos):
            # Cada rodada deve ter 10 partidas (20 times / 2 = 10 partidas por rodada)
            self.assertEqual(len(rodada), 10, 
                           f"A rodada {i+1} deve ter exatamente 10 partidas")
            
            # Verificar se todos os 20 times estão presentes na rodada
            times_na_rodada = set()
            for mandante, visitante in rodada:
                times_na_rodada.add(mandante)
                times_na_rodada.add(visitante)
            
            self.assertEqual(len(times_na_rodada), 20, 
                           f"A rodada {i+1} deve envolver todos os 20 times")
            self.assertEqual(times_na_rodada, set(self.times_teste), 
                           f"A rodada {i+1} deve conter exatamente os times do campeonato")

    def test_time_nao_joga_contra_si_mesmo(self):
        """Teste para garantir que um time não jogue contra si mesmo."""
        self.campeonato.gerar_rodadas()
        
        for i, rodada in enumerate(self.campeonato.jogos):
            for mandante, visitante in rodada:
                self.assertNotEqual(mandante, visitante, 
                                  f"Na rodada {i+1}, {mandante} não pode jogar contra si mesmo")

    def test_cada_confronto_ocorre_exatamente_uma_vez_como_mandante_visitante(self):
        """Teste crítico para validar que, ao final das 38 rodadas, 
        o jogo Time A vs Time B (mandante vs visitante) ocorreu exatamente uma vez."""
        self.campeonato.gerar_rodadas()
        
        # Dicionário para contar quantas vezes cada confronto (mandante vs visitante) ocorre
        confrontos = {}
        
        for rodada in self.campeonato.jogos:
            for mandante, visitante in rodada:
                confronto = (mandante, visitante)
                confrontos[confronto] = confrontos.get(confronto, 0) + 1
        
        # Verificar se cada possível confronto (A vs B) ocorre exatamente uma vez
        for time_a in self.times_teste:
            for time_b in self.times_teste:
                if time_a != time_b:
                    confronto = (time_a, time_b)
                    self.assertEqual(confrontos.get(confronto, 0), 1, 
                                   f"O confronto {time_a} vs {time_b} deve ocorrer exatamente uma vez")

    def test_total_de_partidas_e_380(self):
        """Teste adicional para verificar o total de partidas no campeonato."""
        self.campeonato.gerar_rodadas()
        
        total_partidas = sum(len(rodada) for rodada in self.campeonato.jogos)
        # 20 times, cada time joga 38 partidas, total = 20 * 38 / 2 = 380 partidas
        self.assertEqual(total_partidas, 380, 
                        "O campeonato deve ter 380 partidas no total")

    def test_cada_time_joga_38_partidas(self):
        """Teste para verificar se cada time joga exatamente 38 partidas."""
        self.campeonato.gerar_rodadas()
        
        # Contar quantas partidas cada time joga
        partidas_por_time = {time: 0 for time in self.times_teste}
        
        for rodada in self.campeonato.jogos:
            for mandante, visitante in rodada:
                partidas_por_time[mandante] += 1
                partidas_por_time[visitante] += 1
        
        for time in self.times_teste:
            self.assertEqual(partidas_por_time[time], 38, 
                           f"{time} deve jogar exatamente 38 partidas")

    def test_cada_time_joga_19_partidas_como_mandante(self):
        """Teste para verificar se cada time joga exatamente 19 partidas como mandante."""
        self.campeonato.gerar_rodadas()
        
        # Contar quantas partidas como mandante cada time joga
        mandante_por_time = {time: 0 for time in self.times_teste}
        
        for rodada in self.campeonato.jogos:
            for mandante, visitante in rodada:
                mandante_por_time[mandante] += 1
        
        for time in self.times_teste:
            self.assertEqual(mandante_por_time[time], 19, 
                           f"{time} deve jogar exatamente 19 partidas como mandante")


if __name__ == '__main__':
    unittest.main()