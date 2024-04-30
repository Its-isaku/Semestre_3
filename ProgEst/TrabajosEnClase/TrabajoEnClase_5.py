import time

usuario = str("ADMIN")
contra = str("ADMIN123")

contador = 1

for i in range(5):
    usuario2 = str(input("usuario: "))
    usuario2 = usuario2.upper()
    contra2 = str(input("Passord: "))
    contra2 = contra2.upper()
    print("--------------------------")
    
    if(usuario == usuario2 and contra == contra2):
        print("bienvenido a tu cuenta! ")
        time.sleep(5)
        exit()
    
    else:
        contador += 1
    
    if (contador == 3):
        time.sleep(10)
        
        
    elif (contador == 5):
        print("Te voy a acusar con la fepade! ")
    
    