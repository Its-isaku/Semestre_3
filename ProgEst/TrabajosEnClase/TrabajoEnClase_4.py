print("Bienvenido al programa!")

volar = str(input("Tu personaje puede volar? [V][F]"))

if volar == 'V':
    Humano1 = str(input("Tu personaje es humano? [V][F]"))
    if Humano1 == 'V':
        mascara1 = str(input("Tu personaje tiene mascara? [V][F]"))
        if mascara1 == 'V':
            print("Tu peronaje es ironman!")
        
        else:
            print("Tu peronaje es capitan marvel!")
    else:
        if Humano1 == 'F':
            mascara2 = str(input("Tu personaje tiene mascara? [V][F]"))
            if mascara2 == 'V':
                print("Tu personaje es Ronan el acusador!")
            else:
                print("Tu peronaje es Vision!")
else:
    Humano2 = str(input("Tu personaje es humano? [V][F]"))
    if Humano2 == 'V':
        mascara3 = str(input("Tu personaje tiene mascara? [V][F]"))
        if mascara3 == 'V':
            print("Tu personaje es spiderman!")
            
        else:
            print("Tu personaje es hulk!")
    else:
        if Humano2 == 'F':
            mascara4 = str(input("Tu personaje tiene mascara? [V][F]"))
            if mascara4 == 'V':
                print("Tu personaje es Black Bolt!")
            else:
                print("tu personaje es Thanos!")
        
