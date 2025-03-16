from utils import *

introduccion_juego()

tablero_jugador = crear_tablero()
tablero_maquina = crear_tablero()

colocar_barcos(tablero_jugador)
colocar_barcos(tablero_maquina)
disparos_maq = set()

while True: 
    print("El tabero se encuentra asi: ")
    print("\nEl tablero de la maquina\n")
    mostrar_tablero(tablero_maquina)
    mostrar_tablero(np.where(tablero_maquina == "O", "_", tablero_maquina))
    print("\n"
    "Su tablero\n")
    mostrar_tablero(tablero_jugador)


    disparar(tablero_maquina)
    disparo_maquina(tablero_jugador, disparos_maq)

    # for fila in tablero_jugador:
    #     for casilla in fila:
    #         if casilla != "O" and (casilla == "X" or casilla == "X" or casilla =="_"):
    #             print("La maquina ha ganado") 

    # for fila in tablero_maquina:
    #     for casilla in fila:
    #         if casilla != "O" and (casilla == "X" or casilla == "X" or casilla =="_"):
    #             print("Usted ha ganado")  
