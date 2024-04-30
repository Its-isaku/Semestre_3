nombre = []
datos = ["primer nombre", "segundo nombre", "primer apellido","segundo apellido"]

for i in range(4):

    j = str(input(f"dame tu {datos[i]}: "))
    nombre.append(j)

print("#1")

print(nombre)

print("/-------------------------------------------")
print("#2")

for i in nombre:
    print(i)

print("/-------------------------------------------")
print("#3")

for i in reversed(nombre):
    print(i)

print("/-------------------------------------------")