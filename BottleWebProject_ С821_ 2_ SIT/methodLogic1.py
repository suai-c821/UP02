import random
import math
import itertools

#Метод для создания графа (матрицы)
def createGraph(chanceCreateBond, numberOfApex):
    graph = []
    for i in range(numberOfApex*numberOfApex):
        graph.append(0)

    for i in range(0,numberOfApex):
        for j in range(i,numberOfApex):
            if (random.randint(0,100)<=chanceCreateBond):
                graph[i*numberOfApex+j]=1
                graph[j*numberOfApex+i]=1
    return graph

#Метод преобразования матрицы в связи
def matrixToList(graph):
    k = 0
    point1 = 1
    bonds = []
    while k < len(graph):
        point2 = 1
        for g in range(0, int(math.sqrt(len(graph)))):
            if (graph[k+g] == 1):
                bonds.append(point1)
                bonds.append(point2)
            point2 += 1
        point1 += 1
        k += int(math.sqrt(len(graph)))

    g = 0
    while g < len(bonds):
        k = 0
        while k < len(bonds):
            if (((bonds[g] == bonds[k] and bonds[g+1] == bonds[k+1]) or (bonds[g] == bonds[k+1] and bonds[g+1] == bonds[k])) and g != k):
                bonds[g] = 0
                bonds[g+1] = 0
            k += 2
        g = g + 2

    outBonds = []
    for a in range(0, len(bonds)):
        if(bonds[a] != 0):
            outBonds.append(bonds[a])

    return outBonds

#Метод нахождения графа в графе
def findFragment(mainGraph, fragmentGraph):
    if (not mainGraph or not fragmentGraph):
        finalApexes = []
        return finalApexes

    points = []
    finalMainGraph = []
    maxMainGraph = max(mainGraph)
    for g in range(0,len(mainGraph)):
        finalMainGraph.append(mainGraph[g])

    symbols = ''
    finalSymbols = ''
    for i in range(0, max(finalMainGraph)):
        symbols += str(i+1)

    for k in itertools.permutations(symbols):

        mainGraph = []
        for g in range(0,len(finalMainGraph)):
            mainGraph.append(finalMainGraph[g])

        for g in range(0,len(mainGraph)):
            for l in range(0,len(symbols)):
                if (finalMainGraph[g] == int(symbols[l])):
                    mainGraph[g] = int(''.join(k)[l])

        i = 0
        count = []
        finalCount = []
        while i < len(fragmentGraph):
            j = 0
            while j < len(mainGraph):
                if ((fragmentGraph[i] == mainGraph[j] and fragmentGraph[i+1] == mainGraph[j+1]) or (fragmentGraph[i] == mainGraph[j+1] and fragmentGraph[i+1] == mainGraph[j])):
                    count.append(mainGraph[j])
                    count.append(mainGraph[j+1])
                    finalCount.append(finalMainGraph[j])
                    finalCount.append(finalMainGraph[j+1])
                j += 2
            i += 2
    
        if (len(count) == len(fragmentGraph)):
            points.append(finalCount)

    #Сортировка
    outPoints = []
    for g in range(0,len(points)):
        if (points[g] not in outPoints):
                outPoints.append(points[g])

    #Метод для получения вершин
    endApexes = []
    for g in range(0,len(outPoints)):
        bonds = outPoints[g]
        apexes = []
        for e in range(0,len(bonds)):
            if (bonds[e] not in apexes):
                apexes.append(bonds[e])
        endApexes.append(apexes)

    for g in range(0,len(endApexes)):
        endApexes[g] = sorted(endApexes[g])

    finalApexes = []
    for g in range(0,len(endApexes)):
        if (endApexes[g] not in finalApexes):
            finalApexes.append(endApexes[g])
    return finalApexes