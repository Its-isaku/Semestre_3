import math

valor2 = int(input("Dame el primer valor predeterminado: "))

valor1 = int(input("Dame el segundo valor para sumarlo: "))

res1 = valor2 + valor1
print(f"la suma es : {res1}")
print("------------------------------------------\n")

valor1 = int(input("Dame el segundorvalor para restarlo: "))

res2 = valor2 - valor1
print(f"la resta es : {res2}")
print("------------------------------------------\n")

valor1 = int(input("Dame el segundo valor para multiplicarlo: "))

res3 = valor2 * valor1
print(f"la multiplicacion es : {res3}")
print("------------------------------------------\n")

valor1 = int(input("Dame el segundo valor para dividirlo(flotante): "))

res4 = valor2 / valor1
print(f"la divicion flotante es : {res4}")
print("------------------------------------------\n")

valor1 = int(input("Dame el segundo valor para dividirlo(entero): "))

res5 = valor2 // valor1
print(f"la division entera es : {res5}")
print("------------------------------------------\n")

valor1 = int(input("Dame el segundo valor para eleverlo: "))

res6 = pow(valor2, valor1)
print(f"el valor elevado es : {res6}")
print("------------------------------------------\n")
