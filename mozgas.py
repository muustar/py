from gpiozero import MotionSensor, LED

led = LED(14)

pir = MotionSensor(4)
a=0
while True:
    if pir.motion_detected:
        print("megmozdultál",a)
        led.on()
        a=a+1

    else:
        led.off()
        
