import math


class SeamCarving:

    def __init__(self):
        return



    def run(self, image):
        global h, w, EnergyMap, seam
        h = len(image)
        w = len(image[0])
        EnergyMap = [[0 for i in range(w)] for j in range(h)]
        for i in range(w):
            for j in range(h):
                self.e(j,i,image)
        seam = []
        for j in range(h - 2, -1, -1):
            for i in range(w):
                if i == 0:
                    minPixel = min(EnergyMap[j + 1][i], EnergyMap[j + 1][i + 1])
                elif i == w - 1:
                    minPixel = min(EnergyMap[j + 1][i], EnergyMap[j + 1][i - 1])
                else:
                    minPixel = min(EnergyMap[j + 1][i], EnergyMap[j + 1][i + 1], EnergyMap[j + 1][i - 1])
                EnergyMap[j][i] += minPixel
        minVal = float("inf")
        minIndex = 0
        for p in range(len(EnergyMap[0])):
            if (EnergyMap[0][p] < minVal):
                minVal = EnergyMap[0][p]
                minIndex = p

        seam.append(minIndex)
        weight = minVal
        for j in range(1, h):
            if minIndex == 0:
                minVal = EnergyMap[j][minIndex]
                if EnergyMap[j][minIndex+1] < minVal:
                    minIndex = minIndex+1
                seam.append(minIndex)
            elif minIndex == w - 1:
                minVal = EnergyMap[j][minIndex-1]
                if EnergyMap[j][minIndex] < minVal:
                    minIndex = minIndex
                else:
                    minIndex = minIndex - 1
                seam.append(minIndex)
            else:
                minVal = EnergyMap[j][minIndex - 1]
                index = minIndex - 1
                if EnergyMap[j][minIndex] < minVal:
                    minVal = EnergyMap[j][minIndex]
                    index = minIndex
                if EnergyMap[j][minIndex+1] < minVal:
                    index = minIndex + 1
                minIndex = index
                seam.append(minIndex)
        return weight


    def getSeam(self):
        return seam

    def e(self, j, i, image):
        energy = 0
        if j == 0:
            if i == 0:
                energy += self.d(j,i,j,i+1,image) + self.d(j,i,j+1,i+1,image) + self.d(j,i,j+1,i,image)
                energy = energy / 3
            elif i == w-1:
                energy += self.d(j,i,j,i-1,image) + self.d(j,i,j-1,i-1,image) + self.d(j,i,j+1,i,image)
                energy = energy / 3
            else:
                energy += self.d(j,i,j,i+1,image) + self.d(j,i,j+1,i+1,image) + self.d(j,i,j+1,i,image)
                energy += self.d(j,i,j,i-1,image) + self.d(j,i,j+1,i-1,image)
                energy = energy / 5
        elif i == 0:
            if j == h-1:
                energy += self.d(j,i,j-1,i,image) + self.d(j,i,j-1,i+1,image) + self.d(j,i,j,i+1,image)
                energy = energy / 3
            else:
                energy += self.d(j,i,j-1,i,image) + self.d(j,i,j-1,i+1,image) + self.d(j,i,j,i+1,image)
                energy += self.d(j,i,j+1,i,image) + self.d(j,i,j+1,i+1,image)
                energy = energy / 5
        elif j == h-1:
            if i == w-1:
                energy += self.d(j,i,j,i-1,image) + self.d(j,i,j-1,i,image) +self.d(j,i,j-1,i-1,image)
                energy = energy / 3
            else:
                energy += self.d(j,i,j,i-1,image) + self.d(j,i,j-1,i,image) +self.d(j,i,j-1,i-1,image)
                energy += self.d(j,i,j-1,i+1,image) + self.d(j,i,j,i+1,image)
                energy = energy / 5
        elif i == w-1:
            energy += self.d(j,i,j,i-1,image) + self.d(j,i,j-1,i,image) +self.d(j,i,j-1,i-1,image)
            energy += self.d(j,i,j+1,i-1,image) + self.d(j,i,j+1,i,image)
            energy = energy / 5
        else:
            energy += self.d(j,i,j+1,i,image) + self.d(j,i,j+1,i-1,image) + self.d(j,i,j+1,i+1,image) + self.d(j,i,j,i+1,image)
            energy += self.d(j,i,j,i-1,image) + self.d(j,i,j-1,i,image) + + self.d(j,i,j-1,i-1,image) + self.d(j,i,j-1,i+1,image)
            energy = energy / 8
        EnergyMap[j][i] = energy


    def d(self, j, i, m, n, image):
        distance = math.sqrt((image[j][i][0]-image[m][n][0])**2+(image[j][i][1]-image[m][n][1])**2+(image[j][i][2]-image[m][n][2])**2)
        return distance


