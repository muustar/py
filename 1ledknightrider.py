import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.IN)

ido = 0.04

pinekvissza = pinek = [4,17,27,22,10,9,11,5,6,13,19,26]


## ledek felkapcsolasa
#input = GPIO.input(18)
while True:
	if ((GPIO.input(18))==False):
		print("nyomva")
		break
	pinek = [4,17,27,22,10,9,11,5,6,13,19,26]
	j=pinek.pop()
	pinek.append(j)
	for i in pinek:
		#print(i,"be")
		GPIO.setup(i,GPIO.OUT)
		GPIO.output(i,True)
		time.sleep(ido)
		j=i
		GPIO.setup(j,GPIO.OUT)
		GPIO.output(j,False)
		#time.sleep(ido)
	#print(pinek)
	while len(pinek):		
		j=pinek.pop()
		GPIO.setup(j,GPIO.OUT)
		GPIO.output(j,True)
		time.sleep(ido)
		#print(j)
		GPIO.setup(j,GPIO.OUT)
		GPIO.output(j,False)
		
		




#time.sleep(2)
GPIO.cleanup()

