def encontrar_componentes(grafo):
    def dfs(nodo, componente):
        visitado.add(nodo)
        componente.append(nodo)
        for vecino in grafo.get(nodo, []):
            if vecino not in visitado:
                dfs(vecino, componente)

    visitado = set()
    componentes = []

    for nodo in grafo:
        if nodo not in visitado:
            componente = []
            dfs(nodo, componente)
            componentes.append(componente)

    return componentes

# Ejemplo
grafo = {
    0: [1, 2],
    1: [0],
    2: [0, 3, 4],
    3: [2],
    4: [2],
    5: [6],
    6: [5, 7, 8],
    7: [6],
    8: [6],
    9: [10],
    10: [9]
}

componentes = encontrar_componentes(grafo)
print(f"Componentes conectadas: {componentes}")

