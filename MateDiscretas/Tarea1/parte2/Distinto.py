import matplotlib.pyplot as plt
import networkx as nx

def Dibujar_arbol(esquinas, posicion, titulo):
    tree = nx.DiGraph()
    tree.add_edges_from(esquinas)
    nx.draw(tree, pos=posicion, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', arrows = True)
    plt.title(titulo) 

# Datos para el árbol binario 1
esquinas_arbol1 = [(1, 2), (1, 3), (2, 4), (2, 5)]
posicion1 = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (-1.5, -2), 5: (-0.5, -2)}

# Datos para el árbol binario 2
esquinas_arbol2 = [(1, 2), (1, 3), (3, 4), (3, 5)]
posicion2 = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (0.5, -2), 5: (1.5, -2)}

plt.figure(figsize=(12, 6))

plt.subplot(121)
Dibujar_arbol(esquinas_arbol1, posicion1, 'Árbol Binario 1')

plt.subplot(122)
Dibujar_arbol(esquinas_arbol2, posicion2, 'Árbol Binario 2')
plt.show()