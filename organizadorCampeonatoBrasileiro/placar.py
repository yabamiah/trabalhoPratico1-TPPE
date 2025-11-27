class Placar:
    """Representa o placar de uma partida de futebol.
    
    Esta classe foi extraída da classe Partida através da refatoração "Extrair Classe".
    Responsável por gerenciar os gols marcados por cada time e o estado de finalização.
    
    Atributos:
        gols_mandante (int): Gols marcados pelo time mandante.
        gols_visitante (int): Gols marcados pelo time visitante.
        finalizado (bool): Indica se o placar foi registrado e finalizado.
    """
    
    def __init__(self):
        """Inicializa um placar vazio."""
        self.gols_mandante = 0
        self.gols_visitante = 0
        self.finalizado = False
    
    def registrar(self, gols_mandante: int, gols_visitante: int) -> None:
        """Registra o placar da partida.
        
        Args:
            gols_mandante (int): Número de gols marcados pelo time mandante.
            gols_visitante (int): Número de gols marcados pelo time visitante.
            
        Raises:
            ValueError: Se o placar já foi registrado anteriormente.
            ValueError: Se algum valor de gols for negativo.
        """
        if self.finalizado:
            raise ValueError("Placar já registrado para esta partida")
        
        self._validar_gols(gols_mandante, gols_visitante)
        
        self.gols_mandante = gols_mandante
        self.gols_visitante = gols_visitante
        self.finalizado = True
    
    def _validar_gols(self, gols_mandante: int, gols_visitante: int) -> None:
        """Valida se os valores de gols são válidos.
        
        Args:
            gols_mandante (int): Gols do mandante a serem validados.
            gols_visitante (int): Gols do visitante a serem validados.
            
        Raises:
            ValueError: Se algum valor de gols for negativo.
        """
        if gols_mandante < 0 or gols_visitante < 0:
            raise ValueError("Gols não podem ser negativos")
    
    def obter_resultado(self) -> str:
        """Determina o resultado da partida do ponto de vista do mandante.
        
        Returns:
            str: 'vitoria' se mandante venceu, 'empate' se empatou, 'derrota' se perdeu.
            
        Raises:
            ValueError: Se o placar não foi finalizado.
        """
        if not self.finalizado:
            raise ValueError("Placar não foi finalizado")
        
        if self.gols_mandante > self.gols_visitante:
            return 'vitoria'
        elif self.gols_mandante == self.gols_visitante:
            return 'empate'
        else:
            return 'derrota'
    
    def obter_placar_formatado(self) -> str:
        """Retorna o placar formatado como string.
        
        Returns:
            str: Placar no formato "X x Y".
        """
        return f"{self.gols_mandante}x{self.gols_visitante}"
    
    def total_gols(self) -> int:
        """Calcula o total de gols da partida.
        
        Returns:
            int: Soma dos gols de ambos os times.
        """
        return self.gols_mandante + self.gols_visitante
