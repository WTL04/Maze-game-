# Example file showing a basic pygame "game loop"
import pygame, sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
game = False


#text maker
def draw_text(text, font, text_color, x, y):
	img = font.render(text, True, text_color)
	screen.blit(img, (x,y))

def start_screen():
	screen.fill((105,105,105))

	startImg = pygame.image.load("C:\\Users\\William\\OneDrive\\Desktop\\pygames\\maze game\\start.png")
	smallstartImg = pygame.transform.scale(startImg, (200, 200))
	screen.blit(smallstartImg, (290, 600))

	font = pygame.font.SysFont('Times New Roman', 60)
	draw_text("Welcome to the Maze", font, 'black', 145, 500)


def pause_menu():
	pass


def game_screen():

	screen.fill('black')



#on and off button for game
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE

    if event.type == pygame.KEYDOWN:
    	game = True



    #determines if game starts
    if game == False:
    	start_screen()
    elif game == True:
    	game_screen()


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()