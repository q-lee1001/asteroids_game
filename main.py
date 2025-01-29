import pygame, constants, player, asteroidfield, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

	pygame.init()
	print("""Starting asteroids!
Screen width: 1280
Screen height: 720""")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	x= SCREEN_WIDTH/2
	y= SCREEN_HEIGHT/2
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()


	Player.containers = (updatable, drawable)
	player = Player(x, y,)
	
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	asteroid_field = AsteroidField()
	Shot.containers = (shots, updatable, drawable)
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		for sprite in drawable:
			sprite.draw(screen)

		#update step	
		updatable.update(dt)


		for obj in asteroids:
			if player.coll_check(obj):
				print("Game over!")
				sys.exit()

		for obj in asteroids:
			for shot in shots:
				if obj.coll_check(shot):
					obj.split()
					shot.kill()

		pygame.display.flip()
		
		dt = clock.tick(60)/1000


if __name__ == "__main__":
	main()
