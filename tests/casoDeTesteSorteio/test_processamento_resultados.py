import unittest
import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from organizadorCampeonatoBrasileiro.time import Time
from organizadorCampeonatoBrasileiro.partida import Partida
from organizadorCampeonatoBrasileiro.processador_rodada import ProcessadorRodada


class TestProcessamentoResultados(unittest.TestCase):
    """Testes para o processamento de resultados e atualização de estatísticas.
    
    Responsabilidade do Membro 3: Processamento de Resultados e Estatísticas.
    """

    def setUp(self):
        """Configura times para os testes."""
        self.time_a = Time("Flamengo")
        self.time_b = Time("Palmeiras")
        self.time_c = Time("São Paulo")
        self.time_d = Time("Corinthians")

    def test_cenario_vitoria_time_vencedor_recebe_3_pontos_perdedor_0(self):
        """Teste para cenário de vitória: time vencedor recebe 3 pontos, perdedor 0."""
        # Arrange
        partida = Partida(self.time_a, self.time_b)
        
        # Estado inicial dos times
        self.assertEqual(self.time_a.pontos, 0)
        self.assertEqual(self.time_a.vitorias, 0)
        self.assertEqual(self.time_a.gols_marcados, 0)
        self.assertEqual(self.time_a.gols_sofridos, 0)
        self.assertEqual(self.time_a.saldo_gols, 0)
        
        self.assertEqual(self.time_b.pontos, 0)
        self.assertEqual(self.time_b.vitorias, 0)
        self.assertEqual(self.time_b.gols_marcados, 0)
        self.assertEqual(self.time_b.gols_sofridos, 0)
        self.assertEqual(self.time_b.saldo_gols, 0)
        
        # Act - Flamengo vence Palmeiras por 3x1
        partida.registrar_placar(3, 1)
        
        # Assert - Verificar estatísticas do time vencedor (Flamengo)
        self.assertEqual(self.time_a.pontos, 3, "Time vencedor deve receber 3 pontos")
        self.assertEqual(self.time_a.vitorias, 1, "Time vencedor deve ter 1 vitória")
        self.assertEqual(self.time_a.gols_marcados, 3, "Time vencedor deve ter 3 gols marcados")
        self.assertEqual(self.time_a.gols_sofridos, 1, "Time vencedor deve ter 1 gol sofrido")
        self.assertEqual(self.time_a.saldo_gols, 2, "Saldo de gols deve ser +2")
        
        # Assert - Verificar estatísticas do time perdedor (Palmeiras)
        self.assertEqual(self.time_b.pontos, 0, "Time perdedor deve receber 0 pontos")
        self.assertEqual(self.time_b.vitorias, 0, "Time perdedor não deve ter vitórias")
        self.assertEqual(self.time_b.gols_marcados, 1, "Time perdedor deve ter 1 gol marcado")
        self.assertEqual(self.time_b.gols_sofridos, 3, "Time perdedor deve ter 3 gols sofridos")
        self.assertEqual(self.time_b.saldo_gols, -2, "Saldo de gols deve ser -2")

    def test_cenario_empate_ambos_times_recebem_1_ponto(self):
        """Teste para cenário de empate: ambos os times recebem 1 ponto."""
        # Arrange
        partida = Partida(self.time_c, self.time_d)
        
        # Estado inicial dos times
        self.assertEqual(self.time_c.pontos, 0)
        self.assertEqual(self.time_c.vitorias, 0)
        self.assertEqual(self.time_d.pontos, 0)
        self.assertEqual(self.time_d.vitorias, 0)
        
        # Act - São Paulo empata com Corinthians por 2x2
        partida.registrar_placar(2, 2)
        
        # Assert - Verificar estatísticas do time mandante (São Paulo)
        self.assertEqual(self.time_c.pontos, 1, "Time em empate deve receber 1 ponto")
        self.assertEqual(self.time_c.vitorias, 0, "Time em empate não deve ter vitórias")
        self.assertEqual(self.time_c.gols_marcados, 2, "Time mandante deve ter 2 gols marcados")
        self.assertEqual(self.time_c.gols_sofridos, 2, "Time mandante deve ter 2 gols sofridos")
        self.assertEqual(self.time_c.saldo_gols, 0, "Saldo de gols deve ser 0")
        
        # Assert - Verificar estatísticas do time visitante (Corinthians)
        self.assertEqual(self.time_d.pontos, 1, "Time em empate deve receber 1 ponto")
        self.assertEqual(self.time_d.vitorias, 0, "Time em empate não deve ter vitórias")
        self.assertEqual(self.time_d.gols_marcados, 2, "Time visitante deve ter 2 gols marcados")
        self.assertEqual(self.time_d.gols_sofridos, 2, "Time visitante deve ter 2 gols sofridos")
        self.assertEqual(self.time_d.saldo_gols, 0, "Saldo de gols deve ser 0")

    def test_cenario_derrota_time_perdedor_nao_recebe_pontos(self):
        """Teste explícito para cenário de derrota: time perdedor não recebe pontos."""
        # Arrange
        time_vencedor = Time("Atlético-MG")
        time_perdedor = Time("Cruzeiro")
        partida = Partida(time_perdedor, time_vencedor)  # Perdedor como mandante
        
        # Act - Cruzeiro perde para Atlético-MG por 0x4
        partida.registrar_placar(0, 4)
        
        # Assert - Verificar estatísticas do time perdedor (mandante)
        self.assertEqual(time_perdedor.pontos, 0, "Time perdedor não deve receber pontos")
        self.assertEqual(time_perdedor.vitorias, 0, "Time perdedor não deve ter vitórias")
        self.assertEqual(time_perdedor.gols_marcados, 0, "Time perdedor não marcou gols")
        self.assertEqual(time_perdedor.gols_sofridos, 4, "Time perdedor sofreu 4 gols")
        self.assertEqual(time_perdedor.saldo_gols, -4, "Saldo de gols deve ser -4")
        
        # Assert - Verificar estatísticas do time vencedor (visitante)
        self.assertEqual(time_vencedor.pontos, 3, "Time vencedor deve receber 3 pontos")
        self.assertEqual(time_vencedor.vitorias, 1, "Time vencedor deve ter 1 vitória")
        self.assertEqual(time_vencedor.gols_marcados, 4, "Time vencedor marcou 4 gols")
        self.assertEqual(time_vencedor.gols_sofridos, 0, "Time vencedor não sofreu gols")
        self.assertEqual(time_vencedor.saldo_gols, 4, "Saldo de gols deve ser +4")

    def test_processamento_rodada_completa_multiplas_partidas(self):
        """Teste de integração: processamento de uma rodada completa com múltiplas partidas."""
        # Arrange - Criar times para uma mini rodada
        flamengo = Time("Flamengo")
        palmeiras = Time("Palmeiras")
        sao_paulo = Time("São Paulo")
        corinthians = Time("Corinthians")
        santos = Time("Santos")
        vasco = Time("Vasco")
        
        # Criar partidas da rodada
        partidas = [
            Partida(flamengo, palmeiras),     # Flamengo 2x1 Palmeiras (vitória Flamengo)
            Partida(sao_paulo, corinthians),  # São Paulo 1x1 Corinthians (empate)
            Partida(santos, vasco)            # Santos 0x3 Vasco (vitória Vasco)
        ]
        
        # Registrar placares
        partidas[0].registrar_placar(2, 1)  # Flamengo vence
        partidas[1].registrar_placar(1, 1)  # Empate
        partidas[2].registrar_placar(0, 3)  # Vasco vence
        
        # Criar processador
        processador = ProcessadorRodada()
        
        # Act - Processar a rodada
        processador.processar_rodada(partidas)
        
        # Assert - Verificar estatísticas individuais dos times
        # Flamengo (venceu)
        self.assertEqual(flamengo.pontos, 3)
        self.assertEqual(flamengo.vitorias, 1)
        self.assertEqual(flamengo.gols_marcados, 2)
        self.assertEqual(flamengo.gols_sofridos, 1)
        self.assertEqual(flamengo.saldo_gols, 1)
        
        # Palmeiras (perdeu)
        self.assertEqual(palmeiras.pontos, 0)
        self.assertEqual(palmeiras.vitorias, 0)
        self.assertEqual(palmeiras.gols_marcados, 1)
        self.assertEqual(palmeiras.gols_sofridos, 2)
        self.assertEqual(palmeiras.saldo_gols, -1)
        
        # São Paulo (empatou)
        self.assertEqual(sao_paulo.pontos, 1)
        self.assertEqual(sao_paulo.vitorias, 0)
        self.assertEqual(sao_paulo.gols_marcados, 1)
        self.assertEqual(sao_paulo.gols_sofridos, 1)
        self.assertEqual(sao_paulo.saldo_gols, 0)
        
        # Corinthians (empatou)
        self.assertEqual(corinthians.pontos, 1)
        self.assertEqual(corinthians.vitorias, 0)
        self.assertEqual(corinthians.gols_marcados, 1)
        self.assertEqual(corinthians.gols_sofridos, 1)
        self.assertEqual(corinthians.saldo_gols, 0)
        
        # Santos (perdeu)
        self.assertEqual(santos.pontos, 0)
        self.assertEqual(santos.vitorias, 0)
        self.assertEqual(santos.gols_marcados, 0)
        self.assertEqual(santos.gols_sofridos, 3)
        self.assertEqual(santos.saldo_gols, -3)
        
        # Vasco (venceu)
        self.assertEqual(vasco.pontos, 3)
        self.assertEqual(vasco.vitorias, 1)
        self.assertEqual(vasco.gols_marcados, 3)
        self.assertEqual(vasco.gols_sofridos, 0)
        self.assertEqual(vasco.saldo_gols, 3)
        
        # Assert - Verificar resumo da rodada
        resumo = processador.obter_resumo_rodada()
        self.assertEqual(resumo['total_partidas'], 3)
        self.assertEqual(resumo['total_gols'], 8)  # 2+1+1+1+0+3 = 8 gols
        self.assertEqual(resumo['vitorias'], 1)    # Apenas Flamengo venceu como mandante
        self.assertEqual(resumo['empates'], 1)     # São Paulo x Corinthians
        self.assertEqual(resumo['derrotas'], 1)    # Santos perdeu como mandante

    def test_processamento_rodada_vazia_deve_falhar(self):
        """Teste para verificar que processamento de rodada vazia deve falhar."""
        processador = ProcessadorRodada()
        
        with self.assertRaises(ValueError) as context:
            processador.processar_rodada([])
        
        self.assertIn("Lista de partidas não pode estar vazia", str(context.exception))

    def test_processamento_partida_nao_finalizada_deve_falhar(self):
        """Teste para verificar que partida não finalizada causa erro."""
        time_a = Time("Time A")
        time_b = Time("Time B")
        partida_nao_finalizada = Partida(time_a, time_b)
        # Não chamamos registrar_placar(), então partida.finalizada = False
        
        processador = ProcessadorRodada()
        
        with self.assertRaises(ValueError) as context:
            processador.processar_rodada([partida_nao_finalizada])
        
        self.assertIn("não foi finalizada", str(context.exception))


if __name__ == "__main__":
    unittest.main()