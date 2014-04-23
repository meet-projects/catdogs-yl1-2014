
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
    button3 = Button(100, 200, 224, 315 ,(255,0,127))
    button3.draw_button(main_screen)
    buttoning = pygame.image.load('male.jpg')
    main_screen.blit(buttoning,button3.button_rec)
    global button4
    button4 = Button(550, 200,225,315, (255,0,127)) 
    #button4 = Button(450, 300,300,300, (255,0,127)) 
    button4.draw_button(main_screen)
    buttoning = pygame.image.load('female.JPG')
    main_screen.blit(buttoning,button4.button_rec)
    global back
    back = Button(20, 850,150, 50, (255,0,127))
    back.draw_button(main_screen)
    buttoning = pygame.image.load('back.jpg')
    main_screen.blit(buttoning,back.button_rec)
def age(main_screen):
    main_screen.fill((255,255,255))
    label2 = Label(20,20,400,100, "Age:", (0,0,0), 100)
    label2.draw_label(main_screen)  
    global button5
    button5 = Button(140,150,200,100 ,(255,0,127))
    button5.draw_button(main_screen)
    buttoning = pygame.image.load('0-1.jpg')
    main_screen.blit(buttoning,button5.button_rec)
    global button6
    button6 = Button(140,370,200,100 ,(255,0,127))
    button6.draw_button(main_screen)
    buttoning = pygame.image.load('4-7.jpg')
    main_screen.blit(buttoning,button6.button_rec)
    global button7
    button7 = Button(380,540,200,100 ,(255,0,127))
    button7.draw_button(main_screen)
    buttoning = pygame.image.load('11+.jpg')
    main_screen.blit(buttoning,button7.button_rec)
    global button8
    button8 = Button(600,370,200,100 ,(255,0,127))
    button8.draw_button(main_screen)
    buttoning = pygame.image.load('7-11.jpg')
    main_screen.blit(buttoning,button8.button_rec)
    global button9
    button9 = Button(600,150,200,100 ,(255,0,127))
    button9.draw_button(main_screen)
    buttoning = pygame.image.load('1-4.jpg')
    main_screen.blit(buttoning,button9.button_rec)
    global back1
    back1 = Button(20, 850,150, 50, (255,0,127))
    back1.draw_button(main_screen)
    buttoning = pygame.image.load('back.jpg')
    main_screen.blit(buttoning,back1.button_rec)

def result(main_screen):
    main_screen.fill((255,255,255))
    global button10
    button10 = Button(200,200,500,307 ,(255,0,127))
    button10.draw_button(main_screen)
    buttoning = pygame.image.load(name + '-big.jpg')
    main_screen.blit(buttoning,button10.button_rec)
    global back3
    back3 = Button(20, 850,150, 50, (255,0,127))
    back3.draw_button(main_screen)
    buttoning = pygame.image.load('back.jpg')
    main_screen.blit(buttoning,back3.button_rec)
    global label_result1
    label_result1 = Label(30,20, 350, 100, name, (0,0,0), 60)
    label_result1.draw_label(main_screen)
    global label_result2
<<<<<<< HEAD
    label_result2 = Label(30,90, 350, 100, g , (0,0,0), 60)
    label_result2.draw_label(main_screen)
    global label_result3
    label_result3 = Label(30,140, 350, 100, a, (0,0,0), 60)
=======
    label_result2 = Label(35,80, 350, 100, g , (0,0,0), 60)
    label_result2.draw_label(main_screen)
    global label_result3
    label_result3 = Label(31,120, 350, 100, a, (0,0,0), 60)
>>>>>>> 1b12e716c9bd50caf08c8d31a582d7e60f500abb
    label_result3.draw_label(main_screen)
def breed(main_screen):
    main_screen.fill((255,255,255))
    global button1
    button1 = Button(50, 200, 375, 245 ,(255,0,127))
    button1.draw_button(main_screen)
    buttoning = pygame.image.load('Golden-Manx.jpg')
    main_screen.blit(buttoning,button1.button_rec)
    global button2
    button2 = Button(475,200,375,245, (255,0,127))
    button2.draw_button(main_screen)
    buttoning = pygame.image.load('Persian-Terrier.jpg')
    main_screen.blit(buttoning,button2.button_rec)
    global label1
    label1 = Label(20,20, 400, 100, "Pick Your Breed:", (0,0,0), 100)
    label1.draw_label(main_screen)
 


if __name__=="__main__":
    pygame.init()    
    screen = "breed"
    main_screen = pygame.display.set_mode((900,900))
    breed(main_screen)
    name = ""
    g = ""
    a = ""
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
                        if button1.button_rec.collidepoint(x, y):
                            name = "Golden-Manx"
                        elif button2.button_rec.collidepoint(x,y):
                            name = "Persian-Terrier"
                elif screen=="gender":
                    if button3.button_rec.collidepoint(x, y) or button4.button_rec.collidepoint(x, y):
                        clear_window(main_screen)
                        age(main_screen)
                        screen ="age"
                        if button3.button_rec.collidepoint(x, y):
                            g = "Male"
                        elif button4.button_rec.collidepoint(x,y):
                            g = "Female"
                    elif back.button_rec.collidepoint(x, y):
                        clear_window(main_screen)
                        breed(main_screen)
                        screen = "breed"
                elif screen=="age":
                    if button5.button_rec.collidepoint(x, y) or button6.button_rec.collidepoint(x, y) or button7.button_rec.collidepoint(x, y) or button8.button_rec.collidepoint(x, y) or button9.button_rec.collidepoint(x, y) or button9.button_rec.collidepoint(x, y):
                        
                        if button5.button_rec.collidepoint(x, y):
                            a = "0-1"
                        elif button6.button_rec.collidepoint(x,y):
                            a = "4-7"
                        elif button7.button_rec.collidepoint(x, y):
                            a = "11+"
                        elif button8.button_rec.collidepoint(x,y):
                            a = "7-11"
                        elif button9.button_rec.collidepoint(x, y):
                            a = "1-4"

                        clear_window(main_screen)
                        result(main_screen) 
                        screen ="result"
                    elif back1.button_rec.collidepoint(x, y):
                            clear_window(main_screen)
                            gender(main_screen)
                            screen = "gender"
                elif screen=="result":
                        if back3.button_rec.collidepoint(x, y):
                            clear_window(main_screen)
                            age(main_screen)
                            screen = "age"

            pygame.display.flip()
        
