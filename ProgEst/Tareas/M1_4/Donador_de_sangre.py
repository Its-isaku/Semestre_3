Nombre = str(input("Cual es tu nombre? "))
print("---------------------------------------")
Genero = str(input("Cual es tu genero [H][M]: "))
print("---------------------------------------")

Edad = int(input("Que edad Tienes? "))
print("---------------------------------------")

if Edad >= 18 and Edad <= 65:
    Peso = int(input("Cual es tu peso? "))
    print("---------------------------------------")
    
    if Peso >= 50 and Peso <= 85:
        precion_aterialA = int(input("cual es tu precion Sistolica? "))
        print("---------------------------------------")
        
        if precion_aterialA >= 90 and precion_aterialA <=180:
            precion_aterialB = int(input("cual es tu precion Diastolica? "))
            print("---------------------------------------")
            
            if precion_aterialB >= 50 and precion_aterialB <= 100:
                pulso = int(input("Cual es tu pulso? "))
                print("---------------------------------------")
                
                if pulso >= 50 and pulso <= 110:
                    Hemoglobina = float(input("Cual es tu hemoglobina? "))
                    print("---------------------------------------")
                    
                    if Genero == 'H' and Hemoglobina >= 13.5 or Genero == 'M' and Hemoglobina >= 12.5:
                        Desayuno = str(input("Viene Desayunado [Si][No]: "))
                        print("---------------------------------------")
                        
                        if Desayuno == 'Si':
                            plaquetas = float(input("cuales son sus plaquetas? "))
                            print("---------------------------------------")
                            
                            if plaquetas >= 150.000:
                                proteinas = int(input("Cuales son tus proteinas? "))
                                print("---------------------------------------")
                                
                                if proteinas >= 6:
                                    print("Eres apto para donar!")
                                    print("---------------------------------------")
                                
                                else:
                                    print("No puedes donar porque no cumples con las proteinas  requeridas ")
                                
                            else:
                                print("No puedes donar porque no cumples con las plaquetas requeridas ")
                            
                        else:
                            print("No puedes donar porque no se puede donar en ayunas ")
                    
                    else:
                        print("No puedes donar porque tus niveles de hemoglobina no cunplen con el requerimiento")
                
                else:
                    print("No puedes donar porque no cumples con el pulso requerido ")
            
            else:
                print("No puedes donar porque no cumples con la precion arterial requerida ")    
            
        else:
            print("No puedes donar porque no cumples con la precion arterial requerida ")
    
    else:
        print("No puedes donar porque no cumples con el peso requerido")
    
else:
    print("No puedes donar porque no cumples con la edad requerida")