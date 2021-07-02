import pygame
import os
import sys
from pygame.locals import *
pygame.font.init()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

WIDTH, HEIGHT = 400, 460
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

OPENING_SCREEN = pygame.image.load((os.path.join('tic tac opening.png')))
O_IMAGE = pygame.image.load("O.png")
X_IMAGE = pygame.image.load("X.png")
O_IMAGE = pygame.transform.scale(O_IMAGE, (80,80))
X_IMAGE = pygame.transform.scale(X_IMAGE, (80,80))

WHITE = (255, 255, 255)
BLACK = (0,0,0)
FPS = 60
TTT = [[None]*3,[None]*3,[None]*3]
space_full = False


winner = False
draw = False


font = pygame.font.Font(None, 32)
textX = font.render("X's turn", True ,WHITE , BLACK)
textO = font.render("O's turn", True ,WHITE , BLACK)
textRectX = textX.get_rect()
textRectO = textO.get_rect()
textRectX.center = (200, 430)
textRectO.center = (200, 430)


def draw_window(xturn):
    WIN.fill(WHITE)
    WIN.fill(BLACK,Rect(0,400,400,60))
    pygame.display.update()
    pygame.draw.line(WIN, BLACK, (400 / 3, 0), (400 / 3, 400), 4)
    pygame.draw.line(WIN, BLACK, (400 / 3 * 2, 0), (400 / 3 * 2, 400), 4)
    pygame.draw.line(WIN, BLACK, (0, 400 / 3), (400, 400 / 3), 4)
    pygame.draw.line(WIN, BLACK, (0, 400 / 3 * 2), (400, 400 / 3 * 2), 4)
    pygame.display.flip()
    if xturn == False:
        WIN.blit(textX, textRectX)
    else:
        WIN.blit(textO, textRectO)
    pygame.display.update()

def userClick (xturn, pos):

    x,y = pos
    if x > 0 and x < 400 / 3:
        col = 0
    elif x > 400 / 3 and x < 2*400/3 :
        col = 1
    elif x > 2*400/3 and x < 400:
        col=2

    if y > 0 and y < 400 / 3:
        row = 0
    elif y > 400 / 3 and y < 2*400/3 :
        row = 1
    elif y > 2*400/3 and y < 400:
        row = 2

    if  TTT[row][col] == None :
        if xturn == False:
            TTT[row][col] = "X"
        else:
            TTT[row][col] = "O"
        return False

    else:
        return True



def draw_XO():
    for row in range(0,3):
        for col in range(0,3):
            if TTT[row][col]== "X":
                WIN.blit(X_IMAGE,(col*400/3+25,row*400/3+25))
            elif TTT[row][col] == "O":
                WIN.blit(O_IMAGE, (col * 400 / 3 + 25, row * 400 / 3 + 25))
    pygame.display.update()


def game_opening():
    WIN.blit(OPENING_SCREEN, (0, 0))
    pygame.display.update()
    pygame.time.wait(3000)


def reset_game():
    pygame.time.wait(3000)
    global TTT, winner, draw
    draw = False
    game_opening()
    winner = False
    TTT = [[None]*3,[None]*3,[None]*3]
    pygame.display.update()


def check_win():
    for row in range(0,3):
        row_win_x = True
        row_win_o = True
        for col in range(0,3):
            if not(TTT[row][col] == "X"):
                row_win_x = False
            if not(TTT[row][col] == "O"):
                row_win_o = False
        if row_win_x or row_win_o:
            pygame.draw.line(WIN, BLACK, (0, row*400/3+66), (400, row*400/3+66), 4)
            return True

    for col in range(0,3):
        col_win_x = True
        col_win_o = True
        for row in range(0,3):
            if not(TTT[row][col] == "X"):
                col_win_x = False
            if not(TTT[row][col] == "O"):
                col_win_o = False
        if col_win_x or col_win_o:
            pygame.draw.line(WIN, BLACK, (col*400/3+66, 0), (col*400/3+66, 400), 4)
            return True

    if TTT[0][0]=="X" and TTT[1][1]=="X" and TTT[2][2]=="X":
        pygame.draw.line(WIN, BLACK, (0, 0), (400, 400), 4)
        return True

    if TTT[0][0]=="O" and TTT[1][1]=="O" and TTT[2][2]=="O":
        pygame.draw.line(WIN, BLACK, (0, 0), (400, 400), 4)
        return True

    if TTT[0][2]=="O" and TTT[1][1]=="O" and TTT[2][0]=="O":
        pygame.draw.line(WIN, BLACK, (0, 400), (400, 0), 4)
        return True

    if TTT[0][2]=="X" and TTT[1][1]=="X" and TTT[2][0]=="X":
        pygame.draw.line(WIN, BLACK, (0, 400), (400, 0), 4)
        return True

    pygame.display.flip()
    pygame.display.update()
    return False


def check_draw():
    board_full = True
    for row in range(0, 3):
        for col in range(0, 3):
            if TTT[row][col] == None:
                board_full = False
    if board_full == True :
        return True
    return False

def main():
    xturn = False
    clock = pygame.time.Clock()
    pygame.display.set_caption("First game!")
    game_opening()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == MOUSEBUTTONDOWN:
                # the user clicked; place an X or O
                space_full=userClick(xturn , pygame.mouse.get_pos())
                if xturn and space_full==False:
                    xturn = False
                else:
                    xturn = True
                
            draw_window(xturn)
            draw_XO()

            if check_win() or check_draw():
                pygame.display.flip()
                pygame.display.update()
                xturn = False
                reset_game()
    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
