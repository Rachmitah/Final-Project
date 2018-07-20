import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
usleep = lambda x : time.sleep(x/1000000.0)

GPIO_steppin = 15	
GPIO_dirpin  = 13	
GPIO_enpin   = 11	

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
	while n<=24000:
		n+=1
		GPIO.output(GPIO_steppin, False)
		usleep(0)
		GPIO.output(GPIO_steppin, True)
		usleep(250)
		

def stepA(arah, step, speed):
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
	stepA(False, 31000, 150)
	#print("harusnya berenti woiiiii")
	#time.sleep(1)
	#stepA(False, 12000, 150)
