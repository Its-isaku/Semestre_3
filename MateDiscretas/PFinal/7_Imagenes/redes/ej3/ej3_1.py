#Librerias
import matplotlib.pyplot as plt
import networkx as nx

# Creo una grafica
G = nx.DiGraph()

# agrego los nodos y sus conecciones
Nodos = [
    ("a", "b"),
    ("a", "d"),
    ("a", "c"),
    ("b", "d"),
    ("b", "c"),
    ("d", "c"),

]

for edge in Nodos:
    G.add_edge(edge[0], edge[1])

# Defino las posiciones de los nodos
pos = {
    "a": (0, 1),
    "b": (1, 1),
    "c": (0, 0),
    "d": (1, 0),
    
}

# Se dibuuja la grafica
plt.figure(figsize=(8, 6))

nx.draw(G, pos, with_labels=True,
        node_size=3000,
        node_color='lightblue',
        font_size=10,
        font_weight='bold',
        arrows=False
        )

plt.title('Red 3.1')
plt.show()

#! falta hacer que se curve por fuera b - c