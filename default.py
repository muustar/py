import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print("A pi GPIO port alapra allitasa. GPIO.cleanup()")
GPIO.cleanup()
