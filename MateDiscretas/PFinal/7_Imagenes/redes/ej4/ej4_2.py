#Librerias
import matplotlib.pyplot as plt
import networkx as nx

# Creo una grafica
G = nx.DiGraph()

# agrego los nodos y sus conecciones
Nodos = [
    ("e", "f"),
    ("f", "g")

]

for edge in Nodos:
    G.add_edge(edge[0], edge[1])

# Defino las posiciones de los nodos
pos = {
    "e": (0, 0.7),
    "f": (0.1, 0.3),
    "g": (0.7, 0.7),
    
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

plt.title('Red 4.2')
plt.show()
