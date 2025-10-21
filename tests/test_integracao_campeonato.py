import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from organizadorCampeonatoBrasileiro.time import Time
from organizadorCampeonatoBrasileiro.partida import Partida
from organizadorCampeonatoBrasileiro.campeonato import Campeonato
from organizadorCampeonatoBrasileiro.processador_rodada import ProcessadorRodada
from organizadorCampeonatoBrasileiro.classificacao import ordenar_classificacao

class TestIntegracaoCampeonato(unittest.TestCase):

    def setUp(self):
        self.nomes_times = [
            "Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Grêmio", "Internacional",
            "Atlético-MG", "Cruzeiro", "Fluminense", "Vasco", "Botafogo", "Santos",
            "Bahia", "Vitória", "Mirassol", "Juventude", "Bragantino", "Ceará",
            "Fortaleza", "Sport Recife"
        ]
        
        self.times_dict = {nome: Time(nome) for nome in self.nomes_times}
        self.lista_times = list(self.times_dict.values())
        
        self.campeonato = Campeonato(self.nomes_times)
        
        self.processador = ProcessadorRodada()

    def test_simulacao_primeira_rodada_e_classificacao(self):
        self.campeonato.gerar_rodadas()
        rodada_1_jogos = self.campeonato.jogos[0]
        
        partidas_da_rodada = []
        
        placares_simulados = [
            (3, 0), (2, 1), (1, 0), (4, 2), (2, 0),
            (1, 1), (0, 0), (2, 2),
            (0, 1), (1, 3)
        ]

        for i, (nome_mandante, nome_visitante) in enumerate(rodada_1_jogos):
            mandante = self.times_dict[nome_mandante]
            visitante = self.times_dict[nome_visitante]
            
            partida = Partida(mandante, visitante)
            
            gols_m, gols_v = placares_simulados[i]
            partida.registrar_placar(gols_m, gols_v)
            
            partidas_da_rodada.append(partida)

        self.processador.processar_rodada(partidas_da_rodada)
        classificacao = ordenar_classificacao(self.lista_times)

        resumo = self.processador.obter_resumo_rodada()
        self.assertEqual(resumo['total_partidas'], 10)
        self.assertEqual(resumo['vitorias'], 5)
        self.assertEqual(resumo['empates'], 3)
        self.assertEqual(resumo['derrotas'], 2)
        self.assertEqual(resumo['total_gols'], 26)
        
        times_com_3_pontos = [t for t in classificacao if t.pontos == 3]
        times_com_1_ponto = [t for t in classificacao if t.pontos == 1]
        times_com_0_pontos = [t for t in classificacao if t.pontos == 0]

        self.assertEqual(len(times_com_3_pontos), 7)
        self.assertEqual(len(times_com_1_ponto), 6)
        self.assertEqual(len(times_com_0_pontos), 7)

        self.assertEqual(classificacao[0].pontos, 3)
        self.assertEqual(classificacao[0].saldo_gols, 3)
        
        self.assertEqual(classificacao[-1].pontos, 0)
        self.assertEqual(classificacao[-1].saldo_gols, -3)


    def test_simulacao_campeonato_inteiro_com_resultado_fixo(self):
        self.campeonato.gerar_rodadas()
        self.assertEqual(len(self.campeonato.jogos), 38)

        for rodada_jogos in self.campeonato.jogos:
            partidas_da_rodada = []
            for nome_mandante, nome_visitante in rodada_jogos:
                mandante = self.times_dict[nome_mandante]
                visitante = self.times_dict[nome_visitante]
                
                partida = Partida(mandante, visitante)
                
                partida.registrar_placar(1, 0)
                partidas_da_rodada.append(partida)
            
            self.processador.processar_rodada(partidas_da_rodada)
            self.processador.limpar_historico()
        
        classificacao_final = ordenar_classificacao(self.lista_times)
        
        primeiro_colocado = classificacao_final[0]
        ultimo_colocado = classificacao_final[-1]

        self.assertEqual(primeiro_colocado.pontos, 57)
        self.assertEqual(primeiro_colocado.vitorias, 19)
        self.assertEqual(primeiro_colocado.saldo_gols, 0)
        self.assertEqual(primeiro_colocado.gols_marcados, 19)
        self.assertEqual(primeiro_colocado.gols_sofridos, 19)
        
        self.assertEqual(ultimo_colocado.pontos, 57)
        self.assertEqual(ultimo_colocado.vitorias, 19)
        self.assertEqual(ultimo_colocado.saldo_gols, 0)
        self.assertEqual(ultimo_colocado.gols_marcados, 19)
        self.assertEqual(ultimo_colocado.gols_sofridos, 19)

if __name__ == "__main__":
    unittest.main()