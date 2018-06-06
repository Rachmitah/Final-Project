from Stepper import Stepper
import time
#stepper variables
#[stepPin, directionPin, enablePin]
testStepper = Stepper([11, 13, 15])

#test stepper
while True:
	testStepper.step(1500, "right") #steps, dir, speed, stayOn
	time.sleep(1)
	testStepper.step(1500, "left")
	time.sleep(1)
