import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from organizadorCampeonatoBrasileiro.time import Time
from organizadorCampeonatoBrasileiro.partida import Partida
from organizadorCampeonatoBrasileiro.processador_rodada import ProcessadorRodada, ProcessarRodada


class TestRefatoracaoProcessador(unittest.TestCase):
    """Testes específicos para validar a refatoração com padrão Objeto-Método.
    
    Garante que a refatoração 'Substituir Método por Objeto-Método' foi aplicada
    corretamente e que o comportamento permanece o mesmo.
    """

    def test_objeto_metodo_processa_rodada_corretamente(self):
        """Testa que o objeto-método ProcessarRodada funciona corretamente."""
        time_a = Time("Time A")
        time_b = Time("Time B")
        
        partida = Partida(time_a, time_b)
        partida.registrar_placar(2, 1)
        
        processador = ProcessadorRodada()
        processar = ProcessarRodada([partida], processador)
        
        processar.executar()
        
        self.assertEqual(len(processador.partidas_processadas), 1)
        resultado = processador.partidas_processadas[0]
        self.assertEqual(resultado['mandante'], "Time A")
        self.assertEqual(resultado['visitante'], "Time B")
        self.assertEqual(resultado['placar'], "2x1")
        self.assertEqual(resultado['resultado'], 'vitoria')

    def test_objeto_metodo_determina_resultado_vitoria(self):
        """Testa se o objeto-método determina vitória corretamente."""
        time_mandante = Time("Mandante")
        time_visitante = Time("Visitante")
        
        partida = Partida(time_mandante, time_visitante)
        partida.registrar_placar(3, 1)
        
        processador = ProcessadorRodada()
        processar = ProcessarRodada([partida], processador)
        
        resultado = processar._determinar_resultado(partida)
        self.assertEqual(resultado, 'vitoria')

    def test_objeto_metodo_determina_resultado_empate(self):
        """Testa se o objeto-método determina empate corretamente."""
        time_mandante = Time("Mandante")
        time_visitante = Time("Visitante")
        
        partida = Partida(time_mandante, time_visitante)
        partida.registrar_placar(2, 2)
        
        processador = ProcessadorRodada()
        processar = ProcessarRodada([partida], processador)
        
        resultado = processar._determinar_resultado(partida)
        self.assertEqual(resultado, 'empate')

    def test_objeto_metodo_determina_resultado_derrota(self):
        """Testa se o objeto-método determina derrota corretamente."""
        time_mandante = Time("Mandante")
        time_visitante = Time("Visitante")
        
        partida = Partida(time_mandante, time_visitante)
        partida.registrar_placar(0, 3)
        
        processador = ProcessadorRodada()
        processar = ProcessarRodada([partida], processador)
        
        resultado = processar._determinar_resultado(partida)
        self.assertEqual(resultado, 'derrota')

    def test_processador_limpar_historico_funciona(self):
        """Testa se o método limpar_historico funciona após refatoração."""
        time_a = Time("Time A")
        time_b = Time("Time B")
        
        partida = Partida(time_a, time_b)
        partida.registrar_placar(1, 1)
        
        processador = ProcessadorRodada()
        processador.processar_rodada([partida])
        
        self.assertEqual(len(processador.partidas_processadas), 1)
        
        processador.limpar_historico()
        
        self.assertEqual(len(processador.partidas_processadas), 0)

    def test_processador_obter_resumo_apos_multiplas_rodadas(self):
        """Testa o resumo após processar múltiplas rodadas."""
        processador = ProcessadorRodada()
        
        for i in range(3):
            time_a = Time(f"Time A{i}")
            time_b = Time(f"Time B{i}")
            partida = Partida(time_a, time_b)
            partida.registrar_placar(i, i)
            processador.processar_rodada([partida])
        
        resumo = processador.obter_resumo_rodada()
        self.assertEqual(resumo['total_partidas'], 3)
        self.assertEqual(resumo['empates'], 3)

    def test_refatoracao_mantem_compatibilidade_com_testes_existentes(self):
        """Garante que a refatoração não quebrou a interface pública."""
        time_a = Time("Flamengo")
        time_b = Time("Palmeiras")
        
        partida = Partida(time_a, time_b)
        partida.registrar_placar(3, 0)
        
        processador = ProcessadorRodada()
        
        try:
            processador.processar_rodada([partida])
            interface_mantida = True
        except AttributeError:
            interface_mantida = False
        
        self.assertTrue(interface_mantida, "A interface pública deve ser mantida após refatoração")
        self.assertEqual(time_a.pontos, 3)
        self.assertEqual(time_b.pontos, 0)


if __name__ == "__main__":
    unittest.main()
