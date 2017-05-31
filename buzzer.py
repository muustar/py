from gpiozero import Buzzer
from time import sleep

bz = Buzzer(23)
while True:
    bz.on()
    sleep(0.2)
    bz.off()
    sleep(0.2)
