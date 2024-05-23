def es_arbol(grafo):

    # Se realiza una busqueda DFS para comprobar si hay ciclos
    def dfs(nodo, padre):
        visitado.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitado:
                if not dfs(vecino, nodo):
                    return False
            elif vecino != padre:
                return False
        return True

    # Inicializar el conjunto de nodos visitados
    visitado = set()
    
    # Verificar si el grafo está vacío
    if not grafo:
        return True

    # Obtener el primer nodo del grafo
    nodos = list(grafo.keys())
    primer_nodo = nodos[0]
    
    # Verificar si el grafo es conexo y no contiene ciclos
    if not dfs(primer_nodo, None):
        return False
    
    # Verificar si todos los nodos fueron visitados (grafo conexo)
    if len(visitado) != len(grafo):
        return False
    
    return True

# Ejemplo de uso
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

print(f"Ejemplo 1: {es_arbol(grafo)}")  # Debería imprimir True

grafo_con_ciclo = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print(f"Ejemplo 2: {es_arbol(grafo_con_ciclo)}")  # Debería imprimir False
