lista1 = []
lista2 = []

def FunLista(lista1):

    n = int(input("Que tan grande sera el arreglo? "))
    print("---------------------------------------------------------")
    for i in range(n):
        dato = int(input(f"Dame el valor {i + 1}: "))
        lista1.append(dato)
    print("---------------------------------------------------------")
    print(f"Los datos de mi lista son: {lista1}")

def FunBuscar(lista2):

    n = int(input("Que tan grande sera el arreglo? "))
    print("---------------------------------------------------------")
    for i in range(n):
        dato = int(input(f"Dame el valor {i + 1}: "))
        lista2.append(dato)
    print("---------------------------------------------------------")
    
    valor = int(input("Que valor estas buscando: "))
    print("---------------------------------------------------------")

    contador = lista2.count(str(valor))

    print(f"El valor {valor} se repite {contador} veces en la lista {lista2}")

print("---------------------------------------------------------")
print("Bienvenido al programa de actividad extra! ")
print("---------------------------------------------------------")

while True:

    print("[1]Llenar lista..........................................\n[2]buscar valores en la lista............................\n[0]salir.................................................")
    print("---------------------------------------------------------")

    opc = int(input("Que deceas hacer? "))
    print("---------------------------------------------------------")

    if opc == 1:

        FunLista(lista1)
        print("---------------------------------------------------------")
    elif opc == 2:
        FunBuscar(lista2)
        print("---------------------------------------------------------")

    elif opc == 0:
        print("Gracias por usarel programa, hasta luego!")
        print("---------------------------------------------------------")
        break