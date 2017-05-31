from gpiozero import Button, TrafficLights, Buzzer, LED
from time import sleep


button = Button(21)
lights = TrafficLights(25,8,7)
gyZold = LED(26)
gyPiros = LED(19)

buzzer = Buzzer(15)

while True:
    #button.wait_for_press()
    gyPiros.on()
    lights.green.on()
    sleep(5)   
    lights.green.off()    
    lights.amber.on()
    
    sleep(3)
    lights.amber.off()
    lights.red.on()
    gyPiros.off()
    gyZold.on()
    sleep(3)
    gyZold.blink(0.1,0.1)
    sleep(2)
    gyZold.off()
    gyPiros.on()
    lights.amber.on()
    sleep(3)
    lights.off()
    #lights.green.on()
    


    
    #lights.off()
    #sleep(1)



    
    
    
