import matplotlib.pyplot as plt
import networkx as nx

class NodoArbol:
    def __init__(self, clave):
        self.izquierda = None
        self.derecha = None
        self.valor = clave

def recorrido_en_orden(raiz, resultado=[]):
    if raiz:
        recorrido_en_orden(raiz.izquierda, resultado)
        resultado.append(raiz.valor)
        recorrido_en_orden(raiz.derecha, resultado)
    return resultado

def dibujar_arbol(raiz):
    def agregar_aristas(nodo, pos={}, x=0, y=0, nivel=1):
        if nodo:
            pos[nodo.valor] = (x, y)
            if nodo.izquierda:
                G.add_edge(nodo.valor, nodo.izquierda.valor)
                l = x - 1 / nivel
                agregar_aristas(nodo.izquierda, pos, x=l, y=y-1, nivel=nivel+1)
            if nodo.derecha:
                G.add_edge(nodo.valor, nodo.derecha.valor)
                r = x + 1 / nivel
                agregar_aristas(nodo.derecha, pos, x=r, y=y-1, nivel=nivel+1)
        return pos

    G = nx.DiGraph()
    pos = agregar_aristas(raiz)

    fig, ax = plt.subplots()
    nx.draw(G, pos, ax=ax, with_labels=True, node_size=2000, node_color="lightgreen", font_size=16, font_color="black", font_weight="bold", arrows=False)
    plt.show()

# Construcción del árbol como el de la imagen
raiz = NodoArbol('r')
raiz.izquierda = NodoArbol('a')
raiz.derecha = NodoArbol('e')
raiz.izquierda.izquierda = NodoArbol('c')
raiz.izquierda.derecha = NodoArbol('d')
raiz.derecha.izquierda = NodoArbol('h')
raiz.derecha.derecha = NodoArbol('n')
raiz.izquierda.izquierda.izquierda = NodoArbol('f')
raiz.izquierda.izquierda.derecha = NodoArbol('j')
raiz.izquierda.izquierda.derecha.izquierda = NodoArbol('p')
raiz.izquierda.izquierda.derecha.derecha = NodoArbol('q')
raiz.derecha.derecha.izquierda = NodoArbol('t')
raiz.derecha.derecha.derecha = NodoArbol('u')

# Recorrido en orden
resultado = recorrido_en_orden(raiz, [])
print("Recorrido en orden:", resultado)

# Dibujar el árbol
dibujar_arbol(raiz)
