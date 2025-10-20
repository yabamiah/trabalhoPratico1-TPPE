# Classe para definir os 20 times do campeonato brasileiro, gerar rodadas e definir a classificação final do campeonato.
class Campeonato:
    def __init__(self, equipes: list[str]):
        """Inicializa o campeonato."""

        self.equipes = equipes
        self.num_times = len(equipes)
        self.jogos = []
        
        if self.num_times != 20:
            raise ValueError("O campeonato deve ter 20 equipes")

    def gerar_rodadas(self):
        """Gera as rodadas do campeonato."""

        self.jogos = []
        metade_campeonato = self.num_times // 2

        # PrimeiroTurno
        for r in range(self.num_times - 1):
            jogos_rodada = []
            for i in range(metade_campeonato):
                a = self.equipes[i]
                b = self.equipes[self.num_times - 1 - i]

                # alterna mandos por rodada 
                if r % 2 == 0:
                    jogos_rodada.append((a, b))
                else:
                    jogos_rodada.append((b, a))
            self.jogos.append(jogos_rodada)

            # Rotaciona mantendo o primeiro fixo
            self.equipes = [self.equipes[0], self.equipes[-1]] + self.equipes[1:-1]

        # Returno (invertendo mandos)
        turno = list(self.jogos)
        for rodada in turno:
            self.jogos.append([(visitante, mandante) for mandante, visitante in rodada])
        
    def exibir_jogos(self):
        """Imprime o calendário de jogos gerado."""

        for i, rodada in enumerate(self.jogos):
            print(f"--- Rodada {i + 1} ---")
            for mandante, visitante in rodada:
                print(f"{mandante} x {visitante}")

times_brasileirao_serie_A = ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Grêmio", "Internacional",
        "Atlético-MG", "Cruzeiro", "Fluminense", "Vasco", "Botafogo", "Santos",
        "Bahia", "Vitória", "Mirassol", "Juventude", "Bragantino", "Ceará",
        "Fortaleza", "Sport Recife"]
    
brasileirao_serie_A = Campeonato(times_brasileirao_serie_A)
brasileirao_serie_A.gerar_rodadas()
print(brasileirao_serie_A.exibir_jogos())