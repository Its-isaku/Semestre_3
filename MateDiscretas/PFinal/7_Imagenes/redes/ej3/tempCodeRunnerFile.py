#Librerias
import matplotlib.pyplot as plt
import networkx as nx

# Creo una grafica
G = nx.DiGraph()

# agrego los nodos y sus conecciones
Nodos = [
    ("w", "x"),
    ("w", "z"),
    ("w", "y"),
    ("x", "z"),
    ("x", "y"),
    ("z", "y"),

]

for edge in Nodos:
    G.add_edge(edge[0], edge[1])

# Defino las posiciones de los nodos
pos = {
    "w": (0, 1),
    "x": (1, 1),
    "y": (0, 0),
    "z": (1, 0),
    
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

plt.title('Red 3.2')
plt.show()
