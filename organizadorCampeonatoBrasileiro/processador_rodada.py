from typing import List
from organizadorCampeonatoBrasileiro.partida import Partida


class ProcessarRodada:
    """Objeto-método que encapsula a lógica de processamento de uma rodada.
    
    Esta classe implementa o padrão "Replace Method with Method Object" (Substituir Método por Objeto-Método).
    Cada instância representa uma execução específica do processamento de rodada.
    """
    
    def __init__(self, partidas: List[Partida], processador: 'ProcessadorRodada'):
        """Inicializa o objeto-método com as partidas e referência ao processador.
        
        Args:
            partidas (List[Partida]): Lista de partidas da rodada a serem processadas.
            processador (ProcessadorRodada): Referência ao processador para acessar/atualizar estado.
        """
        self.partidas = partidas
        self.processador = processador
        self.partidas_finalizadas = []
    
    def executar(self) -> None:
        """Executa o processamento completo da rodada.
        
        Raises:
            ValueError: Se a lista de partidas estiver vazia.
            ValueError: Se alguma partida não estiver finalizada.
        """
        self._validar_partidas()
        self._processar_cada_partida()
        self._atualizar_historico()
    
    def _validar_partidas(self) -> None:
        """Valida se a lista de partidas está válida para processamento.
        
        Raises:
            ValueError: Se a lista de partidas estiver vazia.
        """
        if not self.partidas:
            raise ValueError("Lista de partidas não pode estar vazia")
    
    def _processar_cada_partida(self) -> None:
        """Processa cada partida individualmente.
        
        Raises:
            ValueError: Se alguma partida não estiver finalizada.
        """
        for partida in self.partidas:
            self._validar_partida_finalizada(partida)
            resultado_partida = self._criar_resumo_partida(partida)
            self.partidas_finalizadas.append(resultado_partida)
    
    def _validar_partida_finalizada(self, partida: Partida) -> None:
        """Valida se uma partida foi finalizada.
        
        Args:
            partida (Partida): A partida a ser validada.
            
        Raises:
            ValueError: Se a partida não estiver finalizada.
        """
        if not partida.finalizada:
            raise ValueError(
                f"Partida {partida.mandante.nome} vs {partida.visitante.nome} não foi finalizada"
            )
    
    def _criar_resumo_partida(self, partida: Partida) -> dict:
        """Cria um resumo estruturado de uma partida processada.
        
        Args:
            partida (Partida): A partida a ser resumida.
            
        Returns:
            dict: Dicionário com informações da partida processada.
        """
        return {
            'mandante': partida.mandante.nome,
            'visitante': partida.visitante.nome,
            'placar': f"{partida.gols_mandante}x{partida.gols_visitante}",
            'resultado': self._determinar_resultado(partida)
        }
    
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
    
    def _atualizar_historico(self) -> None:
        """Atualiza o histórico de partidas processadas no processador."""
        self.processador.partidas_processadas.extend(self.partidas_finalizadas)


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
        
        Este método utiliza o padrão "Substituir Método por Objeto-Método",
        delegando o processamento para a classe ProcessarRodada.
        
        Args:
            partidas (List[Partida]): Lista de partidas da rodada a serem processadas.
            
        Raises:
            ValueError: Se alguma partida não estiver finalizada.
            ValueError: Se a lista de partidas estiver vazia.
        """
        processar = ProcessarRodada(partidas, self)
        processar.executar()
    
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