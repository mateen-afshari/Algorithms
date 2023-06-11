import math


class ClosestPair:
    def __init__(self):
        return

  
    # @return the distances between the closest pair and second closest pair
    # with closest at position 0 and second at position 1
    def dist(self, file_data):
        min = float("inf")
        for i in range(len(file_data)):
            for j in range(i + 1, len(file_data)):
                x1 = float(file_data[i].split()[0])
                y1 = float(file_data[i].split()[1])
                x2 = float(file_data[j].split()[0])
                y2 = float(file_data[j].split()[1])
                delta = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if (delta < min):
                    min = delta
        return min

    def dist2(self, file_data):
        min = float("inf")
        global d
        for i in range(len(file_data)):
            for j in range(i + 1, len(file_data)):
                x1 = float(file_data[i].split()[0])
                y1 = float(file_data[i].split()[1])
                x2 = float(file_data[j].split()[0])
                y2 = float(file_data[j].split()[1])
                delta = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if (delta < min and delta != d):
                    min = delta
        return min

    def cpp(self, X):
        global d
        if (len(X) <= 3):
            return self.dist(X)

        mid = len(X) // 2
        midpoint = float(X[mid].split()[0])
        l = X[0:mid]
        r = X[mid:]

        dl = self.cpp(l)
        dr = self.cpp(r)
        d = min(dl, dr)

        runway = []

        for i in range(len(X)):
            if (abs(float(X[i].split()[0]) - midpoint) < d):
                runway.append(X[i])
        runway.sort(key=lambda y: float(y.split()[1]))
        # print(runway)
        for i in range(len(runway)):
            for j in range(i + 1, min(len(runway), i+8)):
                x1 = float(runway[i].split()[0])
                y1 = float(runway[i].split()[1])
                x2 = float(runway[j].split()[0])
                y2 = float(runway[j].split()[1])
                delta = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if delta < d:
                    d = delta
        return d

    def scpp(self, X):
        global d
        if (len(X) <= 3):
            return self.dist2(X)

        mid = len(X) // 2
        midpoint = float(X[mid].split()[0])
        l = X[0:mid]
        r = X[mid:]

        dl = self.scpp(l)
        dr = self.scpp(r)
        d2 = min(dl, dr)

        runway = []

        for i in range(len(X)):
            if (abs(float(X[i].split()[0]) - midpoint) < d2):
                runway.append(X[i])
        runway.sort(key=lambda y: float(y.split()[1]))
        for i in range(len(runway)):
            for j in range(i + 1, min(len(runway), i + 8)):
                x1 = float(runway[i].split()[0])
                y1 = float(runway[i].split()[1])
                x2 = float(runway[j].split()[0])
                y2 = float(runway[j].split()[1])
                delta = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if (delta < d2 and delta != d):
                    d2 = delta
        return d2

    def compute(self, file_data):
        file_data.sort(key=lambda x: float(x.split()[0]))
        closest = self.cpp(file_data)
        secondClosest = self.scpp(file_data)
        return [closest, secondClosest]
