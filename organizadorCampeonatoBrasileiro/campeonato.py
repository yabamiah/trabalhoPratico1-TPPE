class Campeonato:
    def __init__(self, equipes: list[str]):
        """Inicializa o campeonato."""
        self.equipes = equipes
        self.num_times = len(equipes)
        self.jogos = []
        
        if self.num_times != 20:
            raise ValueError("O campeonato deve ter 20 equipes")

    def gerar_rodadas(self):
        """Gera as rodadas do campeonato usando o algoritmo Round-Robin.
        
        Implementa um algoritmo Round-Robin que garante que:
        - Cada time jogue contra todos os outros exatamente duas vezes (turno e returno)
        - Cada confronto A vs B ocorra exatamente uma vez
        - Cada time jogue 19 partidas como mandante e 19 como visitante
        - Total de 38 rodadas com 10 partidas cada
        """
        self.jogos = []
        equipes_trabalho = self.equipes.copy()

        self.gerar_primeiro_turno(equipes_trabalho)
        self.gerar_retornos()

    def gerar_primeiro_turno(self, equipes_trabalho):
        """Gera o primeiro turno do campeonato (19 rodadas)."""
        metade_campeonato = self.num_times // 2

        for rodada_num in range(self.num_times - 1):
            jogos_rodada = self.gerar_jogos_da_rodada(equipes_trabalho, rodada_num)
            self.jogos.append(jogos_rodada)
            equipes_trabalho = self.rotacionar_times(equipes_trabalho)

    def gerar_jogos_da_rodada(self, equipes_trabalho, rodada_num):
        """Gera os jogos de uma rodada específica, alternando mandos de campo."""
        jogos_rodada = []
        metade_campeonato = self.num_times // 2
        
        for i in range(metade_campeonato):
            time_a = equipes_trabalho[i]
            time_b = equipes_trabalho[self.num_times - 1 - i]

            # Alterna mandos por rodada para equilibrar casa/fora
            if rodada_num % 2 == 0:
                jogos_rodada.append((time_a, time_b))
            else:
                jogos_rodada.append((time_b, time_a))
                
        return jogos_rodada

    def rotacionar_times(self, equipes_trabalho):
        """Rotaciona os times mantendo o primeiro fixo (algoritmo Round-Robin)."""
        return [equipes_trabalho[0], equipes_trabalho[-1]] + equipes_trabalho[1:-1]

    def gerar_retornos(self):
        """Gera o returno do campeonato (19 rodadas), invertendo os mandos de campo."""
        primeiro_turno = list(self.jogos)
        
        for rodada in primeiro_turno:
            rodada_returno = [(visitante, mandante) for mandante, visitante in rodada]
            self.jogos.append(rodada_returno)

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
brasileirao_serie_A.exibir_jogos()