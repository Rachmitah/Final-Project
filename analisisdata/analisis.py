import numpy as np


class Analisis:
    def __init__(self, m1, m2, m3):
        self.rata_rata = self.ratamatrix(m1, m2, m3)
        self.simpangMax1 = self.simpangMax(m1)
        self.simpangMin1 = self.simpangMin(m1)
        self.simpangMax2 = self.simpangMax(m2)
        self.simpangMin2 = self.simpangMin(m2)
        self.simpangMax3 = self.simpangMax(m3)
        self.simpangMin3 = self.simpangMin(m3)
        self.akurasi1    = self.rSimpang(m1)
        self.akurasi2    = self.rSimpang(m3)
        self.akurasi3    = self.rSimpang(m3)

    def ratamatrix(self, matrix1, matrix2, matrix3):
        n = 0
        m = 0
        for y in matrix1:
            m = 0
            for x in y:
                m += 1
            n += 1
        data = np.zeros(shape=(n, m))
        n = 0
        m = 0
        for y in data:
            m = 0
            for x in y:
                data[n][m] = (matrix1[n][m] + matrix2[n][m] + matrix3[n][m]) / 3
                m += 1
            n += 1
        return data

    def simpangMax(self, matrix):
        nilaiMax = 0
        temp = 0
        n = 0
        m = 0
        for y in matrix:
            m = 0
            for x in y:
                temp = matrix[n][m] - self.rata_rata[n][m]
                if temp > nilaiMax:
                    nilaiMax = temp
                m += 1
            n += 1
        return nilaiMax

    def simpangMin(self, matrix):
        nilaiMin = 0
        temp = 0
        n = 0
        m = 0
        for y in matrix:
            m = 0
            for x in y:
                temp = matrix[n][m] - self.rata_rata[n][m]
                if temp < nilaiMin:
                    nilaiMin = temp
                m += 1
            n += 1
        return nilaiMin

    def rSimpang(self, matrix):
        n = 0
        count = 0
        sumary = 0
        for y in matrix:
            m = 0
            for x in y:
                count += 1
                temp = matrix[n][m] - self.rata_rata[n][m]
                sumary += temp
            n += 1
        simpang = sumary / count
        return simpang
