#Librerias
import matplotlib.pyplot as plt
import networkx as nx

# Creo una grafica
G = nx.DiGraph()

# agrego los nodos y sus conecciones
Nodos = [
    ("w1", "b", 3),
    ("b", "c", 4),
    ("c", "A", 4),
    ("c", "B", 8),
    ("w2", "b", 3),
    ("w2", "d", 2),
    ("d", "B", 6),
    ("d", "C", 2),
    ("w3", "d", 5),
    ("w3", "e", 5),
    ("e", "d", 4),
    ("e", "f", 2),
    ("f", "B", 3),
    ("f", "C", 6),

]

for edge in Nodos:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Defino las posiciones de los nodos
pos = {
    "w1": (0, 2),
    "w2": (0, 1),
    "w3": (0, 0),
    "A": (2, 2),
    "B": (2, 1),
    "C": (2, 0),
    "b": (0.5, 2),
    "c": (1.5, 2),
    "d": (1, 1),
    "e": (0.5, 0),
    "f": (1.5, 0),
    
}

# Se dibuuja la grafica
plt.figure(figsize=(10, 8))

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

plt.title('Red 4')
plt.show()
