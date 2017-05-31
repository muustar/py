import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ido=0.02
GPIO.setup(26,GPIO.IN)
GPIO.setup(19,GPIO.IN)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
while True:
	#0-dik
	#print(GPIO.input(19))
	if (GPIO.input(19)==False):
		if (ido>=0.002):
			ido=ido-0.002
		print("fel")
	if (GPIO.input(26)==False):
		ido=ido+0.009
		print("le")
	if (GPIO.input(19)==False)and(GPIO.input(26)==False):
		break
	GPIO.output(21,0)	
	GPIO.output(20,0)
	GPIO.output(16,0)
	#print("000")
	sleep(ido)

	# 1.
	GPIO.output(21,0)	
	GPIO.output(20,0)
	GPIO.output(16,1)
	#print("001")
	sleep(ido)

	# 2.
	GPIO.output(21,0)	
	GPIO.output(20,1)
	GPIO.output(16,0)
	#print("010")
	sleep(ido)

	# 3.
	GPIO.output(21,0)	
	GPIO.output(20,1)
	GPIO.output(16,1)
	#print("011")
	sleep(ido)

	# 4.
	GPIO.output(21,1)	
	GPIO.output(20,0)
	GPIO.output(16,0)
	#print("100")
	sleep(ido)

	# 5.
	GPIO.output(21,1)	
	GPIO.output(20,0)
	GPIO.output(16,1)
	#print("101")
	sleep(ido)

	# 6.
	GPIO.output(21,1)	
	GPIO.output(20,1)
	GPIO.output(16,0)
	#print("110")
	sleep(ido)

	# 7.
	GPIO.output(21,1)	
	GPIO.output(20,1)
	GPIO.output(16,1)
	#print("111")
	sleep(ido)

GPIO.cleanup()
