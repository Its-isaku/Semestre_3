import matplotlib.pyplot as plt
import networkx as nx
import random

class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = Nodo(clave)
        else:
            self._insertar(self.raiz, clave)

    def _insertar(self, nodo, clave):
        if random.choice([True, False]):
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(clave)
            else:
                self._insertar(nodo.izquierda, clave)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(clave)
            else:
                self._insertar(nodo.derecha, clave)

    def _agregar_nodos_grafo(self, nodo, grafo, pos={}, nivel=0, x=0, y=0, separacion=1.0):
        if nodo is not None:
            grafo.add_node(nodo.clave, pos=(x, y))
            if nodo.izquierda:
                grafo.add_edge(nodo.clave, nodo.izquierda.clave)
                pos = self._agregar_nodos_grafo(nodo.izquierda, grafo, pos, nivel + 1, x - separacion / 2, y - 1, separacion / 2)
            if nodo.derecha:
                grafo.add_edge(nodo.clave, nodo.derecha.clave)
                pos = self._agregar_nodos_grafo(nodo.derecha, grafo, pos, nivel + 1, x + separacion / 2, y - 1, separacion / 2)
        return pos

    def dibujar(self):
        grafo = nx.DiGraph()
        pos = self._agregar_nodos_grafo(self.raiz, grafo)
        pos = nx.get_node_attributes(grafo, 'pos')
        nx.draw(grafo, pos, with_labels=True, arrows=False)
        plt.show()

def generar_arbol_binario_aleatorio(n):
    arbol = ArbolBinario()
    for i in range(1, n + 1):
        arbol.insertar(i)
    return arbol

# Ejemplo de uso
n = int(input("Ingrese el número de vértices del árbol: "))
arbol = generar_arbol_binario_aleatorio(n)
arbol.dibujar()
