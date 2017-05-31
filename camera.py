import os
import pygame, sys
from gpiozero import Button, LED
from time import sleep

from pygame.locals import *
import pygame.camera

led = LED(17)
button = Button(2)
width = 640
height = 480

#initialise pygame   
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(width,height))
cam.start()

#setup window
#windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
#pygame.display.set_caption('Camera')

#take a picture
a = 1
nev="Pictures/"+str(a)+"kep.jpg"
while (a<=10):
    print('Az',a,'. Kép készítéséhez nyomd meg a gombot"')
    button.wait_for_press()
    button.when_pressed = led.on
    button.when_released = led.off
    print('fotoo')
    sleep(1)
    image = cam.get_image()
    nev="Pictures/"+str(a)+"kep.jpg"
    pygame.image.save(image,nev)
    a = a+1
    
cam.stop()

#display the picture
#catSurfaceObj = image
#windowSurfaceObj.blit(catSurfaceObj,(0,0))
#pygame.display.update()

#save picture
#pygame.image.save(image,'Pictures/picture.jpg')
   
print('---vége---')
