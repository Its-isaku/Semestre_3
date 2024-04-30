import matplotlib.pyplot as plt
import networkx as nx

def Dibujar_arbol(esquinas, posicion, titulo):
    tree = nx.DiGraph()
    tree.add_edges_from(esquinas)
    nx.draw(tree, pos=posicion, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
    plt.title(titulo)

# Datos comunes para ambos árboles
posicion_comun = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (-1.5, -2), 5: (-0.5, -2), 6: (0.5, -2), 7: (1.5, -2)}

# Ajustamos los números de los nodos y las posiciones para el Árbol Binario 1
esquinas_arbol1 = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
posicion1 = {key: posicion_comun[key] for key in [1, 2, 3, 4, 5, 6, 7]}

# Ajustamos los números de los nodos y las posiciones para el Árbol Binario 2
esquinas_arbol2 = [(11, 21), (11, 31), (21, 41), (21, 51), (31, 61), (31, 71)]
posicion2 = {11: (0, 0), 21: (-1, -1), 31: (1, -1), 41: (-1.5, -2), 51: (-0.5, -2), 61: (0.5, -2), 71: (1.5, -2)}

plt.figure(figsize=(12, 6))
    
plt.subplot(121)
Dibujar_arbol(esquinas_arbol1, posicion1, 'Árbol Binario 1')

plt.subplot(122)
Dibujar_arbol(esquinas_arbol2, posicion2, 'Árbol Binario 2')
plt.show()
