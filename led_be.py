import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 24

while True:
	GPIO.setup(led,GPIO.OUT)
	GPIO.output(led,GPIO.HIGH)
	time.sleep(1)
	GPIO.setup(led,GPIO.OUT)
	GPIO.output(led,GPIO.LOW)
	time.sleep(0.5)
