import sys
import pygame
import numpy as np

pygame.init()

#colores 
WHITE = '#fbf7f5'
GRAY = '#848484'
RED = '#ff6666'
GREEN = '#00ff99'
BLACK = '#3c3c3c'

#configuracion de ventana
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe con IA")
screen.fill(BLACK)

board = np.zeros((BOARD_ROWS, BOARD_COLS))

def dibuja_lineas(color = WHITE):
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, color, start_pos = (0, SQUARE_SIZE * i), end_pos= (WIDTH, SQUARE_SIZE * i))
        pygame.draw.line(screen, color, start_pos = (SQUARE_SIZE * i, 0), end_pos= (SQUARE_SIZE * i, WIDTH))

def dibuja_figuras(color = WHITE):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, center=(int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), radius=CIRCLE_RADIUS, width=CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, start_pos = (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), end_pos= (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), width=CROSS_WIDTH)
                pygame.draw.line(screen, color, start_pos = (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), end_pos= (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), width=CROSS_WIDTH)

def Marcar_cuadrado(row, col, player):
    board[row][col] = player
                
def cuadrado_disponible(row, col):
    return board[row][col] == 0

def revisartablero_lleno(check_board = board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if check_board[row][col] == 0:
                return False
    return True

def revisar_ganador(player, check_board = board):
    for col in range(BOARD_COLS):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            return True
        
    for row in range(BOARD_ROWS):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            return True
        
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True
    
    if check_board[0][2] == player and check_board[1][1] == player and check_board[2][0] == player:
        return True
    
    return False

def minmax(minmax_board, depth, is_maximizing):
    if revisar_ganador(2, minmax_board):
        return float('inf')
    elif revisar_ganador(1, minmax_board):
        return float('-inf')
    elif revisartablero_lleno(minmax_board):
        return 0

    if is_maximizing:
        mejor_puntaje = -1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if minmax_board[row][col] == 0:
                    minmax_board[row][col] = 2
                    puntaje = minmax(minmax_board, depth + 1, is_maximizing = False)
                    minmax_board[row][col] = 0
                    mejor_puntaje = max(puntaje, mejor_puntaje)
        return mejor_puntaje
    else:
        mejor_puntaje = 1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if minmax_board[row][col] == 0:
                    minmax_board[row][col] = 1
                    puntaje = minmax(minmax_board, depth + 1, is_maximizing = True)
                    minmax_board[row][col] = 0
                    mejor_puntaje = min(puntaje, mejor_puntaje)
        return mejor_puntaje
    
def Mejor_Jugada():
    Mejor_puntaje = -1000
    mueve = (-1, -1)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                puntaje = minmax(board, depth = 0, is_maximizing = False)
                board[row][col] = 0
                if puntaje > Mejor_puntaje:
                    Mejor_puntaje = puntaje
                    mueve = (row, col)

    if mueve != (-1, -1):
        Marcar_cuadrado(mueve[0],mueve[1], player = 2)
        return True
    return False

def Reiniciar_juego():
    screen.fill(BLACK)
    dibuja_lineas()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

dibuja_lineas()

player = 1

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // SQUARE_SIZE
            mouseY = event.pos[1] // SQUARE_SIZE

            if cuadrado_disponible(mouseY, mouseX):
                Marcar_cuadrado(mouseY, mouseX, player)
                if revisar_ganador(player):
                    game_over = True
                player = player % 2 + 1

                if not game_over:
                    if Mejor_Jugada():
                        if revisar_ganador(2):
                            game_over = True
                        player = player % 2 + 1

                if not game_over:
                    if revisartablero_lleno():
                        game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Reiniciar_juego()
                game_over = False
                player = 1

    if not game_over:
        dibuja_figuras()
    else:
        if revisar_ganador(1):
            dibuja_figuras(GREEN)
            dibuja_lineas(GREEN)

        elif revisar_ganador(2):
            dibuja_figuras(RED)
            dibuja_lineas(RED)

        else:
            dibuja_figuras(GRAY)
            dibuja_lineas(GRAY)

    pygame.display.update()
