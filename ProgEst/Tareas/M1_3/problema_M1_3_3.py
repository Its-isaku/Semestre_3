peso_payaso  = 112
peso_muñeca = 75

cantidad_payasos = int(input("Cuantos payasos se vendieron? "))
cantidad_muñecas = int(input("Cuantas muñecas se vendieron? "))

peso_total_gr = (peso_payaso * cantidad_payasos) + (peso_muñeca * cantidad_muñecas)
peso_total_Kg = (((peso_payaso * cantidad_payasos) + (peso_muñeca * cantidad_muñecas)) / 1000)

print(f"El peso total del paquete en gramos es de {peso_total_gr} y en Kilogramos es {peso_total_Kg}")