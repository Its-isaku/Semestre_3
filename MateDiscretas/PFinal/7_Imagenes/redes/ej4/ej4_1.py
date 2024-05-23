#Librerias
import matplotlib.pyplot as plt
import networkx as nx

# Creo una grafica
G = nx.DiGraph()

# agrego los nodos y sus conecciones
Nodos = [
    ("a", "b"),
    ("a", "c"),
    ("a", "d"),
    ("b", "d")

]

for edge in Nodos:
    G.add_edge(edge[0], edge[1])

# Defino las posiciones de los nodos
pos = {
    "a": (1, 1),
    "b": (2, 0.7),
    "c": (0, 0.3),
    "d": (1.3, 0),
    
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

plt.title('Red 4.1')
plt.show()
