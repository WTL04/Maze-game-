import pygame, sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
mainClock = pygame.time.Clock()
from pygame.locals import *



class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):

			#[0] = left mouse button, [1] = middle mouse button, [2] = right mouse button
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True

			
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return self.clicked

#text maker
def draw_text(text, font, text_color, x, y):
	img = font.render(text, True, text_color)
	screen.blit(img, (x,y))

#checks if mouse on path
def is_over(rect, pos):

	if rect.collidepoint(pos[0], pos[1]):
		return True
	else:
		return False

def start_screen():

	running = True

	while running:

		screen.fill('grey')
		pygame.display.set_caption('Start Screen')

		font = pygame.font.SysFont('Times New Roman', 60)
		draw_text("Welcome to the Maze", font, 'black', 145, 600)
					
		#create the start button
		startImg = pygame.image.load("start.png")
		startButton = Button(350, 700, startImg, 0.2)
		startButton.draw(screen)


		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == MOUSEBUTTONDOWN:
				if startButton.draw(screen):
					print('play sound here')
					game_screen()

					


		pygame.display.update()
		mainClock.tick(60)


def game_screen():

	running = True

	while running:
		pygame.display.set_caption('Game') 
		screen.fill('black')

		starting_rect = pygame.draw.rect(screen, 'red', pygame.Rect(350, 720, 100, 60) )
		path1 = pygame.draw.rect(screen, 'red', pygame.Rect(385, 624, 30, 100) )
		path2 = pygame.draw.rect(screen, 'red', pygame.Rect(265, 624, 150, 30) )
		path3 = pygame.draw.rect(screen, 'red', pygame.Rect(265, 575, 30, 50) )
		path4 = pygame.draw.rect(screen, 'red', pygame.Rect(265, 575, 30, 50) )
		path5 = pygame.draw.rect(screen, 'red', pygame.Rect(265, 573, 200, 30) )
		path6 = pygame.draw.rect(screen, 'red', pygame.Rect(435, 533, 30, 50) )
		path7 = pygame.draw.rect(screen, 'red', pygame.Rect(180, 515, 285, 20) )
		path8 = pygame.draw.rect(screen, 'red', pygame.Rect(180, 470, 10, 50) )
		path9 = pygame.draw.rect(screen, 'red', pygame.Rect(80, 470, 100, 10) )
		path10 = pygame.draw.rect(screen, 'red', pygame.Rect(80, 430, 20, 50) )
		path11 = pygame.draw.rect(screen, 'red', pygame.Rect(80, 380, 300, 50) )
		path12 = pygame.draw.rect(screen, 'red', pygame.Rect(370, 312, 10, 100) )
		path13 = pygame.draw.rect(screen, 'red', pygame.Rect(370, 310, 50, 10) )
		path14 = pygame.draw.rect(screen, 'red', pygame.Rect(412, 220, 9, 100) )
		path15 = pygame.draw.rect(screen, 'red', pygame.Rect(412, 150, 5, 70) )
		path16 = pygame.draw.rect(screen, 'red', pygame.Rect(412, 100, 3, 70) )
		path17 = pygame.draw.rect(screen, 'red', pygame.Rect(412, 30, 2, 70) )
		ending_rect = pygame.draw.rect(screen, 'blue', pygame.Rect(400, 30, 30, 30) )

		#get mouse pos
		mousepos = pygame.mouse.get_pos()


		#checks if mouse is on path
		if is_over(starting_rect, mousepos) or is_over(path1, mousepos) or is_over(path2, mousepos) or is_over(path3, mousepos) or is_over(path4, mousepos) or is_over(path5, mousepos) or is_over(path6, mousepos) or is_over(path7, mousepos) or is_over(path8, mousepos) or is_over(path9, mousepos) or is_over(path10, mousepos) or is_over(path11, mousepos) or is_over(path12, mousepos) or is_over(path13, mousepos) or is_over(path14, mousepos) or is_over(path15, mousepos) or is_over(path16, mousepos) or is_over(path17, mousepos):
			pass
		else:
			game_over()



		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pause_menu()


		pygame.display.update()
		mainClock.tick()


def game_over():

	while True:
		#standard setup for new screen
		pygame.display.set_caption('You Lose!')
		screen.fill('black')

		#image background
		drake = pygame.image.load('drake.jpeg')
		drakeImg = pygame.transform.scale(drake, (800, 800))
		screen.blit(drakeImg, (0, 0))

		#sounds
		gameovermusic = pygame.mixer.Sound('Drake - Passionfruit-[AudioTrimmer.com].wav')
		pygame.mixer.Sound.play(gameovermusic) 

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pause_menu()

		pygame.display.update()
		mainClock.tick(60)



def pause_menu():
	running = True
	while running:

		pygame.display.set_caption('Pause')
		screen.fill('black')

		font = pygame.font.SysFont('Times New Roman', 70)
		draw_text('Paused', font, 'white', 300, 200)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					game_screen()

		pygame.display.update()
		mainClock.tick(60)

start_screen()
