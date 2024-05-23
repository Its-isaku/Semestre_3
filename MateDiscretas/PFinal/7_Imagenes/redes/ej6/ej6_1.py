#Librerias
import matplotlib.pyplot as plt
import networkx as nx

# Creo una grafica
G = nx.DiGraph()

# agrego los nodos y sus conecciones
Nodos = [
    ("a", "d"),
    ("b", "e"),
    ("c", "d"),
    ("d", "e")

]

for edge in Nodos:
    G.add_edge(edge[0], edge[1])

# Defino las posiciones de los nodos
pos = {
    "a": (0, 0.5),
    "b": (0.5, 1),
    "c": (0.5, 0.5),
    "d": (0.5, 0),
    "e": (1, 0.5)
    
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

plt.title('Red 6.1')
plt.show()
