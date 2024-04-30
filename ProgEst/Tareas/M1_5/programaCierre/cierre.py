import random

print("---------------------------------------------------------")
print("Bienvenido al programa de cierre del parcial 1! ")
print("---------------------------------------------------------")

while True:


    print("[A]Para calcular la edad.................................\n[B]para contar pares......................................\n[C]Para encontrar valores optimos area del trapeco......\n[D]Contar caracteres no vocales..........................\n[S]salir.................................................")

    print("---------------------------------------------------------")

    opc = str(input("Que deceas hacer? "))
    opc = opc.upper()

    print("---------------------------------------------------------")

#----------------------------------------------------------------------------------------------------
    if opc == 'A':

        edad = int(input("Hola!, cuale es tu edad? "))

        for i in range(edad + 1):
            print(f"cumpliste {i} años")        

#----------------------------------------------------------------------------------------------------
        
    elif opc == 'B':

        Num_aleatorios = []
        contador = 0

        for i in range(50):
            numeros = random.randrange(18, 87)
            Num_aleatorios.append(numeros)
            print(random.randrange(18, 87))
            
        for numeros in Num_aleatorios:
            if numeros % 2 ==0:
                contador += 1

        print("---------------------------------------------------------")  
        print(contador)

#----------------------------------------------------------------------------------------------------
    
    elif opc == 'C':

        N = int(input("Dame el numero de iteraciones: "))
        print("---------------------------------------------------------")

        for i in range(N):
            B = random.randrange(1, 10)
            b = random.randrange(1, 10)
            h  =random.randrange(1, 10)
            Area = ((B + b)/2) * h
            
            if (Area >= 16 and Area <= 19):
                print(Area)
                print(f"El valor B es {B}")
                print(f"El valor b es {b}")
                print(f"El valor h es {h}")   
                print("---------------------------------------------------------")

        
#----------------------------------------------------------------------------------------------------

    elif opc == 'D':
        texto = str(input("Ingresa el texto: "))
        print("---------------------------------------------------------")


        texto= texto.lower()

        vocales = ['a', 'e', 'i', 'o', 'u ']

        contador =0

        for i in texto:
            if i.isalpha() and i not in vocales:
                contador += 1

        print(f"Cantidad de letras que no son vocales:{contador}")

#----------------------------------------------------------------------------------------------------

    elif opc == 'S':
        print("Gracias por usar el programa, hasta luego!")
        print("---------------------------------------------------------")
        break

#----------------------------------------------------------------------------------------------------

    else:
        print("Debes elegir entre las opciones: [A],[B],[C],[D],[S]")
    print("---------------------------------------------------------")




            



