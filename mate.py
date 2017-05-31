import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

t=0
r=10
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)


while True:
	for i in range(r):
		GPIO.output(21,1)
		GPIO.output(20,1)
		GPIO.output(16,0)
		sleep(t)

		GPIO.output(21,0)
		GPIO.output(20,0)
		GPIO.output(16,1)
		sleep(t)
		
	for i in range(r):
		GPIO.output(21,0)
		GPIO.output(20,1)
		GPIO.output(16,0)
		sleep(t)

		GPIO.output(21,1)
		GPIO.output(20,0)
		GPIO.output(16,1)
		sleep(t)
		
	for i in range(r):
		GPIO.output(21,1)
		GPIO.output(20,0)
		GPIO.output(16,0)
		sleep(t)

		GPIO.output(21,0)
		GPIO.output(20,1)
		GPIO.output(16,1)
		sleep(t)
		
	for i in range(r):
		GPIO.output(21,0)
		GPIO.output(20,0)
		GPIO.output(16,0)
		sleep(t)
		
		GPIO.output(21,1)
		GPIO.output(20,1)
		GPIO.output(16,1)
		sleep(t)



GPIO.cleanup()

