from bottle import route, view, post, request
import pdb, json
import methodLogic1
import html
from datetime import datetime
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

    jf = json.dumps({
        'mainGraph': graph1Final,
        'fragmentGraph': graph2Final,
        'apexes': str(methodLogic1.findFragment(methodLogic1.matrixToList(graph1Final), methodLogic1.matrixToList(graph2Final))),
    })
    open('method1.log', 'a').write(f"[{datetime.strftime(datetime.utcnow(), '%Y-%m-%d %H:%M:%S')}] {jf}\n")

    return f"Main graph: <br>{result1}<br> Fragment graph: <br>{result2}<br> Apexes: <br>{methodLogic1.findFragment(methodLogic1.matrixToList(graph1Final), methodLogic1.matrixToList(graph2Final))}"