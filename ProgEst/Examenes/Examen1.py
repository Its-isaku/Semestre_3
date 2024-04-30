"""c = 0

for i in range(100):

    num = i % 2
    if num == 0:
        c +=1
    
print(f"hay {c} numeros pares")"""

#--------------------------------------------------------------------

"""nombre = ["carlos", "CARLOS", "Carlos", "cARLOS"]

print("Usuarios: carlos")
print("")

while True:
    nom = input("Qué usuario deseas usar? ")
    encontrado = False

    for i in nombre:
        if nom == i:
            print("Hola carlos!")
            encontrado = True
            quit()

    if not encontrado:
        print("Usuario no encontrado")"""
    
    


"""import random


while True:
    
    lista1 = []
    lista2 = []
    contador = 0
    
    for i in range(4):
        n = random.randint(1, 20)
        lista1.append(n)

    for i in range(4):
        n = random.randint(1, 20)
        lista2.append(n)

    for i in range(4):
        if lista1[i] == lista2[i]:
            contador += 1
    
    if contador >= 3:
        print("Las listas cumplen con el 80% de similitud")
        print("Esta es la lista 1:", lista1)
        print("Esta es la lista 2:", lista2)
        break """
