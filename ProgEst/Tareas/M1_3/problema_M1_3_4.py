balance_inicia =  float(input("Dame cantidad del deposito: "))

Tasa_interes = 0.05

#calcular balance de primer año
intereses_año_1 = balance_inicia * Tasa_interes
balance_despues_año_1 = balance_inicia + intereses_año_1

#calcular balance de segudo año
intereses_año_2 = balance_despues_año_1 * Tasa_interes
balance_despues_año_2 = balance_despues_año_1 + intereses_año_2

#calcular balance de tercer año
intereses_año_3 = balance_despues_año_2 * Tasa_interes
balance_despues_año_3 = balance_despues_año_2 + intereses_año_3

print(f"El balance del primer año es: {balance_despues_año_1}")
print(f"El balance del segundo año es: {balance_despues_año_2}")
print(f"El balance del tercer año es: {balance_despues_año_3}")