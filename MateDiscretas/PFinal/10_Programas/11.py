def es_seguro(tablero, fila, columna, n):
    # Verifica la columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False
    
    # Verifica la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    # Verifica la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(columna, n)):
        if tablero[i][j] == 1:
            return False
    
    return True

def resolver_n_reinas(tablero, fila, n):
    if fila >= n:
        return True
    
    for columna in range(n):
        if es_seguro(tablero, fila, columna, n):
            tablero[fila][columna] = 1
            if resolver_n_reinas(tablero, fila + 1, n):
                return True
            tablero[fila][columna] = 0
    
    return False

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join("Q" if x == 1 else "." for x in fila))

def n_reinas(n):
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    if resolver_n_reinas(tablero, 0, n):
        imprimir_tablero(tablero)
    else:
        print("No hay solución")


n = int(input("Dame cantidad de rainas: "))
n_reinas(n)
