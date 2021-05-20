import math
import random

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

#заполнить лист нужным образом
def split(graph):
    apexes = []
    k = len(graph)/2
    j = 0
    for i in range(int(k)):
        apexes.append(())
    
    for i in range(int(k)):
        apexes[i] += (graph[j], graph[j+1])
        j = j + 2
    return apexes

#метод поиска эйлерова пути
def sub(visited, _cur, graph):
    if not graph:
        return visited + [_cur]
    for i, edge in enumerate(graph):
        cur, nex = edge
        if _cur not in edge:
            continue
        _graph = graph[:]
        del _graph[i]
        if _cur == cur:
            res = sub(visited + [cur], nex, _graph)
        else:
            res = sub(visited + [nex], cur, _graph)
        if res:
            return res

def findEuler(graph):
    head, tail = graph[0], graph[1:]
    prev, nex = head
    return sub([prev], nex, tail)

