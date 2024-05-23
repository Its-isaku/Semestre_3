#Librerias
import matplotlib.pyplot as plt
import networkx as nx

# Creo una grafica
G = nx.DiGraph()

# agrego los nodos y sus conecciones
Nodos = [
    ("w1", "b", 6),
    ("b", "A", 4),
    ("b","c", 2),
    ("w2", "b", 3),
    ("c", "A", 2),
    ("c", "B", 4),
    ("w3", "d", 3),
    ("d", "c", 3),
]

for edge in Nodos:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Defino las posiciones de los nodos
pos = {
    "w1": (0, 2),
    "w2": (0, 1),
    "w3": (0, 0),
    "A": (2, 2),
    "B": (2, 0),
    "b": (0.5, 2),
    "c": (1.5, 1),
    "d": (0.5, 0)
}

# Se dibuuja la grafica
plt.figure(figsize=(8, 6))

nx.draw(G, pos, with_labels=True,
        node_size=3000,
        node_color='lightblue',
        font_size=10,
        font_weight='bold',
        arrowsize=20
        )

# Draw edge labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title('Red 10.1.3')
plt.show()
