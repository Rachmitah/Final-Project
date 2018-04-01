import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set mode
GPIO_TRIG = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIG,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

#set awalan trigger low
GPIO.output(GPIO_TRIG,GPIO.LOW)

#fungs ntuk mendapatkan jarak
def get_range():
        #kirim 10us sinyal high ke trigger
        GPIO.output(GPIO_TRIG, True)
        time.sleep(0.00001)

        #stop trigger
        GPIO.output(GPIO_TRIG,False)
        timeout_counter = int(time.time())
        start = time.time()

        #mendapatkan waktu start
        while ((GPIO.input(GPIO_ECHO)==0) and (int(time.time() - timeout_counter) < 3)):
                start = time.time()

        timeout_counter = int(time.time())
        stop = time.time()
        #mendapatkan waktu stop
        while ((GPIO.input(GPIO_ECHO)==1) and (int(time.time() - timeout_counter) < 3)):
                stop = time.time()

        #hitungwakt tempuh bolak balik
        pulse = stop.start

        #hitung jarak
        distance = (pulse*0.034)/2

        return distance

#panggil fungsi
jarak = get_range()
print("jarakk = %.2f cm % jarak")
