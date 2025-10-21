class Time:
    """Representa um time do campeonato.

    Atributos:
        nome (str): Nome do time.
        pontos (int): Pontos na tabela (3 vitória, 1 empate, 0 derrota).
        vitorias (int): Número de vitórias.
        gols_marcados (int): Total de gols marcados.
        gols_sofridos (int): Total de gols sofridos.
        saldo_gols (int): Diferença entre gols marcados e sofridos.
    """

    def __init__(self, nome: str):
        self.nome = nome
        self.pontos = 0
        self.vitorias = 0
        self.gols_marcados = 0
        self.gols_sofridos = 0
        self.saldo_gols = 0

    def registrar_partida(self, gols_marcados: int, gols_sofridos: int) -> None:
        if gols_marcados < 0 or gols_sofridos < 0:
            raise ValueError("Gols não podem ser negativos")

        self.gols_marcados += gols_marcados
        self.gols_sofridos += gols_sofridos
        self.saldo_gols = self.gols_marcados - self.gols_sofridos

        if gols_marcados > gols_sofridos:
            self.vitorias += 1
            self.pontos += 3
        elif gols_marcados == gols_sofridos:
            self.pontos += 1
        # derrota: nenhum ponto adicional


