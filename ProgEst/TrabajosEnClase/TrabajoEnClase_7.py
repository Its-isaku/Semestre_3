import time 

def Conversion(Peso):
    dolar = Peso / 16.50

    return dolar 

Peso = int(input("cuantos pesos queres convertir a dolar? "))

print("Llamando a funcion.....")
time.sleep(2)

x = Conversion(Peso)
print(f"${x} pesos")