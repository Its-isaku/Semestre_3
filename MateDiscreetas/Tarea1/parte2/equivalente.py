import matplotlib.pyplot as plt
import networkx as nx

def Dibujar_arbol(esquinas, posicion, titulo):
    tree = nx.DiGraph()
    tree.add_edges_from(esquinas)
    nx.draw(tree, pos=posicion, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
    plt.title(titulo)

# Datos para los árboles binarios
esquinas_arbol = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
posicion = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (-1.5, -2), 5: (-0.5, -2), 6: (0.5, -2), 7: (1.5, -2)}

plt.figure(figsize=(12, 6))

plt.subplot(121)
Dibujar_arbol(esquinas_arbol, posicion, 'Árbol Binario 1')

plt.subplot(122)
Dibujar_arbol(esquinas_arbol, posicion, 'Árbol Binario 2')
plt.show()
