import matplotlib.pyplot as plt
import networkx as nx

# Creo una grafica
G = nx.MultiDiGraph()  # Usar MultiDiGraph para permitir múltiples aristas entre los mismos nodos

# Agrego los nodos y sus conexiones
Nodos = [
    ("1", "2"),
    ("1", "2"),
    ("2", "3"),
    ("2", "3"),
    ("2", "2"),
    ("3", "3"),
    ("3", "3"),
]

for edge in Nodos:
    G.add_edge(edge[0], edge[1])

# Defino las posiciones de los nodos
pos = {
    "1": (0, 0),
    "2": (1, 1),
    "3": (2, 0),
}

# Se dibuja la grafica
plt.figure(figsize=(8, 6))

# Dibujo las conexiones múltiples
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightyellow')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Dibujar aristas duplicadas manualmente
# Dibujar dos veces la misma arista en diferentes posiciones
nx.draw_networkx_edges(G, pos, edgelist=[("1", "2")], arrowstyle='-|>', arrowsize=20, edge_color='navy', connectionstyle='arc3,rad=0.1')
nx.draw_networkx_edges(G, pos, edgelist=[("1", "2")], arrowstyle='-|>', arrowsize=20, edge_color='navy', connectionstyle='arc3,rad=-0.1')
nx.draw_networkx_edges(G, pos, edgelist=[("2", "3")], arrowstyle='-|>', arrowsize=20, edge_color='navy', connectionstyle='arc3,rad=0.1')
nx.draw_networkx_edges(G, pos, edgelist=[("2", "3")], arrowstyle='-|>', arrowsize=20, edge_color='navy', connectionstyle='arc3,rad=-0.1')
nx.draw_networkx_edges(G, pos, edgelist=[("2", "2")], arrowstyle='-|>', arrowsize=20, edge_color='navy', connectionstyle='arc3,rad=0.1')
nx.draw_networkx_edges(G, pos, edgelist=[("3", "3")], arrowstyle='-|>', arrowsize=20, edge_color='navy', connectionstyle='arc3,rad=0.2')
nx.draw_networkx_edges(G, pos, edgelist=[("3", "3")], arrowstyle='-|>', arrowsize=20, edge_color='navy', connectionstyle='arc3,rad=-0.2')

plt.title('Red 6.3')
plt.axis('off')
plt.show()
