def ordenar_classificacao(times):
    return sorted(times, key=lambda time: (time.pontos, time.vitorias), reverse=True)
