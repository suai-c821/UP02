from collections import defaultdict
import random
import math
   
class Graph:  
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list) 
   
    def addEdge(self,u,v):
        self.graph[u].append((v))
        self.graph[v].append((u))
   
    def isVisited(self,v,visited): 
        visited[v]= True
  
        for i in self.graph[v]:
            if visited[i]==False:
                self.isVisited(i,visited)
   
    def isConnected(self):
        visited =[False]*(self.V)
        for i in range(self.V):
            if len(self.graph[i]) > 1:
                break       
        if i == self.V-1:
            return True
        self.isVisited(i,visited)
        for i in range(self.V):
            if visited[i]==False and len(self.graph[i]) > 0:
                return False
          
        return True

    def isEulerian(self):
        if self.isConnected() == False:
            return 0
        else:
            odd = 0
            for i in range(self.V):
                if len(self.graph[i]) % 2 !=0:
                    odd +=1
            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0
  
    def test(self):
         res = self.isEulerian()
         if res == 0:
             result = "graph is not Eulerian"
         elif res ==1 :
             result = "graph has a Euler path"
         else:
             result = "graph has a Euler cycle"
         return result 

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

def splitMatirx(graph, lists=1):
    length = len(graph)
    return [graph[i*length // lists: (i+1)*length // lists] for i in range(lists)]

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