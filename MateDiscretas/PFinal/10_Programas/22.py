import random

def crear_torneo_equipos(equipos):
    random.shuffle(equipos)
    return equipos

def ronda_torneo(equipos):
    if len(equipos) % 2 != 0:
        equipos.append(None)  # Añadir bye si el número de equipos es impar
    enfrentamientos = []
    for i in range(0, len(equipos), 2):
        enfrentamientos.append((equipos[i], equipos[i+1]))
    return enfrentamientos

def ganador_enfrentamiento(enfrentamiento):
    return random.choice(enfrentamiento)

def torneo_eliminacion(equipos):
    ronda = 1
    while len(equipos) > 1:
        print(f"Ronda {ronda}:")
        enfrentamientos = ronda_torneo(equipos)
        equipos = []
        for enfrentamiento in enfrentamientos:
            if enfrentamiento[1] is None:
                ganador = enfrentamiento[0]
            else:
                ganador = ganador_enfrentamiento(enfrentamiento)
            equipos.append(ganador)
            print(f"{enfrentamiento[0]} vs {enfrentamiento[1]} -> Ganador: {ganador}")
        ronda += 1
    print(f"El campeón es: {equipos[0]}")

equipos = ['America', 'Cholos', 'Cruz azul', 'Pumas', 'Liverpool','Manchester city','Necaxa','Barcelona','Real Madrid','Juventus','Oporto','Chelsea','Arsenal','Toluca','Leon','Monterrey']
equipos = crear_torneo_equipos(equipos)
torneo_eliminacion(equipos)
