#Librerias
import matplotlib.pyplot as plt
import networkx as nx

# Creo una grafica
G = nx.DiGraph()

# agrego los nodos y sus conecciones
Nodos = [
    ("a", "b"),
    ("a", "d"),
    ("b", "d"),
    ("b", "c"),
    ("c", "d"),
    ("c", "e"),
    ("c", "f"),
    ("d", "e"),
    ("a", "d"),

]

for edge in Nodos:
    G.add_edge(edge[0], edge[1])

# Defino las posiciones de los nodos
pos = {
    "a": (0, 2),
    "b": (0.7, 1.7),
    "c": (1.1, 1.5),
    "d": (0.1, 1.2),
    "e": (0.6, 0.7),
    "f": (1.2, 0.6),
    
}

# Se dibuuja la grafica
plt.figure(figsize=(4, 6))

nx.draw(G, pos, with_labels=True,
        node_size=3000,
        node_color='lightblue',
        font_size=10,
        font_weight='bold',
        arrows=False
        )

plt.title('Red 5')
plt.show()
