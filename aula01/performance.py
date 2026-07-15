import time


def rodar_laboratorio_ineficiente():
    """QC: versão original do professor, O(N^2), usada para provar que o sistema está lento."""
    tamanho_giga = 15000
    tempo_inicial = time.time()

    # Busca ineficiente de dados (O(N^2))
    resultado = []
    for i in range(tamanho_giga):
        for j in range(tamanho_giga):
            if i == j:
                resultado.append(i)

    tempo_final = time.time()
    tempo_execucao = tempo_final - tempo_inicial

    print(f"[Ineficiente] Tempo de Execução: {tempo_execucao:.4f} segundos")
    print("[Ineficiente] Total de itens processados:", len(resultado))
    return resultado, tempo_execucao


def rodar_laboratorio_otimizado():
    """QA: solução do desafio - elimina o laço interno (for j), mantendo o mesmo resultado, agora O(N)."""
    tamanho_giga = 15000
    tempo_inicial = time.time()

    resultado = []
    for i in range(tamanho_giga):
        resultado.append(i)

    tempo_final = time.time()
    tempo_execucao = tempo_final - tempo_inicial

    print(f"[Otimizado] Tempo de Execução: {tempo_execucao:.4f} segundos")
    print("[Otimizado] Total de itens processados:", len(resultado))
    return resultado, tempo_execucao


if __name__ == "__main__":
    resultado_ineficiente, tempo_ineficiente = rodar_laboratorio_ineficiente()
    resultado_otimizado, tempo_otimizado = rodar_laboratorio_otimizado()

    assert resultado_ineficiente == resultado_otimizado, "Os dois algoritmos devem gerar o mesmo resultado"

    ganho = tempo_ineficiente / tempo_otimizado if tempo_otimizado > 0 else float("inf")
    print(f"\nGanho de performance: {ganho:.1f}x mais rápido eliminando o laço interno")
