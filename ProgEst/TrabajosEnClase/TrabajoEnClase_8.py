import test8
print("******************************************************")
print("*                                                    *")
print("*                [1] Suma                            *")
print("*                [2] Abrir La Calculadora            *")
print("*                [3] Abrir Word                      *")
print("*                [4] Abrir Power Point               *")
print("*                                                    *")
print("******************************************************")

op = input("Que opcion deseas realizar? ")

if op == '1':
    v1 = int(input("Dame el valor 1: "))
    v2 = int(input("Dame el valor 2: "))

    print(f"La suma es {test8.suma(v1,v2)} ")

elif op == '2':
    test8.openCalc()

elif op == '3':
    test8.openw()

elif op == '4':
    test8.openp()
