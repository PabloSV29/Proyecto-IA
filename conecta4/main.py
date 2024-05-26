# Trabajo de ramo IA.
import numpy as np
from random import *
from os import system

def gano(tablero, player,posicion):
    contador = 3
    if(contador == 0)
        return True
    if(tablero[]

def modificar_tablero(tablero,columna, player):
    for fila in range(tablero.shape[0]-1,-1,-1):
        elemento = tablero[fila, (columna-1)]
        if elemento == 0:
            if player == 'jugador_uno':
                tablero[fila,(columna-1)] = 1
            elif player == 'jugador_dos':
                tablero[fila,(columna-1)] = 2
            break


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
        system("clear")
        print(jugador_uno + ' En que columna quieres jugar?')
        print()
        print("\t",1,"\t",2,"\t",3,"\t",4,"\t",5,"\t",6,"\t",7)
        dibujar_tablero(tablero)
        numero = int(input())
        modificar_tablero(tablero, numero, 'jugador_uno')
        system("clear")
        print(jugador_dos + ' En que columna quieres jugar?')
        print()
        print("\t",1,"\t",2,"\t",3,"\t",4,"\t",5,"\t",6,"\t",7)
        dibujar_tablero(tablero)
        variable = int(input())
        modificar_tablero(tablero, variable, 'jugador_dos')

main()



