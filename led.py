from gpiozero import LED
from time import sleep

led = LED(17)



led.blink(0.2,0.2)
sleep(10)
