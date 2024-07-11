# Trabajo del ramo IA
# JUEGO CONECTA 4 CON ALGORITMO MINIMAX.


import numpy as np
from random import *
import pygame
import sys
import math

# Esta matriz contiene los valores 
matriz_puntuacion = np.array([
    [3, 4, 5, 7, 5, 4, 3],
    [4, 6, 8, 10, 8, 6, 4],
    [5, 8, 11, 13, 11, 8, 5], 
    [5, 8, 11, 13, 11, 8, 5],
    [4, 6, 8, 10, 8, 6, 4],
    [3, 4, 5, 7, 5, 4, 3]
])
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0 ,0 ,0)
GREEN = (0,255,00)
def crear_tablero():
    tablero = np.zeros((6,7), dtype=int)
    return tablero


def print_tablero(tablero):
    for fila in tablero:
        for col in fila:
            print(col, end=' ')
        print()


def dibujar_tablero(tablero):
    for fila in tablero:
        for tupla in fila:
            print(tupla[0], end=' ')
        print()

def col_valida(tablero, col):
    #col = int(col)
    if tablero[0][col] == 0:
        return True
    else:
        return False

def fila_disponible(tablero, col):
    for i in range(len(tablero) -1, -1, -1): # Esto recorre la matriz desde abajo hacia arriba. Por ejemplo, si estamos en la col = 3, este for empezaria a leer desde la columna 3 pero fila 5, luego col 3 fila 4, col 3 fila 3, etc. Teniendo en cuenta que la cantidad de filas es 6 y va desde 0 hasta 5.
        if tablero[i][col]== 0:
            return i
    
def insertar_ficha(tablero, col, ficha):
    fila = fila_disponible(tablero, col)
    tablero[fila][col] = ficha 

def puntaje_posicion(tablero, ficha): # Esta funcion es importante porque nos ayuda a tener la heuristica 
    numFil = len(tablero)
    numCol = len(tablero[0])
    puntaje = 0

    # Obtiene el puntaje de la matriz. Basicamente suma los valores de la matriz_puntuacion en donde existan fichas que sean igual a la variable ficha pasada en el argumento de la funcion. Aca la idea es ir sumando los puntajes en donde estan nuestras fichas e ir restando este valor con el puntaje que tiene el oponente. 
    for i in range(numFil):
        for j in range(numCol):
            if tablero[i][j] == ficha:
                puntaje = puntaje + matriz_puntuacion[i][j]
            elif tablero[i][j] != 0:
                puntaje = puntaje - matriz_puntuacion[i][j]
    return puntaje

def posiciones_disp(tablero):
    numCol = len(tablero[0])
    posiciones = []
    for col in range(numCol):
        if col_valida(tablero, col):
            posiciones.append(col)
    return posiciones

def estado_final(tablero):
    listaPosiciones = posiciones_disp(tablero)
    # Caso donde gano el jugador. Caso donde gano la IA. Caso donde no hay mas posiciones disponibles en el tablero. 
    if gano(tablero, 1) or gano(tablero, 2) or listaPosiciones == []:
        return True

def minimax(tablero, profundidad, alpha, beta, maximizingPlayer): # PseudoCodigo obtenido de wikipedia. Link: https://en.wikipedia.org/wiki/minimax
    listaPosiciones = posiciones_disp(tablero) # Lista de columnas donde se puede jugar.
    estadoJuego = estado_final(tablero) # False cuando el juego aun no ha terminado, True cuando el juego ya termino. 

    if profundidad == 0 or estadoJuego == True:
        if estadoJuego == True: # Caso donde el juego ha termina.
            if gano(tablero, 2): # Si la IA gano retorna un puntaje muy alto para priorizar esta rama de movimientos. 
                return (None, 100000000000000)
            elif gano(tablero, 1): # Si el jugador gana, retorna un puntaje muy bajo para no seguir esta rama de movimientos.
                return (None, -100000000000000)
            else: # Caso de empate
                return (None, 0)
        else: # Caso donde la profundidad de exploracion se volvio cero. 
            return (None, puntaje_posicion(tablero, 2))

    if maximizingPlayer == True:
        valor = -np.inf 
        columna = np.random.choice(listaPosiciones)
        for col in listaPosiciones:
            fila = fila_disponible(tablero, col)
            tablero_aux = tablero.copy()
            insertar_ficha(tablero_aux, col, 2) # IA hace el movimiento. 
            nuevo_puntaje = minimax(tablero_aux, profundidad - 1, alpha, beta, False)[1] # Se pasa el false porque tiene que pasar a minimizar el avance del contrario. 
            if nuevo_puntaje > valor:
                valor = nuevo_puntaje
                columna = col
            alpha = max(alpha, valor)
            if alpha >= beta:
                break
        return columna, valor
    else:
        valor = np.inf
        columna = np.random.choice(listaPosiciones)
        for col in listaPosiciones:
            fila = fila_disponible(tablero, col)
            tablero_aux = tablero.copy()
            insertar_ficha(tablero_aux, col, 1)
            nuevo_puntaje = minimax(tablero_aux, profundidad - 1, alpha, beta, True)[1]
            if nuevo_puntaje < valor:
                valor = nuevo_puntaje
                columna = col
            beta = min(beta, valor)
            if alpha >= beta:
                break
        return columna, valor

def gano(tablero, valor_ficha):

    numFil = len(tablero)
    numCol = len(tablero[0])

    
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

def dibujar_tablero1(tablero):
    #Construccion en base a las columnaas y filas
    for c in range(7):
        for f in range(6):
            #Dibujo del tablero
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE, f*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            #Esta parte para que los espacios vacios se muestren como un circulo negro
            if tablero[f][c] == 0:
                pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2),int(f*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
                #Ficha del jugador
            elif tablero[f][c] == 1:
                pygame.draw.circle(screen,RED,(int(c*SQUARESIZE+SQUARESIZE/2),int(f*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
                #Ficha de la IA
            else:
                pygame.draw.circle(screen,GREEN,(int(c*SQUARESIZE+SQUARESIZE/2),int(f*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
    pygame.display.update()

pygame.init()
SQUARESIZE = 100
width = 7 * SQUARESIZE
height = (7) * SQUARESIZE
size = (width,height)
RADIUS = int(SQUARESIZE/2 - 5)
screen = pygame.display.set_mode(size)

def main():
    
    tablero = crear_tablero()
    print_tablero(tablero)
    #Si se deja con input no funciona y se muere :c
    #jugador = input("Ingresa tu nombre: ")
    jugador = "REAL"
    moneda = np.random.randint(2)
    #moneda = 1
    win = False   
    
    dibujar_tablero1(tablero)
    pygame.display.update()

    if moneda == 0:
        # Turno del jugador.
        print(f"COMIENZA {jugador}!")
    else:
        # Turno de la IA
        print("COMIENZA LA IA!")
    while not win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Para hacer el movimiento de la ficha del jugador REAL
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK,(0,0, width, SQUARESIZE))
                pos_x = event.pos[0]
                if moneda == 0:
                    pygame.draw.circle(screen, RED,(pos_x, int(SQUARESIZE/2)),RADIUS)
            pygame.display.update()
            if moneda == 0: 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #print(event.pos)       
                    # Turno del jugador.
                    pos_x = event.pos[0]
                    col = int(math.floor(pos_x/SQUARESIZE))
                    #col = int(input("Ingresa la columna donde quieres jugar en el rango de 0-6:"))
                    if col_valida(tablero, col):
                        insertar_ficha(tablero, col, 1) # El jugador ocupara la ficha 1
                        if gano(tablero, 1):
                            print(f"{jugador} HA GANADO!")
                            win = True
                        else:
                            moneda = 1
                    else:
                        print("Ingresa una columna disponible")
                        continue
                    #Descomentar esta parte de aqui si se quiere ver el tablero por la terminal
                    #print_tablero(tablero)
            else:
                # Turno de la IA.
                print("TURNO DE LA IA")
                print()
                col, puntaje = minimax(tablero, 4, -np.inf, np.inf, True) # Profundidad de 4. No ocupamos el puntaje, solo lo ocupamos dentro de las llamadas recursivas.
                if col_valida(tablero, col):
                    insertar_ficha(tablero, col, 2) # La IA ocuprara la ficha 2.
                    if gano(tablero, 2):
                        print("LA IA HA GANADO")
                        win = True
                    else:
                        moneda = 0
                else:
                    print("flag de error, IA mal posicion")
                    continue
            #Mismo punto que el anterior
            #print_tablero(tablero)
            dibujar_tablero1(tablero)

main()
