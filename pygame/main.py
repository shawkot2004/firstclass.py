import pygame as pg 
pg.init()
info = pg.display.Info()

#Display
width, height = 600, 600
screen = pg.display.set_mode((width, height), pg.RESIZABLE)
screen.fill("red")
pg.display.set_caption("Tic Tac Toe!!")

#Board base
base = pg.Surface((600, 600))
base.fill("red")

pg.draw.line(base, "black", (200, 0), (200, 600), 10)
pg.draw.line(base, "black", (400, 0), (400, 600), 10)
pg.draw.line(base, "black", (0, 200), (600, 200), 10)
pg.draw.line(base, "black", (0, 400), (600, 400), 10)

#Sounds
bg_sound = pg.mixer.Sound("pygame/assets/bg.mp3")
bg_sound.set_volume(2)
click = pg.mixer.Sound("pygame/assets/click.mp3")
click.set_volume(2)
winner = pg.mixer.Sound("pygame/assets/winner.mp3")
bg_sound.play()

#Fonts and texts
text_font = pg.font.Font("pygame/assets/Roboto-Regular.ttf", 50)
restart_font = pg.font.Font("pygame/assets/Roboto-Regular.ttf", 30)

x_winner = text_font.render("X wins", True, "Blue")
o_winner = text_font.render("O wins", True, "Blue")

gameover_message = restart_font.render("CLICK ANYWHERE TO RESTART", False, "white")
gameover_message_rect = gameover_message.get_rect(center = (300, 500))

draw_message = text_font.render("Match DRAWN!", False, "white")
draw_message_rect = draw_message.get_rect(center = (300, 150))

#Images
x_img = pg.image.load("pygame/assets/X.png").convert_alpha()
x_img = pg.transform.smoothscale(x_img, (150, 150))

o_img = pg.image.load("pygame/assets/O.png").convert_alpha()
o_img = pg.transform.smoothscale(o_img, (150, 150))

#Functions
def addXO(pos_x, pos_y, move):
    if move == 1:
        img = x_img
    else:
        img = o_img

    if 0<=pos_x<=200:
        if 0<=pos_y<=200: width, height = 100, 100
        elif 201<=pos_y<=400: width, height = 100, 300
        elif 401<=pos_y<=600: width, height = 100, 500
    
    elif 201<=pos_x<=400:
        if 0<=pos_y<=200: width, height = 300, 100
        elif 201<=pos_y<=400: width, height = 300, 300
        elif 401<=pos_y<=600: width, height = 300, 500
    
    elif 401<=pos_x<=600:
        if 0<=pos_y<=200: width, height = 500, 100
        elif 201<=pos_y<=400: width, height = 500, 300
        elif 401<=pos_y<=600: width, height = 500, 500

    img_rect = img.get_rect(center = (width, height))
    base.blit(img, img_rect)

def update_board(board, pos_x, pos_y, move):
    if 0<=pos_x<=200:
        if 0<=pos_y<=200: x, y = 0, 0
        elif 201<=pos_y<=400: x, y = 1, 0
        elif 401<=pos_y<=600: x, y = 2, 0
    
    elif 201<=pos_x<=400:
        if 0<=pos_y<=200: x, y = 0, 1
        elif 201<=pos_y<=400: x, y = 1, 1
        elif 401<=pos_y<=600: x, y = 2, 1

    elif 401<=pos_x<=600:
        if 0<=pos_y<=200: x, y = 0, 2
        elif 201<=pos_y<=400: x, y = 1, 2
        elif 401<=pos_y<=600: x, y = 2, 2
    else:
        return

    if board[x][y] == None:
        board[x][y] = move
        addXO(pos_x, pos_y, move)
        return True

def isFilled(board):
    for i in board:
        for j in i:
            if j == None:
                return False    
    return True
        
def checkWinner(b):
    if b[0][0] == b[0][1] == b[0][2] != None:
        pg.draw.line(base, "red", (50, 100), (550, 100), 30)
        return True
    if b[1][0] == b[1][1] == b[1][2] != None:
        pg.draw.line(base, "red", (50, 300), (550, 300), 30)
        return True
    if b[2][0] == b[2][1] == b[2][2] != None:
        pg.draw.line(base, "red", (50, 500), (550, 500), 30)
        return True
    if b[0][0] == b[1][0] == b[2][0] != None:
        pg.draw.line(base, "red", (100, 50), (100, 550), 30)
        return True
    if b[0][1] == b[1][1] == b[2][1] != None:
        pg.draw.line(base, "red", (300, 50), (300, 550), 30)
        return True
    if b[0][2] == b[1][2] == b[2][2] != None:
        pg.draw.line(base, "red", (500, 50), (500, 550), 30)
        return True
    if b[0][0] == b[1][1] == b[2][2] != None:
        pg.draw.line(base, "red", (50, 50), (550, 550), 30)
        return True
    if b[0][2] == b[1][1] == b[2][0] != None:
        pg.draw.line(base, "red", (550, 50), (50, 550), 30)
        return True

def reset():
    global board, move, gameover
    for i in range(3):
        for j in range(3):
            board[i][j] = None
    
    move = 0
    gameover = False
    return True
    
def outro(move, x, o):
    x_rect = x.get_rect(center = (300, 150))
    o_rect = o.get_rect(center = (300, 150))
    if move == 1:
        base.blit(x, x_rect)
    else:
        base.blit(o, o_rect)


#Main Loop
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

running = True
move = 1
restart = False
while running:
    base_rect = base.get_rect(center = (width//2, height//2))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pg.display.set_mode((width, height), pg.RESIZABLE)

        if event.type == pg.MOUSEBUTTONDOWN:
            click.play()
            if restart:
                screen = pg.display.set_mode((width, height), pg.RESIZABLE)
                base.fill("yellow")
                pg.draw.line(base, "black", (200, 0), (200, 600), 10)
                pg.draw.line(base, "black", (400, 0), (400, 600), 10)
                pg.draw.line(base, "black", (0, 200), (600, 200), 10)
                pg.draw.line(base, "black", (0, 400), (600, 400), 10)
                restart = False
            else:
                pos = pg.mouse.get_pos()
                x = pos[0] - base_rect.left
                y = pos[1] - base_rect.top
                updated = update_board(board, x, y, move)
                gameover = checkWinner(board)

                if updated:
                    if gameover:
                        outro(move, x_winner, o_winner)
                        winner.play()
                        base.blit(gameover_message, gameover_message_rect)
                        restart = reset()
                    
                    elif isFilled(board):
                        base.blit(draw_message, draw_message_rect)
                        winner.play()
                        base.blit(gameover_message, gameover_message_rect)
                        restart = reset()
                    
                    if move == 1: move = 0
                    else: move = 1

    screen.fill("red")
    screen.blit(base, base_rect)
    pg.display.update()

