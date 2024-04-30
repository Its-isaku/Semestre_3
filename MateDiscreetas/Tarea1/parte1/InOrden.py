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

# se define la busqueda InOrden
    def inOrden(self, nodo):
        if nodo:
            #Primero hace el recorido en el subarbol izquierdo
            self.inOrden(nodo.izquierda)
            print(nodo.clave, end=' ')
            #Despues hace el recorido en el subarbol derecho
            self.inOrden(nodo.derecha)

# Uso del árbol y recorrido inOrden
arbol = BTS()

# se le asignan los valores al arbol
for clave in [50, 30, 20, 40, 70, 60, 80, 10, 90, 25]:
    #se insertan los valores
    arbol.insertar(clave)

arbol.inOrden(arbol.raiz)