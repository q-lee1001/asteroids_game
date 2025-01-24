import pygame, constants
from constants import *
def main():

	pygame.init()
	print("""Starting asteroids!
Screen width: 1280
Screen height: 720""")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		pygame.display.flip()


if __name__ == "__main__":
	main()
