# se inicializa una clase llamada Nodo con sus propiedades
class Nodo:
    # se definen los hijos del nodo (izquierdo y derecho)
    def __init__(self, clave):
        # init inicializa los nodos hijos a None y le pone el valor de clave
        self.izquierda = None
        self.derecha = None
        self.clave = clave#

# se crea clase para  haccer la busqueda  BTS (Binary serch tree)
class BTS:

    # se inicializa la raiz del arbol a None
    def __init__(self):
        self.raiz = None

    # revisa si tiene raiza y si no es asi se inserta la rasiz al arbol
    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = Nodo(clave)
        else:
            self._insertar(clave, self.raiz)


    # revisa si el valor es mayor o menor a la raiz
    def _insertar(self, clave, nodo):
        # si el valor es menor que la raiz se inserta a la izquierda
        if clave < nodo.clave:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(clave)
            else:
                self._insertar(clave, nodo.izquierda)

        # si el valor es mayor que la raiz se inserta a la derecha
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(clave)
            else:
                self._insertar(clave, nodo.derecha)

    def preOrden(self, nodo):
        if nodo:
            print(nodo.clave, end=' ')
            self.preOrden(nodo.izquierda)
            self.preOrden(nodo.derecha)

# Uso del árbol y recorrido preOrden
arbol = BTS()
for clave in [10, 5, 14, 7, 12]:
    arbol.insertar(clave)


arbol.preOrden(arbol.raiz)