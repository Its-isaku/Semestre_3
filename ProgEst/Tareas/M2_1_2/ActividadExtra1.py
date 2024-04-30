import string

cadena = "P3P3PPeca5p1c4PaPa5"


def fun1(cadena):

    print("-----------------------------------------------------------------")
    print(f"La cadena es: {cadena}")
    print("")

    contador1 = 0
    for i in cadena:
        if i.isupper():
            contador1 += 1
    print(f"Cuantas letras mayusculas tiene la cadena? {contador1}")
    print("")

    contador2 = 0
    for i in cadena:
        if i.islower():
            contador2 += 1
    print(f"Cuantas letras minusculas tiene la cadena? {contador2}")
    print("")

    contador3 = 0
    for i in cadena:
            contador3 += 1
    print(f"Que longitud tiene la cadena? {contador3}")
    print("")

    contador4 = 0
    for i in cadena:
        if i.isnumeric():
            contador4 += 1
    print(f"cuantas numeros tiene la cadena? {contador4}")
    print("")

    contador5 = 0
    for i in cadena:
        if i == '3':
            contador5 += 1
    print(f"cuantas veces se repite el 3 en la cadena? {contador5}")
    print("")

    cadena = cadena.replace('3', 'E')
    print(f"Como queda la cadena si cambias los 3 con E? {cadena}")
    print("-----------------------------------------------------------------")

fun1(cadena)

