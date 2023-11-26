import pygame
import sys
import time
WH=(255,255,255)
BC=(0,0,0)
RD=(255,0,0)
sus=pygame.display.set_mode((500,400))
pygame.init();pygame.display.set_caption('ne zmeika');go=False;x1=300;y1=300;x1ch=0;y1ch=0;clc=pygame.time.Clock();
while not go:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            go=True;
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                x1ch=0
                y1ch=+10
            elif event.key==pygame.K_UP:
                x1ch=0
                y1ch=-10
            elif event.key==pygame.K_LEFT:
                x1ch=-10
                y1ch=0
            elif event.key==pygame.K_RIGHT:
                x1ch=+10
                y1ch=0
    x1+=x1ch
    y1+=y1ch
    sus.fill(WH)
    pygame.draw.rect(sus,BC,[x1,y1,10,10])
    pygame.display.update()
    clc.tick(5)
pygame.quit();quit()
   
