import math


peso = float(input("Dame tu peso en Kg: "))
altura  = float(input("Dame tu altura en metros: "))

IMC = (peso/pow(altura, 2.0))

print(f"Tu IMC es: {round(IMC, 2)}")