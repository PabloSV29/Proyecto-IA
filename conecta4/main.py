# Trabajo de ramo IA.
import numpy as np
from random import *
from os import system

def gano(tablero, player, posicion):
    fila, columna = posicion
    print(fila)
    print(columna)
    print(tablero[fila,columna]) 
    contador = 0
    if player == 'jugador_uno':

        # Verificar lado derecho.
        while (columna + 1) < 7 and tablero[fila,columna+1] == 1:
            contador = contador +1
            columna = columna +1
            if contador == 3:
                return("WIN")
        contador = 0        
        # Verificar diagonal derecho superior 
        while (columna + 1) < 7 and (fila - 1) >= 0 and tablero[fila-1,columna+1] == 1:
            contador = contador + 1
            columna = columna + 1
            fila = fila - 1
            if contador == 3:
                return("WIN")
        # Verificar arriba
        while (fila - 1) >= 0 and tablero[fila - 1, columna] == 1:
            contador = contador + 1 
            fila = fila - 1
            if contador == 3:
                return("WIN")
        contador = 0
        # Verificar diagonal izquierdo superior
        while (columna - 1) >= 0 and (fila - 1) >= 0 and tablero[fila-1,columna-1] == 1:
            contador = contador + 1
            columna = columna - 1 
            fila = fila - 1 
            if contador == 3:
                return("WIN")
        contador = 0
        # Verificar izquierda
        while (columna - 1) >= 0 and tablero[fila, columna-1] == 1:
            contador = contador + 1 
            columna = columna -1 
            if contador == 3:
                return("WIN")
        contador = 0
        # Verificar diagonal izquierdo inferior
        while (columna - 1) >=0 and (fila + 1) < 6 and tablero[fila+1,columna-1] == 1:
            contador = contador + 1 
            columna = columna -1
            fila = fila + 1 
            if contador == 3:
                return("WIN")
        contador = 0
        # Verificar abajo
        while (fila + 1) < 6 and tablero[fila+1,columna] == 1:
            contador = contador + 1 
            fila = fila + 1 
            if contador == 3:
                return("WIN")
        contador = 0
        # Verificar diagonal derecho inferior
        while (columna + 1) < 7 and (fila + 1) < 6 and tablero[fila+1,columna+1] == 1:
            contador = contador + 1 
            columna = columna + 1 
            fila = fila + 1 
            if contador == 3:
                return("WIN")
        contador = 0

    elif player == 'jugador_dos':
        # Verificar lado derecho.
        while (columna + 1) < 7 and tablero[fila,columna+1] == 2:
            contador = contador +1
            columna = columna +1
            if contador == 3:
                return("WIN")
        contador = 0        
        # Verificar diagonal derecho superior 
        while (columna + 1) < 7 and (fila - 1) >= 0 and tablero[fila-1,columna+1] == 2:
            contador = contador + 1
            columna = columna + 1
            fila = fila - 1
            if contador == 3:
                return("WIN")
        # Verificar arriba
        while (fila - 1) >= 0 and tablero[fila - 1, columna] == 2:
            contador = contador + 1 
            fila = fila - 1
            if contador == 3:
                return("WIN")
        contador = 0
        # Verificar diagonal izquierdo superior
        while (columna - 1) >= 0 and (fila - 1) >= 0 and tablero[fila-1,columna-1] == 2:
            contador = contador + 1
            columna = columna - 1 
            fila = fila - 1 
            if contador == 3:
                return("WIN")
        contador = 0
        # Verificar izquierda
        while (columna - 1) >= 0 and tablero[fila, columna-1] == 2:
            contador = contador + 1 
            columna = columna -1 
            if contador == 3:
                return("WIN")
        contador = 0
        # Verificar diagonal izquierdo inferior
        while (columna - 1) >=0 and (fila + 1) < 6 and tablero[fila+1,columna-1] == 2:
            contador = contador + 1 
            columna = columna -1
            fila = fila + 1 
            if contador == 3:
                return("WIN")
        contador = 0
        # Verificar abajo
        while (fila + 1) < 6 and tablero[fila+1,columna] == 2:
            contador = contador + 1 
            fila = fila + 1 
            if contador == 3:
                return("WIN")
        contador = 0
        # Verificar diagonal derecho inferior
        while (columna + 1) < 7 and (fila + 1) < 6 and tablero[fila+1,columna+1] == 2:
            contador = contador + 1 
            columna = columna + 1 
            fila = fila + 1 
            if contador == 3:
                return("WIN")
        contador = 0


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
        system("clear")
        print(jugador_uno + ' En que columna quieres jugar?')
        print()
        print("\t",1,"\t",2,"\t",3,"\t",4,"\t",5,"\t",6,"\t",7)
        dibujar_tablero(tablero)
        numero = int(input())
        posicion = modificar_tablero(tablero, numero, 'jugador_uno')
        print(posicion)
        system("clear")
        ss = gano(tablero,'jugador_uno',posicion)
        if ss == 'WIN': 
            print(jugador_uno + " GANADOR!")
            break
            
        print(jugador_dos + ' En que columna quieres jugar?')
        print()
        print("\t",1,"\t",2,"\t",3,"\t",4,"\t",5,"\t",6,"\t",7)
        dibujar_tablero(tablero)
        variable = int(input())
        posicion = modificar_tablero(tablero, variable, 'jugador_dos')
        ss = gano(tablero, 'jugador_uno', posicion)
        if ss == 'WIN':
            print(jugador_uno + " GANADOR!")
            break
        system("clear")
main()



