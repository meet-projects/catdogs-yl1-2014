import pygame
import sys

if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600, 600))
	main_screen.fill((255, 255, 255))
	button_rec = pygame.Rect(0 , 0 , 100 ,100)
	button_sq = pygame.Surface([100, 100])
	main_screen.blit(button_sq, button_rec)
	buttonimg = pygame.image.load('CatDog.JPG')
	main_screen.blit(buttonimg, button_rec)
	while True :
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT: 
			sys.exit()
		if ev.type ==pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			if button_rec.collidepoint(x,y) :
				print ev.pos
		pygame.display.flip()
				