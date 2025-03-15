from utils import *

tablero_jugador = crear_tablero()
tablero_maquina = crear_tablero()

colocar_barcos(tablero_jugador)
colocar_barcos(tablero_maquina)

disparos_maquina = set()



def main():
    tablero_jugador = crear_tablero()
    tablero_maquina = crear_tablero()
    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_maquina)
    disparos_maq = set()

    while True:
        print("\n Tu tablero:")
        mostrar_tablero(tablero_jugador)

        print("\n Tablero enemigo (oculto):")
        mostrar_tablero(np.where(tablero_maquina == "O", "_", tablero_maquina))

        print("\n Tu turno:")
        disparar(tablero_maquina)

        if juego_terminado(tablero_maquina):
            print(" ¡Has ganado!")
            break

        print("\n Turno de la máquina:")
        disparo_maquina(tablero_jugador, disparos_maq)

        if juego_terminado(tablero_jugador):
            print(" La máquina ha ganado.")
            break
