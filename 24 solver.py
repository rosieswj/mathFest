from tkinter import *
import random

def init(data):
    data.randlist = []
    data.solution = ''
    data.mode = 0
    data.startgenerate = False
    data.input = ''
    data.order = 0
    data.answer = False
    data.timeToCheck = False
    data.timeToCheckNoAnswer = False
    data.showOneSolution = False
    data.showAllSolution = False
    data.solutionList = []
    data.cantsolve = False
    data.minute = 0
    data.second = 0
    data.minuteString = ""
    data.secondString = ""
    data.timing = False
    
def mousePressed(event, data):
    # play 24
    if(data.mode == 0 and event.x > 200 and event.x < 400 and event.y > 250 and event.y < 350):
        data.mode += 1
    if(data.mode == 1):
        # generate numbers
        if(event.x > 180 and event.x < 420 and event.y > 80 and event.y < 120):
            data.showOneSolution = False
            data.timeToCheck = False
            data.timeToCheckNoAnswer = False
            randomGenerator(data)
            data.startgenerate = True
            data.timing = True
            data.minute = 0
            data.second = 0
        # can't solve
        if(event.x > 410 and event.x < 510 and event.y > 300 and event.y < 340):
            data.timeToCheckNoAnswer = True
        # submit
        if(event.x > 200 and event.x < 290 and event.y > 350 and event.y < 390):
            data.timeToCheck = True
        # solution
        if(event.x > 310 and event.x < 400 and event.y > 350 and event.y < 390):
            data.showOneSolution = True
            data.timing = False
            data.timeToCheck = False
            data.timeToCheckNoAnswer = False
        # try another one in mode 1
        if(data.showOneSolution == True and event.x > 125 and event.x < 235 and event.y > 510 and event.y < 550):
            data.showOneSolution = False
            data.startgenerate = False
            data.timeToCheck = False
            data.timeToCheckNoAnswer = False
            data.input = ""
            data.minute = 0
            data.second = 0
        # show all solutions
        if(data.showOneSolution == True and event.x > 245 and event.x < 355 and event.y > 510 and event.y < 550):
            data.mode = 3
            data.minute = 0
            data.second = 0
        # exit in mode 1
        if(data.showOneSolution == True and event.x > 365 and event.x < 475 and event.y > 510 and event.y < 550):
            data.showOneSolution = False
            data.mode = 0
            data.startgenerate = False
            data.timeToCheck = False
            data.timeToCheckNoAnswer = False
            data.minute = 0
            data.second = 0
            data.input = ""
    if(data.mode == 2):
        # try another one in mode 2
        if(event.x > 180 and event.x < 290 and event.y > 330 and event.y < 370):
            data.mode = 1
            data.startgenerate = False
            data.timeToCheck = False
            data.timeToCheckNoAnswer = False
            data.minute = 0
            data.second = 0
            data.input = ""
        # exit in mode 2
        if(event.x > 310 and event.x < 420 and event.y > 330 and event.y < 370):
            data.mode = 0
            data.startgenerate = False
            data.timeToCheck = False
            data.timeToCheckNoAnswer = False
            data.minute = 0
            data.second = 0
            data.input = ""
    if(data.mode == 3):
        # try another one in mode 3
        if(event.x > 180 and event.x < 290 and event.y > 330 and event.y < 370):
            data.showOneSolution = False
            data.showAllSolution = False
            data.mode = 1
            data.startgenerate = False
            data.timeToCheck = False
            data.timeToCheckNoAnswer = False
            data.minute = 0
            data.second = 0
            data.input = ""
        # exit in mode 3
        if(event.x > 310 and event.x < 420 and event.y > 330 and event.y < 370):
            data.showOneSolution = False
            data.showAllSolution = False
            data.mode = 0
            data.startgenerate = False
            data.timeToCheck = False
            data.timeToCheckNoAnswer = False
            data.minute = 0
            data.second = 0
            data.input = ""
    
def keyPressed(event, data):
    if(event.keysym == "1"): 
        data.input += '1'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "2"): 
        data.input += '2'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "3"): 
        data.input += '3'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "4"): 
        data.input += '4'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "5"): 
        data.input += '5'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "6"): 
        data.input += '6'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "7"): 
        data.input += '7'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "8"): 
        data.input += '8'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "9"): 
        data.input += '9'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "0"): 
        data.input += '0'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "plus"): 
        data.input += '+'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "minus"): 
        data.input += '-'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "asterisk"): 
        data.input += '*'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "slash"): 
        data.input += '/'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "parenleft"):
        data.input += '('
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "parenright"):
        data.input += ')'
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False
    if(event.keysym == "BackSpace" and len(data.input) > 0):
        data.input = data.input[:len(data.input)-1]
        data.timeToCheck = False
        data.timeToCheckNoAnswer = False

def timerFired(data):
    if(data.timing == True):
        timing(data)
    
def redrawAll(canvas, data):
    if(data.mode == 0):
        drawBackground(canvas)
    elif(data.mode == 1):
        drawTime(canvas,data)
        drawGenerator(canvas,data)
        if(data.startgenerate == True):
            solution(data)
            drawFourNumbers(canvas,data)
            drawWriteAnswer(canvas)
            drawAnswer(canvas, data)
            if(data.timeToCheck == True):
                checkAnswer(data)
                if(data.answer == True):
                    data.timing = False
                    data.mode += 1
                else:
                    drawNotCorrect(canvas)
            if(data.timeToCheckNoAnswer == True):
                checkNoAnswer(data)
                if(data.answer == True):
                    data.timing = False
                    data.mode += 1
                else:
                    drawNotCorrect(canvas)
            if(data.showOneSolution == True):
                drawSolution(canvas, data)
    elif(data.mode == 2):
        drawCorrect(canvas, data)
    elif(data.mode == 3):
        drawAllSolutions(canvas, data)
    
# functions

def timing(data):
    data.second += 1
    if(data.second == 60):
        data.minute += 1
        data.second = 0
    
def randomGenerator(data):
    data.cantsolve = False
    data.randlist = []
    for i in range(0,4):
        n = random.randint(1,13)
        data.randlist.append(str(n))
    
def solution(data):
    data.solution = ''
    data.solutionList = solve24(data.randlist)
    if(len(data.solutionList) == 0):
        data.cantsolve = True
    else:
        data.solution += data.solutionList[0]
        data.solution += "=24 "
        
def checkAnswer(data):
    try:
        if(eval(data.input) == 24):
            data.answer = True
        else:
            data.answer = False
    except:
        data.answer = False
        
def checkNoAnswer(data):
    if(data.cantsolve == True):
        data.answer = True
    else:
        data.answer = False
        
def generateTime(data):
    time = ""
    minute = ""
    second = ""
    if(data.minute < 10):
        minute = "0" + str(data.minute)
    else:
        minute = str(data.minute)
    if(data.second < 10):
        second = "0" + str(data.second)
    else:
        second = str(data.second)
    time = minute + " : " + second
    return time
    
# draw
def drawBackground(canvas):
    canvas.create_rectangle(200,250,400,350)
    canvas.create_text(300,300,text="Play 24",font="Helvetica 26 bold")
    
def drawTime(canvas, data):
    time = generateTime(data)
    canvas.create_rectangle(4,4,50,24)
    canvas.create_text(27,14,text = time)
    
def drawGenerator(canvas, data):
    canvas.create_rectangle(180,80,420,120)
    canvas.create_text(300,100,text="Generate your cards:",font="Helvetica 16")
    
def drawFourNumbers(canvas, data):
    for i in range(0,4):
        canvas.create_text(150+100*i, 170, text=data.randlist[i])
        
def drawWriteAnswer(canvas):
    canvas.create_text(300, 220, text="Write your answer using only numbers and such operators:")
    canvas.create_text(300, 250, text="+  -  *  /  (  )")
    canvas.create_rectangle(200, 300, 400, 340)
    canvas.create_rectangle(410, 300, 510, 340)
    canvas.create_text(460, 320, text="Can't solve")
    canvas.create_rectangle(200, 350, 290, 390)
    canvas.create_text(245, 370, text="Submit")
    canvas.create_rectangle(310, 350, 400, 390)
    canvas.create_text(355, 370, text="Solution")
    
def drawAnswer(canvas, data):
    canvas.create_text(300, 320, text=data.input)
    
def drawCorrect(canvas, data):
    time = generateTime(data)
    canvas.create_text(300, 250, text="Correct!", font="Helvetica 50")
    canvas.create_text(300, 300, text="Your time is: " + time)
    canvas.create_rectangle(180, 330, 290, 370)
    canvas.create_text(235, 350, text="Try Another One")
    canvas.create_rectangle(310, 330, 420, 370)
    canvas.create_text(365, 350, text="Exit")
    
def drawNotCorrect(canvas):
    canvas.create_text(300, 410, text="Sorry, please try again...")
        
def drawSolution(canvas, data):
    if(data.cantsolve == True):
        canvas.create_text(300, 450, text="You can't solve it")
    else:
        space = 0
        for i in range(1,len(data.solution)-1):
            if(data.solution[i].isdigit() and data.solution[i-1].isdigit()):
                space += 1
            canvas.create_text(10+35*i-28*space, 450, text=data.solution[i])
    canvas.create_rectangle(125, 510, 235, 550)
    canvas.create_text(180, 530, text="Try Another One")
    canvas.create_rectangle(245, 510, 355, 550)
    canvas.create_text(300, 530, text="Show All Answers")
    canvas.create_rectangle(365, 510, 475, 550)
    canvas.create_text(420, 530, text="Exit")
    
def drawAllSolutions(canvas, data):
    space = 0
    for i in range(0, len(data.solutionList)):
        data.solution = data.solutionList[i]
        data.solution += "=24 "
        for j in range(1,len(data.solution)-1):
            if(data.solution[j].isdigit() and data.solution[j-1].isdigit()):
                space += 1
            canvas.create_text(10+35*j-28*space, 60+60*i, text=data.solution[j])
        space = 0
    canvas.create_rectangle(180, 330, 290, 370)
    canvas.create_text(235, 350, text="Try Another One")
    canvas.create_rectangle(310, 330, 420, 370)
    canvas.create_text(365, 350, text="Exit")
    
# solver

def checkOperators(n):
    operators = []
    for i in range(0, len(n)):
        if(n[i] in '+-*/'):
            operators.append(n[i])
            operators.sort()
    return operators

def solve24(n): 
    result=[]
    def solve(n):
        length=len(n)
        if length == 1 and eval(n[0]) == 24:
            if(len(result) == 0):
                result.append(n[0])
            else:
                count = 0
                for i in range(0, len(result)):
                    if(checkOperators(n[0]) != checkOperators(result[i])):
                        count += 1
                if(count == len(result)):
                    result.append(n[0])
        for number1 in range(length):
            for number2 in range(length):
                if number1 != number2:
                    for operator in '+-*/':
                        answer=list(n)
                        answer[number1]='('+n[number1]+operator+n[number2]+')'
                        del answer[number2]
                        if operator!='/' or eval(n[number2])!=0:
                            solve(answer)
    solve(n)
    return result
    
# run function
    
def run(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 1000 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run()
