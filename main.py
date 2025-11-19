import pygame, sys, random, os
from button import Button
from pygame.locals import *

class Krab(object):  
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load("assets/mrkrab.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        # krab position
        self.x = 500
        self.y = 600

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 10 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

class Mulla:
    def __init__(self, speed, x, y):
        self.image = pygame.image.load("assets/money.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.speed = speed
        self.x = x
        self.y = y

pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Money Catcher")

BG = pygame.image.load("assets/krustyKrab.png")
BG = pygame.transform.smoothscale(BG, WIN.get_size())

MONEY_SPEED = 5

def get_font(size): # Returns Press-Start-2P in the desired size
    try:
        return pygame.font.Font("assets/cartoon.ttf", size)
    except FileNotFoundError:
        print("Error: font.ttf file not found in 'assets' directory. Using default font.")
        return pygame.font.SysFont(None, size)

def play():
    WIN.blit(BG, (0,0))

    krab = Krab()
    money = Mulla(MONEY_SPEED, random.randrange(30, WIDTH - 30), -600) 

    clock = pygame.time.Clock()

    score = 0

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BACK = Button(image=None, pos=(500, 750), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(WIN)
        
        WIN.blit(BG, (0,0))
        WIN.blit(money.image, (money.x, money.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main()
        
        krab.handle_keys()
        krab.draw(WIN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(WIN)
        
        money.y += money.speed

        if abs(krab.x - money.x) < 50 and abs(krab.y - money.y) < 50:
            money.y = -10
            money.x = random.randrange(50, WIDTH - 50)
            score += 1

        scoretext = get_font(30).render("{0} CENTS".format(score), 1, (0,0,0))
        WIN.blit(scoretext, (5, 10))
        pygame.display.update()

        clock.tick(60)
    
    
def main():
    run = True

    while run:
        WIN.blit(BG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Main Menu", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(500, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        WIN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

        pygame.display.update()

    pygame.quit()
 
if __name__ == "__main__":
    main()