import time
import numpy as np
from ultra_man import get_range
from mapping import array6x4

arr = np.array([
    [1,   2,  3,  4,  5,  6],	# 1
    [12, 11, 10,  9,  8,  7],	# 2
    [13, 14, 15, 16, 17, 18],	# 3
    [24, 23, 22, 21, 20, 19]])	# 4

hsl = np.array([
    [0, 0, 0, 0, 0, 0],	# 1
    [0, 0, 0, 0, 0, 0],	# 2
    [0, 0, 0, 0, 0, 0],	# 3
    [0, 0, 0, 0, 0, 0]])# 4

n 	 = 1
posY = 0
posX = 0
for y in hsl:
        # Y Ganjil -> dari kiri ke kanan
        if (n == 1):
                for x in y:
                        # lakukan scan ultrasonic
                        hsl[posY][posX] = get_range()
                        print(hsl[posY][posX])
                        posX += 1
                        time.sleep(1)
                n = 0
        # Y Genap -> dari kanan ke kiri
        else:
                posX -= 1
                for x in reversed(y):
                        # lakukan scan ultrasonic
                        hsl[posY][posX] = get_range()
                        print(hsl[posY][posX])
                        posX -= 1
                        time.sleep(1)
                n = 1
        posY += 1

print(hsl)