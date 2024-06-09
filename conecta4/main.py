# Trabajo de ramo IA.
import numpy as np
from random import *
from os import system

def gano(tablero, jugador):

    numFil = len(tablero)
    numCol = len(tablero[0])

    if jugador == 'jugador_uno':
        valor_ficha = 1
    elif jugador == 'jugador_dos':
        valor_ficha = 2

    # Verificar las horizontales
    for fila in range(numFil):
        for col in range(numCol - 3):
            if tablero[fila][col] == valor_ficha and tablero[fila][col + 1] == valor_ficha and tablero[fila][col + 2] == valor_ficha and tablero[fila][col + 3] == valor_ficha:
                return True 

    # Verificar verticales
    for fila in range(numFil - 3):
        for col in range(numCol):
            if tablero[fila][col] == valor_ficha and tablero[fila + 1][col] == valor_ficha and tablero[fila + 2][col] == valor_ficha and tablero[fila + 3][col] == valor_ficha:
                return True 
    
    # Verificar diagonal hacia der.
    for fila in range(numFil - 3):
        for col in range(numCol - 3):
            if tablero[fila][col] == valor_ficha and tablero[fila + 1][col + 1] == valor_ficha and tablero[fila + 2][col + 2] == valor_ficha and tablero[fila + 3][col + 3] == valor_ficha:
                return True

    # Verificar diagonal hacia izq.
    for fila in range(3, numFil):
        for col in range(numCol - 3):
            if tablero[fila][col] == valor_ficha and tablero[fila - 1][col + 1] == valor_ficha and tablero[fila - 2][col + 2] == valor_ficha and tablero[fila - 3][col + 3] == valor_ficha:
                return True


    return False

def dibujar_tablero(tablero):
    for fila in tablero:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

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
        if gano(tablero, 'jugador_uno'):
            dibujar_tablero(tablero)
            print(jugador_uno + " GANADOR!")
            break
            
        print(jugador_dos + ' En que columna quieres jugar?')
        print()
        print("\t",1,"\t",2,"\t",3,"\t",4,"\t",5,"\t",6,"\t",7)
        dibujar_tablero(tablero)
        variable = int(input())
        posicion = modificar_tablero(tablero, variable, 'jugador_dos')
        if gano(tablero, 'jugador_dos'):
            dibujar_tablero(tablero)
            print(jugador_dos + " GANADOR!")
            break
        # system("clear")
main()



