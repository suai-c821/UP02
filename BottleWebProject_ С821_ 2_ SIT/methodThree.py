from collections import defaultdict
from bottle import post, request, template, run
import random
import math
import methodLogic3
import json
import datetime


@post('/method3', method='post')
def my_form():
    
    matrix = request.forms.get('matrix')
    
    if(matrix is not ""):        

        matrixFinal = []

        for i in range(0, len(matrix)):
            if(matrix[i]== "1" or matrix[i]== "0"):
                matrixFinal.append(int(matrix[i]))

        if (int(math.sqrt(len(matrixFinal)))**2 != len(matrixFinal)):
            return "Main graph is not correct"

        if (len(matrix) == 1 and str(matrix[0]) == "0"):
            return "Can`t be 0"

        else:
            graph = methodLogic3.matrixToList(matrixFinal)

            splitedGraph = methodLogic3.split(graph)     

            result = " " 
            with open ('method3log.txt', 'a') as outfile:
                        jp = json.dumps(matrixFinal)
                        open('method3log.txt', 'a').write("Matrix: " + jp + " Time  : " + str(datetime.datetime.now()) + '\n')
 
            result += "Matrix: " + "<br/>" + str(matrixFinal) + "<br/>"

            euler = methodLogic3.findEuler(splitedGraph)

            result += "<br/>" + "Connects: " + "<br/>" +  str(graph) + "<br/>" + "<br/>" + "Result: " + "<br/>" + str(euler)

            return result 

    else:
        return "Matrix can`t be empty"
