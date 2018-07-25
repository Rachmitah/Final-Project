import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
usleep = lambda x : time.sleep(x/1000000.0)

GPIO_steppin = 7	
GPIO_dirpin  = 5	
GPIO_enpin   = 3	

GPIO.setup(GPIO_steppin, GPIO.OUT)
GPIO.setup(GPIO_dirpin, GPIO.OUT)
GPIO.setup(GPIO_enpin, GPIO.OUT)

GPIO.output(GPIO_enpin, True)
GPIO.output(GPIO_dirpin, False)
usleep(500)
def step():
	GPIO.output(GPIO_enpin, False)
	GPIO.output(GPIO_dirpin, False)
	
	n=0
	#print("Kiri")
	while n<=36000:
		n+=1
		GPIO.output(GPIO_steppin, False)
		GPIO.output(GPIO_steppin, True)
		usleep(100)
	

def stepB(arah, step, speed):
	GPIO.output(GPIO_enpin, True)
	GPIO.output(GPIO_dirpin, False)
	usleep(500)
	GPIO.output(GPIO_enpin, False)
	GPIO.output(GPIO_dirpin, arah)
	
	n=0
	#print("Kiri")
	while n<=step:
		n+=1
		GPIO.output(GPIO_steppin, False)
		GPIO.output(GPIO_steppin, True)
		usleep(speed)
	
	
if __name__=="__main__":
	#step()
	stepB(True, 40000, 150)
	print("harusnya berenti woiiiii")
	#time.sleep(1)
	#stepB(False, 1000, 150)


