list_estaturas = []
suma = 0

while True:
    estatura = float(input("Dame tu estatura en CM (si deseas  terminar introduce 0): "))
    
    if estatura == 0:
        break
    
    
    if estatura > 60:
        list_estaturas.append(estatura)
        suma += estatura
        
    else:
        print("La estatura debe ser mayor a 60cm! ")
        
    
if len(list_estaturas) > 0:
    promedio  = suma / len(list_estaturas)
    print(f"La estatura promedio del grupos es: {promedio}cm")
    
else:
    print("Las estaturas ingtesadas no son validas!")
    
