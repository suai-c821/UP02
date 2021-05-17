from collections import defaultdict
from bottle import post, request, template, run
import random
import math
import methodLogic3
import json
import datetime


@post('/method3', method='post')
def my_form():
    apexes = request.forms.get('ADRESS')
 
    if(apexes.isdigit()):   
        apexes = int(apexes)
        if(apexes > 0):
            matrix = methodLogic3.createGraph(70, apexes)
            splitedMatrix = methodLogic3.splitMatirx(matrix, apexes)

            for i in range(len(splitedMatrix)):
                print(splitedMatrix[i])

            graph = methodLogic3.matrixToList(matrix)
            print(graph)
            connects = int(len(graph)/2)
            vertices = max(graph) + 1
            j = 0
            g1 = methodLogic3.Graph(vertices);

            for i in range(connects):
                g1.addEdge(graph[j],graph[j+1])
                j = j + 2;

            result = " " 
            with open ('data.txt', 'a') as outfile:
                        jp = json.dumps(apexes)
                        open('data.txt', 'a').write("Number of apexes: " + jp + " Time  : " + str(datetime.datetime.now()) + '\n')
 
            for i in range(len(splitedMatrix)):
                result += str(splitedMatrix[i]) + "<br/>" 

            result += str(graph) + "<br/>" + str(g1.test()) + "<br/>"

            return result 
        else:
            return "Apexes can`t be 0"
    else:
        return "Wrong apex"
