import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)
#GPIO.setup(23,GPIO.OUT)
GPIO.output(18,0)	
#GPIO.output(23,0)


