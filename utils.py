import random
import numpy as np


def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, '_')

def colocar_barco(barco, tablero):
    for h,v in barco: 
        tablero [h,v] == "O"


def crear_barco_aleatorio(eslora, tablero):
    while True: 
        orientacion = random.choice(["Horizontal", "Vertical"])
        barco_aleatorio = []

        if orientacion == "Horizontal": 
            fila = random.randint(0, 9)
            columna = random.randint(0, 10 - eslora)
            for i in range(eslora): 
                barco_aleatorio.append((fila, columna + i))
        else: 
            columna = random.randint(0, 9)
            fila = random.randint(0, 10 - eslora)
            for i in range(eslora): 
                barco_aleatorio.append((fila + i, columna))

        valido = True
        for h, v in barco_aleatorio: 
            if tablero[h, v] != "_": 
                valido = False
                break  # no hace falta volver a llamar a la función, el while se repite solo
        
        if valido: 
            return barco_aleatorio
        


def colocar_barcos(tablero):
    esloras = [2, 2, 2, 3, 3, 4]
    for eslora in esloras:
        barco_valido = crear_barco_aleatorio(eslora, tablero)
        for h, v in barco_valido:
            tablero[h, v] = "O"

# def mostrar_tablero(tablero):
#     print("   0 1 2 3 4 5 6 7 8 9")  
#     print("  ---------------------")
#     for i in range(10):
#         fila = " ".join(tablero[i])
#         print(f"{i}| {fila}")

def mostrar_tablero(tablero, ocultar_barcos=False):
    print("   0 1 2 3 4 5 6 7 8 9")  
    print("  ---------------------")
    for i in range(10):
        fila = []
        for casilla in tablero[i]:
            if ocultar_barcos and casilla == "O":
                fila.append("_")
            else:
                fila.append(casilla)
        print(f"{i}| " + " ".join(fila))



def disparar(tablero):
    while True:
    
        fila = int(input("Introduce la fila (0-9): "))
        columna = int(input("Introduce la columna (0-9): "))
            
        if not (0 <= fila <= 9 and 0 <= columna <= 9):     
            print("Has disparado fuera del tablero. Intenta de nuevo")
            continue  

        if tablero[fila, columna] == "O":
            print(" Acertaste!")
            tablero[fila, columna] = "X"
            break

        elif tablero[fila, columna] in ("X", "A"):
            print(" Ya habías disparado ahí.")
            continue  
        
        else:
            print(" Fallaste ")
            tablero[fila, columna] = "A"
            break


def disparo_maquina(tablero, disparos_maq):
    while True:
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        casilla = (fila, columna)  

        if casilla not in disparos_maq:
            disparos_maq.add(casilla)
            print("La máquina dispara a ", casilla)
    
        if tablero[casilla] == "O":
            print("La máquina ha acertado")
            tablero[casilla] = "X"
        else:
            print("La máquina ha fallado")
            tablero[casilla] = "A"
        return tablero 

    

def juego_terminado(tablero):
    aun_hay_barcos = True
    while aun_hay_barcos: 
        for fila in tablero:
            for casilla in fila:
                if casilla != "O":               
                    aun_hay_barcos = False 
    return ("El juego ha terminado")