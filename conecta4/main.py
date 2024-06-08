# Trabajo de ramo IA.
import numpy as np
from random import *
from os import system

def DFSL_gano(tablero, player, posicion, limite, acumulado):
    pos_y, pos_x = posicion
    print(f"La posicion: {pos_y,pos_x}. El limite es {limite} y el acumulado es {acumulado}")
    # Verificar que la posicion en donde estamos es una posicion correcta.
    if pos_y < 0 or pos_y >= len(tablero) or pos_x < 0 or pos_x >= len(tablero[0]) or limite < 0:
        print("Posicion Incorrecta. No cumple con alguno de los requerimientos")
        return None
    # Verificar caso base, es decir, que se hayan encontrado 4 fichas acumuladas.
    if player == 'jugador_uno':
        print("-----> JUGADOR UNO") 
        if tablero[pos_y, pos_x] == 1:
            acumulado = acumulado + 1 
            if acumulado == 3:
                return 'WIN'
            # Verificar arriba.
            print("## Verificar posicion arriba")
            DFSL_gano(tablero, 'jugador_uno', (pos_y - 1, pos_x), limite - 1, acumulado)
            # Verificar diagonal izquierda superior.
            print("## Verificar diagonal superior izquierda")
            DFSL_gano(tablero, 'jugador_uno', (pos_y - 1, pos_x - 1), limite - 1, acumulado)
            # Verificamos izquierda.
            print("## Verificar izquierda")
            DFSL_gano(tablero, 'jugador_uno', (pos_y, pos_x - 1), limite - 1, acumulado)
            # Verificamos diagonal izquierda inferior.
            print("## Verificar diagonal inferior izquierda")
            DFSL_gano(tablero, 'jugador_uno', (pos_y + 1, pos_x - 1), limite - 1, acumulado)
            # Verificamos abajo.
            print("## Verificar abajo")
            DFSL_gano(tablero, 'jugador_uno', (pos_y + 1, pos_x), limite - 1, acumulado)
            # Verificamos diagonal derecha inferior.
            print("## Verificar diagonal inferior derecha")
            DFSL_gano(tablero, 'jugador_uno', (pos_y + 1, pos_x + 1), limite - 1, acumulado)
            # Verificamos derecha.
            print("## Verificar derecha")
            DFSL_gano(tablero, 'jugador_uno', (pos_y, pos_x + 1), limite - 1, acumulado)
            # Verficamos diagonal derecha superior.
            print("## Verificar diagonal superior derecha")
            DFSL_gano(tablero, 'jugador_uno', (pos_y - 1, pos_x + 1), limite - 1, acumulado)
        else:
            return None

    elif player == 'jugador_dos':
        print("-----> JUGADOR DOS") 
        if tablero[pos_y, pos_x] != 2: 
            return None
        else:
            acumulado = acumulado + 1 
            if acumulado == 4:
                return 'WIN'
            else:
                # Verificar arriba.
                print("## Verificar posicion arriba")
                DFSL_gano(tablero, 'jugador_dos', (pos_y - 1, pos_x), limite - 1, acumulado)
                # Verificar diagonal izquierda superior.
                print("## Verificar diagonal superior izquierda")
                DFSL_gano(tablero, 'jugador_dos', (pos_y - 1, pos_x - 1), limite - 1, acumulado)
                # Verificamos izquierda.
                print("## Verificar izquierda")
                DFSL_gano(tablero, 'jugador_dos', (pos_y, pos_x - 1), limite - 1, acumulado)
                # Verificamos diagonal izquierda inferior.
                print("## Verificar diagonal inferior izquierda")
                DFSL_gano(tablero, 'jugador_dos', (pos_y + 1, pos_x - 1), limite - 1, acumulado)
                # Verificamos abajo.
                print("## Verificar abajo")
                DFSL_gano(tablero, 'jugador_dos', (pos_y + 1, pos_x), limite - 1, acumulado)
                # Verificamos diagonal derecha inferior.
                print("## Verificar diagonal inferior derecha")
                DFSL_gano(tablero, 'jugador_dos', (pos_y + 1, pos_x + 1), limite - 1, acumulado)
                # Verificamos derecha.
                print("## Verificar derecha")
                DFSL_gano(tablero, 'jugador_dos', (pos_y, pos_x + 1), limite - 1, acumulado)
                # Verficamos diagonal derecha superior.
                print("## Verificar diagonal superior derecha")
                DFSL_gano(tablero, 'jugador_dos', (pos_y - 1, pos_x + 1), limite - 1, acumulado)
    return None
    

def DFSL_ganoo(tablero, player, posicion, limite, acumulado):
    pos_y, pos_x = posicion
    print(f"La posicion: {pos_y,pos_x}. El limite es {limite} y el acumulado es {acumulado}")
    
    # Verificar que la posicion en donde estamos es una posicion correcta.
    if pos_y < 0 or pos_y >= len(tablero) or pos_x < 0 or pos_x >= len(tablero[0]) or limite < 0:
        print("Posicion Incorrecta. No cumple con alguno de los requerimientos")
        return None

    # Verificar el jugador actual y la condición de victoria.
    if player == 'jugador_uno':
        print("-----> JUGADOR UNO")
        if tablero[pos_y][pos_x] != 1:
            return None
        else:
            acumulado += 1
            if acumulado == 4:
                return 'WIN'
    elif player == 'jugador_dos':
        print("-----> JUGADOR DOS")
        if tablero[pos_y][pos_x] != 2:
            return None
        else:
            acumulado += 1
            if acumulado == 4:
                return 'WIN'

    # Verificar en todas las direcciones.
    directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    for dy, dx in directions:
        new_pos = (pos_y + dy, pos_x + dx)
        result = DFSL_gano(tablero, player, new_pos, limite - 1, acumulado)
        if result == 'WIN':
            return 'WIN'
    
    return None


def modificar_tablero(tablero,columna, player):
    posicion = (0,0) 
    for fila in range(tablero.shape[0]-1,-1,-1):
        elemento = tablero[fila, (columna-1)]
        if elemento == 0:
            if player == 'jugador_uno':
                tablero[fila,(columna-1)] = 1
                posicion = (fila,(columna-1))
                return posicion
            elif player == 'jugador_dos':
                tablero[fila,(columna-1)] = 2
                posicion = (fila,(columna-1))
                return posicion
    return none


def dibujar_tablero(tablero):
    for fila in tablero:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

def main():
    
    tablero = np.zeros((6,7), dtype=int)
    # tablero = np.random.randint(0,10, size=(6,7))
    jugador_uno = input("Nombre del jugador 1: ")
    jugador_dos = input("Nombre del jugador 2: ")
    while True:
        # system("clear")
        print(jugador_uno + ' En que columna quieres jugar?')
        print()
        print("\t",1,"\t",2,"\t",3,"\t",4,"\t",5,"\t",6,"\t",7)
        dibujar_tablero(tablero)
        numero = int(input())
        posicion = modificar_tablero(tablero, numero, 'jugador_uno')
        print(posicion)
        # system("clear")
        ss = DFSL_ganoo(tablero, 'jugador_uno', posicion,4,0)
        if ss == 'WIN': 
            dibujar_tablero(tablero)
            print(jugador_uno + " GANADOR!")
            break
            
        print(jugador_dos + ' En que columna quieres jugar?')
        print()
        print("\t",1,"\t",2,"\t",3,"\t",4,"\t",5,"\t",6,"\t",7)
        dibujar_tablero(tablero)
        variable = int(input())
        posicion = modificar_tablero(tablero, variable, 'jugador_dos')
        ss = DFSL_ganoo(tablero, 'jugador_dos', posicion,4,0)
        if ss == 'WIN':
            dibujar_tablero(tablero)
            print(jugador_uno + " GANADOR!")
            break
        # system("clear")
main()



