import numpy as np
import random

# mockup array execute every timeN
arr = np.array([
    [1, 2, 3, 4, 5, 6],  # 1
    [12, 11, 10, 9, 8, 7],  # 2
    [13, 14, 15, 16, 17, 18],  # 3
    [24, 23, 22, 21, 20, 19]])  # 4


def initialisasi():
    # This for init
    filename = "data.py"
    with open(filename, 'r') as file:
        data = file.readlines()
    print(data)
    print("Your name: " + data[0])
    data[0] = '#1\n'
    with open(filename, 'w') as file:
        file.writelines(data)


def writeData(arr):
    # This for Writeing Data
    # initialisasi()

    filename = "data.py"
    file = open(filename, 'a')
    file.write("dat = ")
    file.write("np.array([\n")
    z = 0
    for x in arr:
        file.write("	[")
        n = 0
        for y in x:
            print(n)
            file.write(str(y))
            if n == len(x) - 1:
                file.write("")
            else:
                file.write(", ")
            n += 1
        if z == len(arr) - 1:
            file.write("]")
        else:
            file.write("],\n")
        z += 1
    file.write("])\n\n")
    file.close()


def simpanDataAnalisis(name, matrix, max1, min1, max2, min2, max3, min3, acu1, acu2, acu3):
    filename = "dataHasilAnalisis.py"
    file = open(filename, 'a')
    file.write(name + " = ")
    file.write("np.array([\n")
    z = 0
    for x in matrix:
        file.write("	[")
        n = 0
        for y in x:
            file.write(str(y))
            if n == len(x) - 1:
                file.write("")
            else:
                file.write(", ")
            n += 1
        if z == len(arr) - 1:
            file.write("]")
        else:
            file.write("],\n")
        z += 1

    file.write("])\n")

    file.write(name)
    file.write("_simpangMax1 = ")
    file.write(str(max1))
    file.write("\n")

    file.write(name)
    file.write("_simpangMin1 = ")
    file.write(str(min1))
    file.write("\n")

    file.write(name)
    file.write("_simpangMax2 = ")
    file.write(str(max2))
    file.write("\n")

    file.write(name)
    file.write("_simpangMin2 = ")
    file.write(str(min2))
    file.write("\n")

    file.write(name)
    file.write("_simpangMax3 = ")
    file.write(str(max3))
    file.write("\n")

    file.write(name)
    file.write("_simpangMin3 = ")
    file.write(str(min3))
    file.write("\n")

    file.write(name)
    file.write("_akurasi_1 = ")
    file.write(str(acu1))
    file.write("\n")

    file.write(name)
    file.write("_akurasi_2 = ")
    file.write(str(acu2))
    file.write("\n")

    file.write(name)
    file.write("_akurasi_3 = ")
    file.write(str(acu3))
    file.write("\n")

    file.close()


def readDataAndCalculate():
    # This for Read a certain amount of data and calculate all
    import data
    print("")


def calculating():
    # This for calculating the data
    print("")


if __name__ == "__main__":
    # This main program
    writeData(arr)
# readDataAndCalculate()
