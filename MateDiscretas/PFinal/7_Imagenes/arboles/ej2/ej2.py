import matplotlib.pyplot as plt
import networkx as nx

# Definir la estructura del árbol
arbol = {
    1: [2, 3, 4],
    2: [5],
    3: [6, 7],
    4: [8, 9, 10],
    5: [11, 12, 13, 14],
    10: [15, 16, 17]
}

# Función para realizar el recorrido en pre-orden
def recorrido_preorden(nodo, arbol, resultado):
    if nodo is None:
        return
    resultado.append(nodo)
    if nodo in arbol:
        for hijo in arbol[nodo]:
            recorrido_preorden(hijo, arbol, resultado)

# Función para realizar el recorrido en post-orden
def recorrido_postorden(nodo, arbol, resultado):
    if nodo is None:
        return
    if nodo in arbol:
        for hijo in arbol[nodo]:
            recorrido_postorden(hijo, arbol, resultado)
    resultado.append(nodo)

# Realizar los recorridos
resultado_preorden = []
resultado_postorden = []
recorrido_preorden(1, arbol, resultado_preorden)
recorrido_postorden(1, arbol, resultado_postorden)

# Imprimir los resultados
print("Recorrido en pre-orden:", resultado_preorden)
print("Recorrido en post-orden:", resultado_postorden)

# Visualizar el árbol usando NetworkX y Matplotlib
G = nx.DiGraph()
for padre, hijos in arbol.items():
    for hijo in hijos:
        G.add_edge(padre, hijo)

# Posiciones manuales para los nodos
pos = {
    1: (0, 3),
    2: (-2, 2),
    3: (0, 2),
    4: (2, 2),
    5: (-2, 1),
    6: (-0.5, 1),
    7: (0.5, 1),
    8: (1.5, 1),
    9: (2.5, 1),
    10: (3.5, 1),
    11: (-3, 0),
    12: (-2.5, 0),
    13: (-2, 0),
    14: (-1.5, 0),
    15: (3, 0),
    16: (3.5, 0),
    17: (4, 0)
}

plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightgreen', font_size=12, font_weight='bold', arrows=False)
plt.title('Visualización del Árbol')
plt.show()
