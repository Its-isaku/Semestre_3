#Librerias
import matplotlib.pyplot as plt
import networkx as nx

# Creo una grafica
G = nx.DiGraph()

# agrego los nodos y sus conecciones
Nodos = [
    ("a", "b", 5,),
    ("b", "c", 6),
    ("c", "z", 5),
    ("c", "e", 6),
    ("e", "z", 5,),
    ("a", "d", 4),
    ("d", "e", 3,),

]

for edge in Nodos:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Defino las posiciones de los nodos
pos = {
    "a": (0, 1),
    "b": (1, 2),
    "c": (2, 2),
    "d": (1, 0),
    "e": (2, 0),
    "z": (3, 1),
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

plt.title('Red 1')
plt.show()
