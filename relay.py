import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.output(18,1)	
GPIO.output(23,1)
GPIO.setup(4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
statusz = False
try:
	while True:
		gomb=GPIO.input(4)
		if (gomb == False) and statusz:
			print("Ki")
			statusz=False
			GPIO.output(18,1)	
			GPIO.output(23,1)
			sleep(0.2)
		else:
			if gomb == False:
				statusz=True
				print("Be")
				GPIO.output(18,0)		
				GPIO.output(23,0)
				sleep(0.2)
except KeyboardInterrupt:
	print("Felhasznaloi megszakitas")
	GPIO.cleanup()

