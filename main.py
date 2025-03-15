from utils import *

tablero_jugador = crear_tablero()
tablero_maquina = crear_tablero()

colocar_barcos(tablero_jugador)
colocar_barcos(tablero_maquina)

disparos_maquina = set()



while True:
    print("\n Tu tablero:")
    mostrar_tablero(tablero_jugador)

    print("\n Tablero de la máquina:")
    mostrar_tablero(np.where(tablero_maquina == "O", "_", tablero_maquina))  

   
    casilla = pedir_casilla_al_usuario()
    disparar(casilla, tablero_maquina)

    if juego_terminado(tablero_maquina):
        print("\n ¡Has ganado!")
        break

    disparo_maquina(tablero_jugador, disparos_maquina)

    if juego_terminado(tablero_jugador):
        print("\n La máquina ha ganado...")
        break

    