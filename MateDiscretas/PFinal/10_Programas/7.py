class Arbol:
    def __init__(self, raiz):
        self.raiz = raiz
        self.arbol = {raiz: []}
        self.padres = {raiz: None}

    def agregar_hijo(self, padre, hijo):
        if padre not in self.arbol:
            self.arbol[padre] = []
        self.arbol[padre].append(hijo)
        self.padres[hijo] = padre
        self.arbol[hijo] = []

    def encontrar_padre(self, v):
        return self.padres.get(v, None)

    def encontrar_ancestros(self, v):
        ancestros = []
        actual = v
        while actual is not None:
            actual = self.padres.get(actual, None)
            if actual is not None:
                ancestros.append(actual)
        return ancestros

    def encontrar_hijos(self, v):
        return self.arbol.get(v, [])

    def encontrar_descendientes(self, v):
        descendientes = []
        def dfs(nodo):
            for hijo in self.arbol.get(nodo, []):
                descendientes.append(hijo)
                dfs(hijo)
        dfs(v)
        return descendientes

    def encontrar_hermanos(self, v):
        padre = self.encontrar_padre(v)
        if padre is None:
            return []
        return [hijo for hijo in self.arbol[padre] if hijo != v]

    def es_terminal(self, v):
        return len(self.encontrar_hijos(v)) == 0


# Ejemplo
arbol = Arbol(1)
arbol.agregar_hijo(1, 2)
arbol.agregar_hijo(1, 3)
arbol.agregar_hijo(2, 4)
arbol.agregar_hijo(2, 5)
arbol.agregar_hijo(3, 6)
arbol.agregar_hijo(3, 7)
arbol.agregar_hijo(4, 8)
arbol.agregar_hijo(4, 9)
arbol.agregar_hijo(5, 10)
arbol.agregar_hijo(5, 11)
arbol.agregar_hijo(7, 12)
arbol.agregar_hijo(7, 13)

v = 5

print(f"Padre de {v}: {arbol.encontrar_padre(v)}")
print(f"Ancestros de {v}: {arbol.encontrar_ancestros(v)}")
print(f"Hijos de {v}: {arbol.encontrar_hijos(v)}")
print(f"Descendientes de {v}: {arbol.encontrar_descendientes(v)}")
print(f"Hermanos de {v}: {arbol.encontrar_hermanos(v)}")
print(f"{v} es un vértice terminal?: {arbol.es_terminal(v)}")
