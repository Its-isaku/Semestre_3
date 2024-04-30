#librerias
import math
import string

#funciones
def AreaCir(Radio):

    Area = math.pi * (Radio**2)

    return Area

def PerimetroCir(Radio2):
    Perimetro = 2 * math.pi * Radio2

    return Perimetro

def Login(Password, Nombre):

    if len(Password) < 8:
        print("---------------------------------------------------------")
        print("Tu Password debe tener al menos 8 caracteres")
        return "fail"

    else:

        upper = False
        lower = False
        digitoespecial = False

        for caracter in Password:
            if caracter.isupper():
                upper = True
            elif caracter.islower():
                lower = True
            elif caracter.isdigit():
                digitoespecial = True

        if not upper:
            print("---------------------------------------------------------")
            print("Tu Password debe tener al menos una mayúscula")
            return "fail"
        elif not lower:
            print("---------------------------------------------------------")
            print("Tu Password debe tener al menos una minúscula")
            return "fail"
        elif not digitoespecial:
            print("---------------------------------------------------------")
            print("Tu Password debe tener al menos un número o un carácter especial")
            return "fail"
        else:
            print("---------------------------------------------------------")
            print(f"Bienvenido {Nombre}!, has creado tu cuenta exitosamente....")
            return "Exitoso"


#codigo principal
print("---------------------------------------------------------")
print("Bienvenido a la tarea Meta 2.1! ")
print("---------------------------------------------------------")

while True:

    print("[1] Calcular el área y el perímetro de un circulo........\n[2] Contraseña segura....................................\n[0] Salir................................................")
    print("---------------------------------------------------------")
    opc = int(input("Que deceas hacer? "))
    print("---------------------------------------------------------")
    
    if opc == 1:

        Radio = float(input("Dame el Radio: "))
        print("---------------------------------------------------------")
        print(f"El Area del circulo es: {AreaCir(Radio)}")
        print(f"El Perimetro del circulo es: {PerimetroCir(Radio)}")

        print("---------------------------------------------------------")


    elif opc == 2:
        Nombre = input("Cual es tu nombre: ")
        while True:
            Password = input("Insterte la Clave: ")
            resultado = Login(Password,Nombre)
            print("---------------------------------------------------------")
            if resultado == "Exitoso":
                break


    elif opc == 0:
        print("Gracias por uar el programa, hasta luego!")
        print("---------------------------------------------------------")
        break










