import pygame
from pygame.locals import *
import time
import BG.Logic as Logic

pygame.init()
Screenheight=640
Screenwidth=480
screen=pygame.display.set_mode((Screenheight,Screenwidth))
clock = pygame.time.Clock()

Button_Rect=pygame.Rect(320-50,240-50,100,100)
Timer_button=pygame.Rect(320-100,240-50,200,100)

font=pygame.font.SysFont("Cooper Black",72)
fontus=pygame.font.SysFont("Algerian",100)
value_text = fontus. render ("BRAIN GAME", True, "RED")
text_rect = value_text.get_rect(center=(320, 190) )
screen.blit(value_text, text_rect)
pygame.display.flip()

fontus=pygame.font.SysFont("Arial",20)
value_text = fontus. render ("--- Click Anywhere to Continue ---", True, "RED")
text_rect = value_text.get_rect(center=(320, 420) )
screen.blit(value_text, text_rect)
pygame.display.flip()


def main():
    click=True
    total_time=0
    while True:
        
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click==True:
                screen.fill((222,142,14))

                for i in range (110):                
                    font = pygame.font.SysFont('Algerian',int(72-i*0.25))
                    title= font. render ("BRAIN GAME", True, ("Black"))
                    title_pos = title.get_rect(center= (320, 180-i))
                    screen.blit(title, title_pos)
                    clock.tick(100)
                    pygame.display.update()
                    
                    screen.fill((222,142,14))
                else:
                    Heading()
                    pygame.display.update()
                    click=False
                    #Start Button
                    Start_button()
                    total_time=pygame.time.get_ticks()
                    print(total_time)
                    break

            if event.type== MOUSEBUTTONDOWN and event.button==1 and Timer_button.collidepoint(event.pos):
                screen.fill((222,142,14))
                Heading()
                fontus=pygame.font.SysFont("Cooper Black",72) #i= 99
                pygame.display.update()

                pygame.time.delay(250)

                value_text = fontus. render ("Get", True, (80, 12, 63))
                text_rect = value_text.get_rect(center=(320, 240) ) #i=99 (100, 5)
                screen.blit(value_text, text_rect)
                
                pygame.display.update()

                pygame.time.delay(1000)

                button1 = pygame.Rect(320-150, 240-30, 300, 60)  # create button 1                
                pygame.draw.rect(screen, (222,142,14), button1)# draw button 1

                pygame.display.update()

                pygame.time.delay(250)

                fontus=pygame.font.SysFont("Cooper Black",72) #i= 99
                value_text = fontus. render ("Set", True, (80, 12, 63))
                text_rect = value_text.get_rect(center=(320, 240) ) #i=99 (100, 5)
                screen.blit(value_text, text_rect)
                pygame.display.update()

                pygame.time.delay(1000)

                button1 = pygame.Rect(320-150, 240-30, 300, 60)  # create button 1                
                pygame.draw.rect(screen, (222,142,14), button1)# draw button 1

                pygame.display.update()

                pygame.time.delay(250)

                fontus=pygame.font.SysFont("Cooper Black",72) #i= 99
                value_text = fontus. render ("Go...", True, (80, 12, 63))
                text_rect = value_text.get_rect(center=(320, 240) ) #i=99 (100, 5)
                screen.blit(value_text, text_rect)
                pygame.display.update()

                pygame.time.delay(1000)

                button1 = pygame.Rect(320-150, 240-30, 300, 60)  # create button 1                
                pygame.draw.rect(screen, (222,142,14), button1)# draw button 1

                pygame.display.update()

                pygame.time.delay(250)
                timer()
                pygame.display.update()

                pygame.draw.rect(screen,(31, 97, 141),Button_Rect,3,5)
                pygame.display.update()               
                

                # pygame.display.flip()
                
                break
                 
            # print(total_time)   
            # pygame.time.delay(total_time)            
            # screen.fill((222,142,14))   
    
  
        pygame.display.flip()
    
def timer():
    for i in range(5):
        # Using draw.rect module of
        # pygame to draw the solid circle
        pygame.draw.circle(screen,(251, 200, 100),[160,240],50,0) #Inner Number Circle
        pygame.draw.circle(screen,"Black",[160,240],73,6)

        if(i==0): 
            # pygame.draw.arc(screen,"Red",(160-99,240-99,198,198),3.14/2,5*3.14/2,15)
            pygame.draw.arc(screen,"Red",(160-70,240-70,140,140),3.14/2,5*3.14/2,15)
            

            value_text = font. render (str(5), True, "Black")
            text_rect = value_text.get_rect(center= (160,240-10))

            screen.blit(value_text, text_rect)
            pygame.display.update()
            pygame.time.delay(750)

        # pygame.draw.circle(screen, "Gray",
        #                 [160, 240], 100, 15)
        pygame.draw.circle(screen, "Gray",
                        [160, 240], 70, 15)
        # pygame.draw.arc(screen,"Red",(160-100,240-100,200,200),3.14/2,5*3.14/2-2*3.14/5*(i+1),16)
        pygame.draw.arc(screen,"Red",(160-70,240-70,140,140),3.14/2,5*3.14/2-2*3.14/5*(i+1),16)

        pygame.draw.circle(screen,(251, 200, 100),[160,240],50,0)
        pygame.draw.circle(screen,("#A8E890"),[160,240],55,6)

        value_text = font. render (str(5-i-1), True, "Black")
        text_rect = value_text.get_rect(center= (160,240-10))

        screen.blit(value_text, text_rect)
        pygame.display.update()

        # Draws the surface object to the screen.
        pygame.draw.rect(screen,(31, 97, 141),Button_Rect,5,15)
        iButton_Rect=pygame.Rect(320-45,240-45,90,90)
        pygame.draw.rect(screen,(7, 247, 236),iButton_Rect,0,10)

        pygame.display.update()
        pygame.time.delay(100)  

        value_text = font. render (str(Logic.win_set[i]),  True, "Black")
        text_rect = value_text.get_rect(center= (320,240))
        screen.blit(value_text, text_rect)

        pygame.display.update()
        print(pygame.time.delay(900))

def Start_button():
    pygame.draw.ellipse(screen,"Red",Timer_button)
    pygame.draw.ellipse(screen,"Black",Timer_button,8)
    fontus=pygame.font.SysFont("Cooper Black",48)
    value_text = fontus. render ("Start", True, "Black")
    text_rect = value_text.get_rect(center= (320,240))
    screen.blit(value_text, text_rect)

def Heading():
    # fonti = pygame.font.SysFont('Algerian',72)
    # title = fonti.render("BRAIN GAME", True, (252,14,14))
    # screen.blit(title, (100, 5))

    fontus=pygame.font.SysFont("Cooper Black",int(72-99*0.25)+10) #i= 99
    value_text = fontus. render ("BRAIN GAME", True, (80, 12, 63))
    text_rect = value_text.get_rect(center=(320, 150-99) ) #i=99 (100, 5)
    screen.blit(value_text, text_rect)
main()