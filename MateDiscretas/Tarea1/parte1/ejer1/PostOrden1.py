class Nodo:
    def __init__(self, clave):
        self.izquierda = None
        self.derecha = None
        self.clave = clave

class BTS:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = Nodo(clave)
        else:
            self._insertar(clave, self.raiz)

    def _insertar(self, clave, nodo):
        if clave < nodo.clave:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(clave)
            else:
                self._insertar(clave, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(clave)
            else:
                self._insertar(clave, nodo.derecha)

    def postOrden(self, nodo):
        if nodo:
            self.postOrden(nodo.izquierda)
            self.postOrden(nodo.derecha)
            print(nodo.clave, end=' ')

# Creación del árbol y uso del recorrido postOrden con caracteres
arbol = BTS()
letras = ['G', 'B', 'Q', 'A', 'C', 'K', 'F', 'P', 'D', 'E', 'R', 'H']

for letra in letras:
    arbol.insertar(letra)

arbol.postOrden(arbol.raiz)
