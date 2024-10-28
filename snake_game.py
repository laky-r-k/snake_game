import sys
from button_for_game import *
import time
import pygame
import random
import collisionchecker as collisionchecker
again=False    
def head(again):
    pygame.init()
    pygame.mixer.init()
    win=pygame.display.set_mode((500,600))
    pygame.display.set_caption("snake game")
    white=(250,250,250)
    image=pygame.image.load("snake.png")
    image_2=pygame.image.load("egg.png")
    snake_p=pygame.transform.scale(image,(15,15))
    egg=pygame.transform.scale(image_2,(15,15))
    #color
    black=[0,0,0]
    skin=[230,200,100]
    #sounds
    failing=pygame.mixer.Sound("failing.wav")
    end_s=pygame.mixer.Sound("sforscor.wav")
    #button
    start=button("start",black,skin,30,50,[200,320])
    exit=button("exit",black,[200,200,200],30,50,[260,320])
    retry=button("retry",black,skin,30,50,[180,320])
    
    
    pos=[230,380]
    snake=[[230,380],[245,380],[260,380]]
    direction="left"
    change_to=direction
    egg_cor=[]

    def starting():
        run=True
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if start.is_button_pressed(pos):
                        run=False
            win.fill([250,250,250])
            start.create_button(win)
            pygame.display.update()
    def end(score):
        run=True
        time.sleep(1)
        end_s.play()
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if exit.is_button_pressed(pos):
                        run=False
                        sys.exit()
                    elif retry.is_button_pressed(pos):
                        again=True
                        head(again)
    
            win.fill([250,250,250])
            font_o=pygame.font.SysFont("BOLD",50)
            surface=pygame.font.Font.render(font_o,"Score :"+str(score),True,[0,0,0])     
            win.blit(surface,(180,280))
            exit.create_button(win)
            retry.create_button(win)
            pygame.display.update()
            
    def display_egg():
        if len(egg_cor)==0:
            egg_x=random.randint(10,440)
            egg_y=random.randint(10,580)
            egg_cor.append(pygame.Rect(egg_x,egg_y,15,15))
            win.blit(egg,egg_cor[0])
        else:
            win.blit(egg,egg_cor[0])
        
    def show_score(font,size,color,score):
        font_o=pygame.font.SysFont(font,size)
        surface=pygame.font.Font.render(font_o,"Score :"+str(score),True,color)
        win.blit(surface,(0,0))
    def display_snake():
        for body in snake:
            win.blit(snake_p,body)
    def main(change_to,direction):
        if again==False:
            starting()
        run=True
        score=0
        clock=pygame.time.Clock()
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    sys.exit()
                pressed=pygame.key.get_pressed()
                if pressed[pygame.K_UP]:
                    change_to="up"
                if pressed[pygame.K_DOWN]:
                    change_to="down"
                if pressed[pygame.K_LEFT]:
                    change_to="left"
                if pressed[pygame.K_RIGHT]:
                    change_to="right"
            if change_to!=direction:
                if change_to=="up"and direction=="right":
                    pos[1]-=15
                    direction="up"
                elif change_to=="up" and direction=="left":
                    pos[1]-=15
                    direction="up"
                elif change_to=="down" and direction=="right":
                    pos[1]+=15
                    direction="down"
                elif change_to=="down" and direction=="left":
                    pos[1]+=15
                    direction="down" 
                elif change_to=="left" and direction=="up":
                    pos[0]-=15
                    direction="left"
                elif change_to=="left" and direction=="down":
                    pos[0]-=15
                    direction="left"
                elif change_to=="right" and direction=="up":
                    pos[0]+=15
                    direction="right"
                elif change_to=="right" and direction=="down":      
                    pos[0]+=15
                    direction="right"
                else:
                    run=False
            else:
                if direction=="left":
                    pos[0]-=15
                elif direction=="right":
                    pos[0]+=15
                elif direction=="up":
                    pos[1]-=15
                elif direction=="down":
                    pos[1]+=15
            if pos[0]<=0 or pos[1]<0  or pos[0]>=500 or pos[1]>=600:#seting boundry for the snake to move
                run=False
                failing.play()
                time.sleep(2)
            snake.insert(0,[pos[0],pos[1]])
            if collisionchecker.collision(pos,egg_cor,15,15):
                egg_cor.pop()
                score+=10 
            else:
                snake.pop()
            
            if collisionchecker.collide(pos,snake,15,15):
                time.sleep(1)
                failing.play()
                run=False
                
            win.fill(white)
            display_egg()
            display_snake()
            show_score("BOLd",30,[0,0,0],score)
            pygame.display.update()
            clock.tick(10)
        end(score)    
    main(change_to,direction)
    pygame.quit()
                
head(again)   














































































































































