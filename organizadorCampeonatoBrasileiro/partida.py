from organizadorCampeonatoBrasileiro.time import Time


class Partida:
    """Representa uma partida de futebol entre dois times.

    Atributos:
        mandante (Time): Time da casa.
        visitante (Time): Time visitante.
        gols_mandante (int): Gols do mandante na partida.
        gols_visitante (int): Gols do visitante na partida.
        finalizada (bool): Indica se o placar foi registrado.
    """

    def __init__(self, mandante: Time, visitante: Time):
        if mandante is None or visitante is None:
            raise ValueError("Mandante e visitante devem ser informados")

        self.mandante = mandante
        self.visitante = visitante
        self.gols_mandante = 0
        self.gols_visitante = 0
        self.finalizada = False

    def registrar_placar(self, gols_mandante: int, gols_visitante: int) -> None:
        if self.finalizada:
            raise ValueError("Placar já registrado para esta partida")
        if gols_mandante < 0 or gols_visitante < 0:
            raise ValueError("Gols não podem ser negativos")

        self.gols_mandante = gols_mandante
        self.gols_visitante = gols_visitante
        self.finalizada = True

        # Atualiza estatísticas dos times
        self.mandante.registrar_partida(gols_mandante, gols_visitante)
        self.visitante.registrar_partida(gols_visitante, gols_mandante)


