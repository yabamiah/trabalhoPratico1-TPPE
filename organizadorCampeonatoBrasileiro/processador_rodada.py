from typing import List
from organizadorCampeonatoBrasileiro.partida import Partida


class ProcessadorRodada:
    """Responsável pelo processamento de resultados de uma rodada completa.
    
    Esta classe implementa a lógica do Membro 3: Processamento de Resultados e Estatísticas.
    Recebe uma lista de partidas de uma rodada e atualiza as estatísticas dos times.
    """
    
    def __init__(self):
        """Inicializa o processador de rodada."""
        self.partidas_processadas = []
    
    def processar_rodada(self, partidas: List[Partida]) -> None:
        """Processa uma lista de partidas de uma rodada.
        
        Args:
            partidas (List[Partida]): Lista de partidas da rodada a serem processadas.
            
        Raises:
            ValueError: Se alguma partida não estiver finalizada.
            ValueError: Se a lista de partidas estiver vazia.
        """
        if not partidas:
            raise ValueError("Lista de partidas não pode estar vazia")
            
        partidas_finalizadas = []
        
        for partida in partidas:
            if not partida.finalizada:
                raise ValueError(f"Partida {partida.mandante.nome} vs {partida.visitante.nome} não foi finalizada")
            
            partidas_finalizadas.append({
                'mandante': partida.mandante.nome,
                'visitante': partida.visitante.nome,
                'placar': f"{partida.gols_mandante}x{partida.gols_visitante}",
                'resultado': self._determinar_resultado(partida)
            })
        
        self.partidas_processadas.extend(partidas_finalizadas)
    
    def _determinar_resultado(self, partida: Partida) -> str:
        """Determina o resultado da partida do ponto de vista do mandante.
        
        Args:
            partida (Partida): A partida a ser analisada.
            
        Returns:
            str: 'vitoria', 'empate' ou 'derrota' do ponto de vista do mandante.
        """
        if partida.gols_mandante > partida.gols_visitante:
            return 'vitoria'
        elif partida.gols_mandante == partida.gols_visitante:
            return 'empate'
        else:
            return 'derrota'
    
    def obter_resumo_rodada(self) -> dict:
        """Retorna um resumo estatístico da última rodada processada.
        
        Returns:
            dict: Resumo com estatísticas da rodada.
        """
        if not self.partidas_processadas:
            return {'total_partidas': 0, 'total_gols': 0, 'vitorias': 0, 'empates': 0, 'derrotas': 0}
        
        total_partidas = len(self.partidas_processadas)
        vitorias = sum(1 for p in self.partidas_processadas if p['resultado'] == 'vitoria')
        empates = sum(1 for p in self.partidas_processadas if p['resultado'] == 'empate')
        derrotas = sum(1 for p in self.partidas_processadas if p['resultado'] == 'derrota')
        
        # Conta total de gols (soma dos placares)
        total_gols = 0
        for p in self.partidas_processadas:
            placar = p['placar'].split('x')
            total_gols += int(placar[0]) + int(placar[1])
        
        return {
            'total_partidas': total_partidas,
            'total_gols': total_gols,
            'vitorias': vitorias,
            'empates': empates,
            'derrotas': derrotas
        }
    
    def limpar_historico(self) -> None:
        """Limpa o histórico de partidas processadas."""
        self.partidas_processadas.clear()