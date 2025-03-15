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

def mostrar_tablero(tablero):
    print("   0 1 2 3 4 5 6 7 8 9")  
    print("  ---------------------")
    for i in range(10):
        fila = " ".join(tablero[i])
        print(f"{i}| {fila}")


def disparar(casilla, tablero):
    fila, columna = casilla
    if  fila > 10 or fila < 0 and columna > 10 and columna < 0: 
        print("has disparado fuera del tablero, prueba de nuevo!!")
        return disparar(casilla, tablero)  

    if tablero[casilla] == "O":
        print("Acertaste")
        tablero[casilla] = "X"
        return tablero
    
    elif tablero[casilla] == "X" or tablero[casilla] == "A": 
        print("Ya habias disparado ahi previamente!!")
        return disparar(casilla, tablero)
    else:
        print("Fallaste")
        tablero[casilla]  = "A"
        return tablero

def donde_disparo():
    fila = int(input("Introduce la fila (0-9): "))
    columna = int(input("Introduce la columna (0-9): "))
    if 0 <= fila <= 9 and 0 <= columna <= 9:
        return (fila, columna)
    else:
       print(" Coordenadas fuera del tablero. Intenta de nuevo.")


def disparo_maquina(tablero, disparos_maq):
    casilla = fila, columna
    while True:
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        if (fila, columna) not in disparos_maq:
            disparos_maq.add((fila, columna))
            print("la máquina dispara a ({fila}, {columna})")
            disparar_maq(casilla, tablero) 
            break
        else: disparo_maquina(tablero, disparos_maq)

def resultado_disparo_maq(casilla, tablero):
    casilla = fila, columna
    if tablero[casilla] == "O":
        print("La maquina ha acertado")
        tablero[casilla] = "X"
        return tablero
    else:
        print("La maquina ha")
        tablero[casilla]  = "A"
        return tablero
    

def juego_terminado(tablero):
    aun_hay_barcos = True
    while aun_hay_barcos: 
        for fila in tablero:
            for casilla in fila:
                if casilla != "O":               
                    aun_hay_barcos = False 
    return ("El juego ha terminado")