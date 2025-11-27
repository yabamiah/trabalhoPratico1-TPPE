from organizadorCampeonatoBrasileiro.time import Time
from organizadorCampeonatoBrasileiro.placar import Placar


class Partida:
    """Representa uma partida de futebol entre dois times.
    
    Esta classe foi refatorada usando "Extrair Classe" para delegar
    a responsabilidade de gerenciar o placar para a classe Placar.

    Atributos:
        mandante (Time): Time da casa.
        visitante (Time): Time visitante.
        placar (Placar): Objeto que gerencia o placar da partida.
    """

    def __init__(self, mandante: Time, visitante: Time):
        if mandante is None or visitante is None:
            raise ValueError("Mandante e visitante devem ser informados")

        self.mandante = mandante
        self.visitante = visitante
        self.placar = Placar()

    @property
    def gols_mandante(self) -> int:
        """Retorna os gols do mandante (mantido para compatibilidade)."""
        return self.placar.gols_mandante
    
    @property
    def gols_visitante(self) -> int:
        """Retorna os gols do visitante (mantido para compatibilidade)."""
        return self.placar.gols_visitante
    
    @property
    def finalizada(self) -> bool:
        """Retorna se a partida foi finalizada (mantido para compatibilidade)."""
        return self.placar.finalizado

    def registrar_placar(self, gols_mandante: int, gols_visitante: int) -> None:
        """Registra o placar da partida e atualiza as estatísticas dos times.
        
        Args:
            gols_mandante (int): Gols marcados pelo time mandante.
            gols_visitante (int): Gols marcados pelo time visitante.
            
        Raises:
            ValueError: Se o placar já foi registrado ou se gols forem negativos.
        """
        # Delega o registro do placar para a classe Placar
        self.placar.registrar(gols_mandante, gols_visitante)

        # Atualiza estatísticas dos times
        self.mandante.registrar_partida(gols_mandante, gols_visitante)
        self.visitante.registrar_partida(gols_visitante, gols_mandante)


