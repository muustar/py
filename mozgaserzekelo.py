import RPi.GPIO as GPIO
import subprocess
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(10,GPIO.IN)
GPIO.setup(18,GPIO.OUT)

pir = 0
i=0
while True:
    if GPIO.input(10):
		print("Mozgas",i) 
		i=i+1       
		GPIO.output(18,0)
		subprocess.call("/bin/sh /home/pi/nfs-malna/py/camera.sh", shell=True)
		#sleep(1)
		pir=1
    else:
		if pir:
			for x in range(1,4):
				subprocess.call("/bin/sh /home/pi/nfs-malna/py/camera.sh", shell=True)
				print("varakozas mozgasra")
			#sleep(5)
			if (GPIO.input(10)==0):	
				GPIO.output(18,1)
		pir=0
		i=0
    
