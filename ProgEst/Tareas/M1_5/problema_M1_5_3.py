import random

N = int(input("Dame el numero de iteraciones: "))  

for i in range(N):
    B = random.randrange(1, 10)
    b = random.randrange(1, 10)
    h  =random.randrange(1, 10)
    Area = ((B + b)/2) * h
    
    if (Area >= 16 and Area <= 19):
        print(Area)
        print(f"El valor B es {B}")
        print(f"El valor b es {b}")
        print(f"El valor h es {h}")    
        



