#Librerias
import matplotlib.pyplot as plt
import networkx as nx

# Creo una grafica
G = nx.DiGraph()

# agrego los nodos y sus conecciones
Nodos = [
    ("b", "e"),
    ("e", "d"),

]

for edge in Nodos:
    G.add_edge(edge[0], edge[1])

# Defino las posiciones de los nodos
pos = {
    "b": (0, 1),
    "d": (0, 0),
    "e": (0.5, 0.5)
    
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

plt.title('Red 6.3')
plt.show()
