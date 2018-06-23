import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
usleep = lambda x : time.sleep(x/1000000.0)

GPIO_steppin = 15
GPIO_dirpin  = 13
GPIO_enable  = 11

GPIO.setup(GPIO_steppin, GPIO.OUT)
GPIO.setup(GPIO_dirpin, GPIO.OUT)

stp = 0
dir = 0
ext = 0

GPIO.output(GPIO_dirpin, False)
GPIO.output(GPIO_steppin, False)

while True:
	GPIO.output(GPIO_dirpin, True)
	usleep(1000)
	GPIO.output(GPIO_dirpin, False)
	usleep(1000)
	stp += 1
	if (stp > 3200):
		ext += 1
		if (dir == 0):
			print("LEFT")
			GPIO.output(GPIO_steppin, True)
			dir = 1
		else:
			print("RIGHT")
			GPIO.output(GPIO_steppin, False)
			dir = 0
		stp = 0
	if (stp == 0):
		usleep(500)

	if (ext == 4):
		GPIO.output(GPIO_dirpin, False)
		GPIO.output(GPIO_steppin, False)
		time.sleep(1)
		ext = 0
