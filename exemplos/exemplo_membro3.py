#!/usr/bin/env python3
"""
Exemplo prático de uso do Processador de Rodada - Membro 3
Demonstra o processamento de resultados e estatísticas de uma rodada do Campeonato Brasileiro.
"""

import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from organizadorCampeonatoBrasileiro.time import Time
from organizadorCampeonatoBrasileiro.partida import Partida
from organizadorCampeonatoBrasileiro.processador_rodada import ProcessadorRodada


def criar_times_brasileirao():
    """Cria alguns times do Brasileirão para o exemplo."""
    times = [
        Time("Flamengo"),
        Time("Palmeiras"),
        Time("São Paulo"),
        Time("Corinthians"),
        Time("Santos"),
        Time("Vasco"),
        Time("Botafogo"),
        Time("Atlético-MG"),
        Time("Internacional"),
        Time("Grêmio")
    ]
    return times


def simular_rodada_exemplo():
    """Simula uma rodada completa com 5 partidas."""
    print("=== SIMULAÇÃO DE RODADA DO CAMPEONATO BRASILEIRO ===\n")
    
    # Criar times
    times = criar_times_brasileirao()
    
    # Criar partidas da rodada
    partidas = [
        Partida(times[0], times[1]),  # Flamengo vs Palmeiras
        Partida(times[2], times[3]),  # São Paulo vs Corinthians
        Partida(times[4], times[5]),  # Santos vs Vasco
        Partida(times[6], times[7]),  # Botafogo vs Atlético-MG
        Partida(times[8], times[9])   # Internacional vs Grêmio
    ]
    
    # Definir placares (simulados)
    placares = [
        (3, 1),  # Flamengo 3x1 Palmeiras
        (2, 2),  # São Paulo 2x2 Corinthians
        (1, 0),  # Santos 1x0 Vasco
        (0, 2),  # Botafogo 0x2 Atlético-MG
        (1, 1)   # Internacional 1x1 Grêmio
    ]
    
    print("RESULTADOS DA RODADA:")
    print("-" * 40)
    
    # Registrar placares e exibir resultados
    for i, (partida, placar) in enumerate(zip(partidas, placares)):
        gols_mandante, gols_visitante = placar
        partida.registrar_placar(gols_mandante, gols_visitante)
        
        resultado = "VITÓRIA" if gols_mandante > gols_visitante else "EMPATE" if gols_mandante == gols_visitante else "DERROTA"
        print(f"{partida.mandante.nome} {gols_mandante} x {gols_visitante} {partida.visitante.nome} - {resultado}")
    
    print("\n")
    
    # Processar rodada
    processador = ProcessadorRodada()
    processador.processar_rodada(partidas)
    
    # Exibir estatísticas detalhadas
    print("ESTATÍSTICAS DETALHADAS DOS TIMES:")
    print("-" * 80)
    print(f"{'Time':<15} {'Pts':<4} {'V':<3} {'GM':<3} {'GS':<3} {'SG':<4}")
    print("-" * 80)
    
    # Ordenar times por pontos (critério básico)
    todos_times = []
    for partida in partidas:
        if partida.mandante not in todos_times:
            todos_times.append(partida.mandante)
        if partida.visitante not in todos_times:
            todos_times.append(partida.visitante)
    
    # Ordenar por pontos, depois por vitórias, depois por saldo de gols
    todos_times.sort(key=lambda t: (-t.pontos, -t.vitorias, -t.saldo_gols))
    
    for i, time in enumerate(todos_times, 1):
        print(f"{i:2}. {time.nome:<12} {time.pontos:2} {time.vitorias:2} {time.gols_marcados:2} {time.gols_sofridos:2} {time.saldo_gols:+3}")
    
    # Exibir resumo da rodada
    print("\n")
    print("RESUMO DA RODADA:")
    print("-" * 30)
    resumo = processador.obter_resumo_rodada()
    print(f"Total de partidas: {resumo['total_partidas']}")
    print(f"Total de gols: {resumo['total_gols']}")
    print(f"Vitórias do mandante: {resumo['vitorias']}")
    print(f"Empates: {resumo['empates']}")
    print(f"Derrotas do mandante: {resumo['derrotas']}")
    
    # Análise adicional
    print("\n")
    print("ANÁLISE DA RODADA:")
    print("-" * 20)
    
    # Times com melhor e pior desempenho
    melhor_time = max(todos_times, key=lambda t: t.pontos)
    pior_time = min(todos_times, key=lambda t: t.pontos)
    
    print(f"Melhor desempenho: {melhor_time.nome} ({melhor_time.pontos} pontos)")
    print(f"Pior desempenho: {pior_time.nome} ({pior_time.pontos} pontos)")
    
    # Maior goleada
    maior_diferenca = 0
    partida_goleada = None
    for partida in partidas:
        diferenca = abs(partida.gols_mandante - partida.gols_visitante)
        if diferenca > maior_diferenca:
            maior_diferenca = diferenca
            partida_goleada = partida
    
    if maior_diferenca > 1:
        print(f"Maior goleada: {partida_goleada.mandante.nome} {partida_goleada.gols_mandante} x {partida_goleada.gols_visitante} {partida_goleada.visitante.nome}")
    else:
        print("Não houve goleadas nesta rodada")
    
    # Artilheiros da rodada
    print(f"Média de gols por partida: {resumo['total_gols'] / resumo['total_partidas']:.1f}")


def demonstrar_casos_especiais():
    """Demonstra o tratamento de casos especiais."""
    print("\n\n=== DEMONSTRAÇÃO DE CASOS ESPECIAIS ===\n")
    
    processador = ProcessadorRodada()
    
    # Teste 1: Tentar processar rodada vazia
    print("1. Tentando processar rodada vazia:")
    try:
        processador.processar_rodada([])
    except ValueError as e:
        print(f"   ❌ Erro capturado: {e}")
    
    # Teste 2: Tentar processar partida não finalizada
    print("\n2. Tentando processar partida não finalizada:")
    time_a = Time("Time A")
    time_b = Time("Time B")
    partida_nao_finalizada = Partida(time_a, time_b)
    
    try:
        processador.processar_rodada([partida_nao_finalizada])
    except ValueError as e:
        print(f"   ❌ Erro capturado: {e}")
    
    # Teste 3: Processamento normal
    print("\n3. Processamento normal:")
    partida_normal = Partida(time_a, time_b)
    partida_normal.registrar_placar(1, 0)
    
    try:
        processador.processar_rodada([partida_normal])
        print(f"   ✅ Partida processada com sucesso!")
        print(f"   {time_a.nome}: {time_a.pontos} pontos, {time_a.vitorias} vitórias")
        print(f"   {time_b.nome}: {time_b.pontos} pontos, {time_b.vitorias} vitórias")
    except Exception as e:
        print(f"   ❌ Erro inesperado: {e}")


if __name__ == "__main__":
    print("Exemplo de uso do Processador de Rodada - Membro 3")
    print("Desenvolvido para o Trabalho Prático 1 - TPPE")
    print("=" * 60)
    
    simular_rodada_exemplo()
    demonstrar_casos_especiais()
    
    print("\n" + "=" * 60)
    print("Exemplo concluído com sucesso!")
    print("Todas as funcionalidades do Membro 3 foram demonstradas.")