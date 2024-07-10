# Trabajo de ramo IA.
import math
import numpy as np
from random import *
from os import system

tablero = [
    [(0,3),(0,4),(0,5),(0,7),(0,5),(0,4),(0,3)],
    [(0,4),(0,6),(0,8),(0,10),(0,8),(0,6),(0,4)],
    [(0,5),(0,7),(0,11),(0,13),(0,11),(0,7),(0,5)],
    [(0,5),(0,7),(0,11),(0,13),(0,11),(0,7),(0,5)],
    [(0,4),(0,6),(0,8),(0,10),(0,8),(0,6),(0,4)],
    [(0,3),(0,4),(0,5),(0,7),(0,5),(0,4),(0,3)],
]

def score(tablero):
    puntaje_jugador = 0
    puntaje_IA = 0 
    
    numFil = len(tablero)
    numCol = len(tablero[0])

    for fila in range(numFil):
        for col in range(numCol):
            if tablero[fila][col][0] == 1: # si es una ficha del jugador humano, se suma.
                puntaje_jugador = puntaje_jugador + tablero[fila][col][1]
            elif tablero[fila][col][0] == 2: # si es la ficha del jugador IA
                puntaje_IA = puntaje_IA + tablero[fila][col][1]

    return puntaje_IA - puntaje_jugador

def is_terminal_board(tablero):
    if gano(tablero, 'jugador') and gano(tablero, 'jugador_IA') and all(tablero[0][i][0] != 0 for i in range(7)):
        return True
    else:
        return False

def obtener_col_disponibles(tablero):
    col_disponibles = []
    for i in range(7):
        if tablero[0][i][0] == 0:
            print("Encontre una columna disponible")
            col_disponibles.append(i) 
    return col_disponibles


def alphabeta(tablero, depth, a, b, maximizingPlayer):
    col_disponibles = obtener_col_disponibles(tablero)
    print(f"Estas son las columnas disponibles: {col_disponibles}")
    is_terminal = is_terminal_board(tablero)
    print(f"Es terminal? {is_terminal}")
    if depth == 0 or is_terminal:
        if is_terminal:
            if gano(tablero,'jugador'):
                return None, -1000000
            elif gano(tablero, 'jugador_IA'):
                return None,1000000
            else:
                return None,0 # empate.
        elif depth == 0:
            return None,score(tablero)

    if maximizingPlayer:
        value = -math.inf
        col_return = 0
        for columna in col_disponibles:
            pos = buscar_pos_disponible(tablero, columna) 
            copy_tablero = tablero
            modificar_tablero(copy_tablero, pos,'jugador_IA')
            nuevo_puntaje = alphabeta(copy_tablero, depth - 1, a, b, False)
            if nuevo_puntaje[1] > value:
                value = nuevo_puntaje[1]
                col_return = columna 
            a = max(a, value)
            if a >= b: 
                break
        return col_return, value
    else: 
        value = math.inf
        col_return = 0
        for columna in col_disponibles:
            pos = buscar_pos_disponible(tablero, columna) 
            copy_tablero = tablero
            modificar_tablero(copy_tablero, pos,'jugador')
            nuevo_puntaje = alphabeta(copy_tablero, depth - 1, a, b, True)
            if nuevo_puntaje[1] < value:
                value = nuevo_puntaje[1]
                col_return = columna 
            b = min(b, value)
            if a >= b: 
                break
        return col_return, value 

def gano(tablero, jugador):

    numFil = len(tablero)
    numCol = len(tablero[0])

    if jugador == 'jugador':
        valor_ficha = 1
    elif jugador == 'jugador_IA':
        valor_ficha = 2
    
    # Verificar las horizontales
    for fila in range(numFil):
        for col in range(numCol - 3):
            if tablero[fila][col][0] == valor_ficha and tablero[fila][col + 1][0] == valor_ficha and tablero[fila][col + 2][0] == valor_ficha and tablero[fila][col + 3][0] == valor_ficha:
                return True 

    # Verificar verticales
    for fila in range(numFil - 3):
        for col in range(numCol):
            if tablero[fila][col][0] == valor_ficha and tablero[fila + 1][col][0] == valor_ficha and tablero[fila + 2][col][0] == valor_ficha and tablero[fila + 3][col][0] == valor_ficha:
                return True 
    
    # Verificar diagonal hacia der.
    for fila in range(numFil - 3):
        for col in range(numCol - 3):
            if tablero[fila][col][0] == valor_ficha and tablero[fila + 1][col + 1][0] == valor_ficha and tablero[fila + 2][col + 2][0] == valor_ficha and tablero[fila + 3][col + 3][0] == valor_ficha:
                return True

    # Verificar diagonal hacia izq.
    for fila in range(3, numFil):
        for col in range(numCol - 3):
            if tablero[fila][col][0] == valor_ficha and tablero[fila - 1][col + 1][0] == valor_ficha and tablero[fila - 2][col + 2][0] == valor_ficha and tablero[fila - 3][col + 3][0] == valor_ficha:
                return True


    return False

def dibujar_tablero(tablero):
    for fila in tablero:
        for tupla in fila:
            print(tupla[0], end=' ')
        print()


def buscar_pos_disponible(tablero, columna):
    for i in range(len(tablero) -1, -1, -1):
        if tablero[i][columna][0] == 0:
            return i,columna
    return 

def modificar_tablero(tablero, pos, jugador):
    print(f"Posicion recibida en modificar tablero {pos}")
    fila,columna = pos
    tupla_antigua = tablero[fila][columna]
    print(f"tupla antigua = {tupla_antigua}")
    valor = 0 
    if jugador == 'jugador':
        tablero[fila][columna] = (1, tupla_antigua[1])
    elif  jugador == 'jugador_IA':
        tablero[fila][columna] = (2, tupla_antigua[1])  
    print(tablero[fila][columna])


def main():
    
   # Tablero fijo. Preguntarse como podria variar para que sea mas grande.
    tablero = [
        [(0,3),(0,4),(0,5),(0,7),(0,5),(0,4),(0,3)],
        [(0,4),(0,6),(0,8),(0,10),(0,8),(0,6),(0,4)],
        [(0,5),(0,7),(0,11),(0,13),(0,11),(0,7),(0,5)],
        [(0,5),(0,7),(0,11),(0,13),(0,11),(0,7),(0,5)],
        [(0,4),(0,6),(0,8),(1,10),(0,8),(0,6),(0,4)],
        [(0,3),(0,4),(0,5),(2,7),(0,5),(0,4),(0,3)],
    ]

    
    # tablero = np.zeros((6,7), dtype=int)
    # tablero = np.random.randint(0,10, size=(6,7))
    jugador_humano = input("Nombre del jugador: ")
    comienza = np.random.randint(0,1)
    win = False 
    if comienza == 1:
        print("COMIENZA EL JUGADOR! ;D") 
    else:
        print("COMIENZA LA IA! :p")
    print(f"COMIENZA: {comienza}")
    # calcular_score(tablero)
    while not win:
        if comienza == 1:
            # system("clear")
            print(jugador_humano + ' en que columna quieres jugar?')
            print()
            print(1,2,3,4,5,6,7)
            dibujar_tablero(tablero)
            # print(f"diferencia de puntaje: {score(tablero)}")
            columna = int(input())
            modificar_tablero(tablero, buscar_pos_disponible(tablero,columna-1), 'jugador')
            if gano(tablero, 'jugador'):
                print(jugador_humano + 'GANASTE!!')
                win = True
            else:
                comienza = 0
        else:
            # system("clear")
            tupla = alphabeta(tablero, 5, -math.inf, math.inf, True)
            print(f"TUPLA: {tupla}")
            modificar_tablero(tablero, buscar_pos_disponible(tablero, tupla[0]), 'jugador_IA')
            print(1,2,3,4,5,6,7)
            dibujar_tablero(tablero)
            if gano(tablero, 'jugador_IA'):
                print("LA IA A GANADO ESTA PARTIDA")
                win = True
            else:
                comienza = 1


main()



