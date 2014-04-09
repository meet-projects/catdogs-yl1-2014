
import pygame
import sys

class Button(object):
    def __init__(self, x, y, w, h,color):
        self.button_rec = pygame.Rect(x, y, w, h)
        self.button_sq = pygame.Surface([w, h]) 
        self.button_sq.fill(color)
        self.color = color   
    def draw_button(self, main_screen):
        main_screen.blit(self.button_sq, self.button_rec)
    
    
class Label(object):
    def __init__(self,x,y,w,h,text,color,size):
        self.label_rec = pygame.Rect(x, y, w, h)
        self.text = str(text)
        self.color = color
        self.size = size
    def draw_label(self, main_screen):
        orderlabel= pygame.font.Font("cafbrewery.ttf", self.size)
        label = orderlabel.render(self.text, 1, self.color)
        main_screen.blit(label, self.label_rec)

def clear_window(main_screen):
    button_rec = pygame.Rect(0, 0, 900, 900)
    button_sq = pygame.Surface([900, 900])  
    main_screen.blit(button_sq, button_rec)
def gender(main_screen):
    main_screen.fill((255,255,255))
    label2 = Label(20,20,400,100, "Gender:", (0,0,0), 100)
    label2.draw_label(main_screen)
    global button3
    button3 = Button(100, 300, 300, 300 ,(255,0,127))
    button3.draw_button(main_screen)
    buttoning = pygame.image.load('male.JPG')
    main_screen.blit(buttoning,button3.button_rec)
    global button4
    button4 = Button(450, 300,300,300, (255,0,127)) 
    #button4 = Button(450, 300,300,300, (255,0,127)) 
    button4.draw_button(main_screen)
    buttoning = pygame.image.load('female.JPG')
    main_screen.blit(buttoning,button4.button_rec)
    global back
    back = Button(10, 850,150, 200, (255,0,127))
    back.draw_button(main_screen)

def age(main_screen):
    main_screen.fill((255,255,255))
    label2 = Label(20,20,400,100, "Age:", (255,0,127), 100)
    label2.draw_label(main_screen)  
    global button5
    button5 = Button(140,150,200,100 ,(255,0,127))
    button5.draw_button(main_screen)
    global button6
    button6 = Button(140,370,200,100 ,(255,0,127))
    button6.draw_button(main_screen)
    global button7
    button7 = Button(390,540,200,100 ,(255,0,127))
    button7.draw_button(main_screen)
    global button8
    button8 = Button(600,370,200,100 ,(255,0,127))
    button8.draw_button(main_screen)
    global button9
    button9 = Button(600,150,200,100 ,(255,0,127))
    button9.draw_button(main_screen)


def result(main_screen):
    main_screen.fill((255,255,255))
    global button10
    button10 = Button(200,200,500,500 ,(255,0,127))
    button10.draw_button(main_screen)

def breed(main_screen):
    main_screen.fill((255,255,255))
    global button1
    button1 = Button(50, 200, 375, 245 ,(255,0,127))
    button1.draw_button(main_screen)
    buttoning = pygame.image.load('CatDogB.jpg')
    main_screen.blit(buttoning,button1.button_rec)
    global button2
    button2 = Button(475,200,375,245, (255,0,127))
    button2.draw_button(main_screen)
    buttoning = pygame.image.load('CatDogAjpg.jpg')
    main_screen.blit(buttoning,button2.button_rec)
    global label1
    label1 = Label(20,20, 400, 100, "Pick Your Breed:", (0,0,0), 100)
    label1.draw_label(main_screen)
 


if __name__=="__main__":
    pygame.init()   
    screen = "breed"
    main_screen = pygame.display.set_mode((900,900))
    breed(main_screen)
    
    while True: 
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT: 
                    sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                x, y = ev.pos
                if screen=="breed":
                    if button1.button_rec.collidepoint(x, y) or button2.button_rec.collidepoint(x, y):
                        clear_window(main_screen)    
                        gender(main_screen)
                        screen = "gender"
                elif screen=="gender":
                    if button1.button_rec.collidepoint(x, y) or button2.button_rec.collidepoint(x, y):
                        clear_window(main_screen)
                        age(main_screen)
                        screen ="age"
                    if back.button_rec.collidepoint(x, y):
                        clear_window(main_screen)
                        breed(main_screen)
                        screen = "breed"
                elif screen=="age":
                    if button5.button_rec.collidepoint(x, y) or button6.button_rec.collidepoint(x, y) or button7.button_rec.collidepoint(x, y) or button8.button_rec.collidepoint(x, y) or button9.button_rec.collidepoint(x, y) or button9.button_rec.collidepoint(x, y):
                        clear_window(main_screen)
                        result(main_screen)
                        screen ="result"
                elif screen=="result":
                    print "result"
                        

            pygame.display.flip()
        
