from bottle import route, view, post, request
import pdb, json
import methodLogic1
import html
import datetime
import math

@post('/method1', method = 'post')
def generate():

    graph1 = request.forms.get('graph1')
    graph2 = request.forms.get('graph2')
    graph1Final = []
    graph2Final = []
    for i in range(0, len(graph1)):
        if(graph1[i]== "1" or graph1[i]== "0"):
            graph1Final.append(int(graph1[i]))

    for i in range(0, len(graph2)):
        if(graph2[i]== "1" or graph2[i]== "0"):
            graph2Final.append(int(graph2[i]))

    result1 = ""
    result2 = ""

    if (int(math.sqrt(len(graph1Final)))**2 != len(graph1Final)):
        return "Main graph is not correct"

    if (int(math.sqrt(len(graph2Final)))**2 != len(graph2Final)):
        return "Fragment graph is not correct"

    h = 0
    for i in range(0, int(math.sqrt(len(graph1Final)))):
        for j in range(0, int(math.sqrt(len(graph1Final)))):
            result1 += str(graph1Final[j+h]) + " "
        h += int(math.sqrt(len(graph1Final)))
        result1 += "<br>"

    h = 0
    for i in range(0, int(math.sqrt(len(graph2Final)))):
        for j in range(0, int(math.sqrt(len(graph2Final)))):
            result2 += str(graph2Final[j+h]) + " "
        h += int(math.sqrt(len(graph2Final)))
        result2 += "<br>"

    log = {}
    log['mainGraph'] = graph1Final
    log['fragmentGraph'] = graph2Final
    log['apexes'] = str(methodLogic1.findFragment(methodLogic1.matrixToList(graph1Final), methodLogic1.matrixToList(graph2Final)))
    jp = json.dumps(log)
    open('method1log.txt', 'a').write(jp + '\n' + "Date: " + str(datetime.datetime.now()) + '\n\n')

    return "Main graph: <br>" + result1 + "<br> Fragment graph: <br>" + result2 + "<br> Apexes: <br>" + str(methodLogic1.findFragment(methodLogic1.matrixToList(graph1Final), methodLogic1.matrixToList(graph2Final)))