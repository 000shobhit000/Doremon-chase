import pygame
import sys
import pygame.locals
import random

pygame.init()

clock = pygame.time.Clock()

win_width = 1000
win_height = 494
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("doremon chase")
font = pygame.font.SysFont(None, 60)

# music
music = pygame.mixer.music.load("mortal kombat.mp3")
pygame.mixer.music.play(-1)


# global variables
player_x = 200
player_y = 280
walkcount = 0
back_x = 0
back_y = 0
vel = 10
distance = 0
lvl = 1
mouse_x = random.randint(600, 900)
mouse_y = player_y + 20
n_mouse_x = 600
jumpcount = 10
jump = True
score = 0



fps = 30
game_over = False
exit_game = False
# background
bg1 = pygame.image.load("bg1.jpg").convert()
bg2 = pygame.image.load("bg2.jpg").convert()
bg3 = pygame.image.load("bg3.jpg").convert()
bg4 = pygame.image.load("bg4.jpg").convert()


# player
do1 = pygame.image.load("do1.png")
do2 = pygame.image.load("do2.png")
do3 = pygame.image.load("do3.png")
do4 = pygame.image.load("do4.png")
do5 = pygame.image.load("do5.png")
do6 = pygame.image.load("do6.png")

# mouse
mo1 = pygame.image.load("mouse1.png")
mo2 = pygame.image.load("mouse2.png")
mo3 = pygame.image.load("mouse3.png")
mo4 = pygame.image.load("mouse4.png")


# walking
walk_list = [do1, do2, do3, do4, do5, do6]


# functions
def show_text(text, color, x, y):
    screen = font.render(text, True, color)
    win.blit(screen, (x, y))

def enemy():
    win.blit(mo1, (mouse_x, mouse_y))


    n = 1
    while n < 100:
        if n % 2 == 0:
            win.blit(mo2, (mouse_x + n*(n_mouse_x), mouse_y))
        else:
            win.blit(mo3, (mouse_x + n*(n_mouse_x), mouse_y))
        n += 1
        


# mouse_pos_list = [((random.randint(mouse_x + (i-1)*(n_mouse_x), mouse_x + i*(n_mouse_x)), mouse_y)) for i in range(1,21)]

# if i have made screen with just bg1 with like x value by not repeating the third bg1 in a loop 
# this method probably would work well.....
# i will try this in my next programm




# mian event loop --------------------------------------------------- 

while not exit_game:

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    if game_over == True:
        win.fill((200, 200, 255))
        show_text("game over", (0, 200, 200), 100, 100)
        show_text("better play next time", (0, 100, 200), 100, 200)


    elif game_over == False:

        keys = pygame.key.get_pressed()

        # player jumping
        if not jump:
            if keys[pygame.K_SPACE]:
                jump = True

        else:        
            if jumpcount >= -10:
                neg = 1
                if jumpcount <= 0:
                    neg = -1
                player_y -= (jumpcount ** 2) * 0.5 * neg
                jumpcount -= 1
            else:
                jump = False
                jumpcount = 10


        # mouse moving
        mouse_x -= vel

        
        


        # background blitting
        win.blit(bg1, (back_x, back_y))
        win.blit(bg1, (back_x + win_width, back_y))

        back_x -= vel
        if distance < 3*lvl:
            if back_x + win_width == 0:
                back_x = back_x + win_width
                distance += 1

        if distance >= 3*lvl and distance < 6*lvl:
            win.blit(bg2, (back_x, back_y))
            win.blit(bg2, (back_x + (win_width), back_y))
            if back_x + win_width == 0:
                back_x = back_x + win_width
                distance += 1

        if distance >= 6*lvl and distance < 9*lvl:
            win.blit(bg3, (back_x, back_y))
            win.blit(bg3, (back_x + (win_width), back_y))
            if back_x + win_width == 0:
                back_x = back_x + win_width
                distance += 1

        if distance >= 9*lvl:
            win.blit(bg4, (back_x, back_y))
            win.blit(bg4, (back_x + (win_width), back_y))
            if back_x + win_width == 0:
                back_x = back_x + win_width
                distance += 1

        if distance >= 12*lvl:
            distance = 0
            fps += 10

        # mouse blitting
        
        enemy()
        
            


        # player blitting
        win.blit(walk_list[int(walkcount)], (int(player_x), int(player_y)))
        walkcount += 0.5
        if walkcount > 5:
            walkcount = 0
            score += 1

        if abs((player_x + 30) - mouse_x) < 20 and abs(player_y - mouse_y) < 25:
            game_over = True
            
        
        n = 1
        while n < 100:
            n += 1
            if (abs((player_x + 30) - (mouse_x + n*(n_mouse_x))) < 20 and abs(player_y - mouse_y) < 25) or (abs((player_x + 30) - (mouse_x + n*(n_mouse_x))) < 20 and abs((player_y + 90) - mouse_y) < 25):
                game_over = True

        show_text(("score : " + str(score)), (200, 0, 0), 0, 0)

    


    pygame.display.update()
    clock.tick(fps)
    