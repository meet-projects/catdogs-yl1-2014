import pygame
import sys

class Button(object):
	def __init__(self, x, y, w, h):
		self.button_rec = pygame.Rect(x, y, w, h)
		self.button_sq = pygame.Surface([w, h])		 
	def draw_button(self):
		main_screen.blit(self.button_sq, self.button_rec)
	
	
class Label(object):
	def __init__(self,x,y,w,h):
		label_rec = pygame.Rect(x, y, w, h)


if __name__=="__main__":
	pygame.init()	
	main_screen = pygame.display.set_mode((900,900))
	main_screen.fill((39,87,192))
	
	button1 = Button(100, 300, 300, 300)
	button2 = Button(450, 300,300,300)
	button1.draw_button()
	button2.draw_button()


	while True: 
        	ev = pygame.event.poll()
        	if ev.type == pygame.QUIT: 
            		sys.exit()
       		if ev.type == pygame.MOUSEBUTTONDOWN:
            		x, y = ev.pos
            		
       		pygame.display.flip()
