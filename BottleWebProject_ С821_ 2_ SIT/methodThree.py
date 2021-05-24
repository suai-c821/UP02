from collections import defaultdict
from bottle import post, request, template, run
import random
import math
import methodLogic3
import json
from datetime import datetime


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
            euler = methodLogic3.findEuler(methodLogic3.split(graph))

            open('method3.log', 'a').write(f"[{datetime.strftime(datetime.utcnow(), '%Y-%m-%d %H:%M:%S')}] {json.dumps(matrixFinal)}\n")

            return f"Matrix: <br/>{matrixFinal}<br/><br/>Connects: <br/>{graph}<br/><br/>Result: <br/>{euler}"

    else:
        return "Matrix can`t be empty"
