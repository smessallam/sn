import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LIGHT = 4
GPIO.setup(LIGHT,GPIO.OUT)

try:
	while True:
		GPIO.output(LIGHT,True)
		time.sleep(0.5)
		GPIO.output(LIGHT,False)
		time.sleep(0.5)
		print("blink")
except KeyboardInterrupt:
	GPIO.cleanup()
