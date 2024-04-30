Horas = int(input("Cuantas horas trabajas a la semana sin contar horas extra? "))
pago_X_hora = int(input("Cuanto pagan por hora? "))


Pago_Diario = (8 * pago_X_hora)
Pago_semanal = (Horas * pago_X_hora)
Pago_mensual = (Pago_semanal) * 4

print(f"Tu pago diario es {Pago_Diario}")
print(f"Tu pago semanal es {Pago_semanal}")
print(f"Tu pago mesual es {Pago_mensual}")