import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.IN)

ido = 0.06

pinekvissza = pinek = [4,17,27,22,10,9,11,5,6,13,19,26]


## ledek felkapcsolasa
#input = GPIO.input(18)
while True:
	if ((GPIO.input(18))==False):
		print("nyomva")
		break
	pinekvissza = [4,17,27,22,10,9,11,5,6,13,19,26]
	for i in pinek:
		#print(i,"be")
		GPIO.setup(i,GPIO.OUT)
		GPIO.output(i,True)
		time.sleep(ido)
	while len(pinekvissza):
		pin=pinekvissza.pop()
		#print("vissza:",pin)
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,False)
		time.sleep(ido)




#time.sleep(2)
GPIO.cleanup()

