import matplotlib.pyplot as plt
import networkx as nx

class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = Nodo(clave)
        else:
            self._insertar(self.raiz, clave)

    def _insertar(self, nodo, clave):
        if clave < nodo.clave:
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

# Función para solicitar cadenas al usuario
def solicitar_cadenas():
    cadenas = []
    print("Dame los datos de la cadena(deja vacío para terminar)\n")
    while True:
        cadena = input("Cadena: ")
        if cadena == "":
            break
        cadenas.append(cadena)
    return cadenas

# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
cadenas = solicitar_cadenas()

for cadena in cadenas:
    arbol.insertar(cadena)

arbol.dibujar()
