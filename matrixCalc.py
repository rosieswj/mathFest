from tkinter import *
from oop_matrix import Matrix, Rational
import copy

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

class MovingNumber(object):
    vanishSpeed=10
    leftSpeed=10
    rightSpeed=10
    swapSpeed=10
    dis=0
    
    def __init__(self,numStr,row,col,x,y):
        self.num=numStr
        self.fallSpeed=4
        self.horizontalSpeed=2
        self.color=(100,100,100)
        self.row=row
        self.col=col
        self.x=x
        self.y=y
        self.time=0    
        
    def __repr__(self):
        return ('%s')%(self.num)
        
    def returnstr(self):
        return self.num
    
    def position(self):
        return self.x,self.y
    
    def vanish(self):
        oldR,oldG,oldB=self.color
        vanishInterv=MovingNumber.vanishSpeed-self.time
        newR=oldR-oldR//vanishInterv
        newG=oldG-oldG//vanishInterv
        newB=oldB-oldB//vanishInterv
        self.color=newR,newG,newB
    
    #no idea the target of the movement need to be fixed
    
    def left(self,dis):
        oldX,oldY=self.x,self.y
        newX=oldX-dis
        self.x,self.y=newX,oldY
    
    def right(self,dis):
        oldX,oldY=self.x,self.y
        newX=oldX+dis
        self.x,self.y=newX,oldY
    
    def down(self,dis):
        oldX,oldY=self.x,self.y
        newY=oldY+dis
        self.x,self.y=oldX,newY
    
    def Up(self,dis):
        oldX,oldY=self.x,self.y
        newY=oldY+dis
        self.x,self.y=oldX,newY
    
    # no idea where is the target of the movement need to be fixed
    def swapNumber(self,x,y):
        oldX,oldY=self.x,self.y
        newX,newY=other.x,other.y
        disX=newX-oldX
        intervX=disX/MovingNumber.swapSpeed-self.time
        disY=newY-oldY
        intervY=disY/MovingNumber.swapSpeed-self.time
        oldX=oldX+intervX
        oldY=oldY+intervY
        self.x,self.y=oldX,oldY
    
    '''
    def down(self,row):
    '''
        
'''
class bracket(MovingNumber):
    def __init__(self):
        super().__init__(self)
   '''     
'''
class Input(object):
    def __init__(self):
        self.matrix1=Matrix([[]])
        self.matrix2=Matrix([[]])
    
    def setFirst(self,):
'''        

def initNum(dataNum):
    dataNum.INPUT="INPUT"
    dataNum.INVERSESE='INVERSE'
    dataNum.MULTIPLY='MULMARTIX'
    dataNum.ADD='ADDMATRIX'
    dataNum.OPERATION='OPERATION'
    dataNum.LU='LU'
    dataNum.RANK='RANK'
    dataNum.DETERMINANT='DETERMINANT'
    dataNum.TRANSPOSE='TRANSPOSE'
    dataNum.OUTPUT='output'
    dataNum.mode=dataNum.INPUT
    dataNum.matrixBlockWidth=min(dataNum.height/15,dataNum.width/15)
    dataNum.matrixBlockHeight=dataNum.matrixBlockWidth
    dataNum.matrixBlockDis=dataNum.matrixBlockWidth/5
    dataNum.MATRIX1='1'
    dataNum.matrix1InputRow=0
    dataNum.matrix1InputCol=0
    dataNum.matrix1X=(dataNum.width/2-(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)*(1/2)-
            dataNum.matrixBlockWidth/2)
    dataNum.matrix1Y=(dataNum.height/2-(
            dataNum.matrixBlockHeight+dataNum.matrixBlockDis)*(1/2)-
            dataNum.matrixBlockHeight/2)
    dataNum.MATRIX2='2'
    dataNum.matrix2InputRow=0
    dataNum.matrix2InputCol=0
    dataNum.matrix1=[['_']]
    dataNum.matrix2=[['_']]
    dataNum.matrix2X=(dataNum.width*2/3-(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)*(1/2)-
            dataNum.matrixBlockWidth*2/3)
    dataNum.matrix2Y=(dataNum.height/2-(
            dataNum.matrixBlockHeight+dataNum.matrixBlockDis)*(1/2)-
            dataNum.matrixBlockHeight/2)
    dataNum.inputTime=0
    dataNum.outputTime=0
    dataNum.time=0
    dataNum.mulSpeed=10
    dataNum.multime=0
    dataNum.instructionSpeed=7
    dataNum.addTime=0
    dataNum.mulTime=0
    dataNum.inverseTime=0
    dataNum.instructionTime=7
    dataNum.inputInstructionHeight=30
    dataNum.inputInstruction='Please enter a matrix'
    dataNum.inputInstX,dataNum.inputInstY=dataNum.width/2,dataNum.height/2
    dataNum.operationInstruction='select an operation'
    dataNum.outputInstruction='What is your next operation?'
    initOPERATION(dataNum)
    initADD(dataNum)
    dataNum.output=[[]]
    dataNum.outputX=(dataNum.width/2-(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)*(1/2)-
            dataNum.matrixBlockWidth/2)
    dataNum.outputY=(dataNum.height/2-(
            dataNum.matrixBlockHeight+dataNum.matrixBlockDis)*(1/2)-
            dataNum.matrixBlockHeight/2)
    dataNum.output2=[[]]
    dataNum.OUTPUT2='OUTPUT2'
    
def initADD(dataNum):
    dataNum.addingTime=0
    dataNum.addingSpeed=(dataNum.width/2-dataNum.width/3)/dataNum.freezeTime
    

def initOPERATION(dataNum):
    dataNum.operationTime=0
    dataNum.freezeTime=7
    dataNum.operationMatrix1=[[]]
    dataNum.operationMatrix2=[[]]
    dataNum.leftMargin=dataNum.width/4
    dataNum.bracketLeft=0
    dataNum.bracketTop=0
    dataNum.bracketHeight=0
    dataNum.bracketWidth=0
    dataNum.buttonMul='MULTIPLY'
    dataNum.buttonAdd='ASS'
    dataNum.buttonInverse="INVERSE"
    dataNum.buttonLU='LU'
    dataNum.buttonrank='RANK'
    dataNum.buttondet='DET'
    dataNum.buttontranspose='TRANSPOSE'
    dataNum.buttonXwidth=dataNum.width/10
    dataNum.buttonX=dataNum.width*2/3
    dataNum.buttonYblock=dataNum.height/13
    dataNum.buttonDis=dataNum.buttonYblock*2/7
    dataNum.buttonAllY=dataNum.buttonYblock+dataNum.buttonDis
    dataNum.buttonMargin=dataNum.height*2/13
    dataNum.buttonYM=dataNum.buttonAllY*1+dataNum.buttonMargin
    dataNum.buttonYA=dataNum.buttonAllY*2+dataNum.buttonMargin
    dataNum.buttonYI=dataNum.buttonAllY*3+dataNum.buttonMargin
    dataNum.buttonYL=dataNum.buttonAllY*4+dataNum.buttonMargin
    dataNum.buttonYR=dataNum.buttonAllY*5+dataNum.buttonMargin
    dataNum.buttonYD=dataNum.buttonAllY*6+dataNum.buttonMargin
    dataNum.buttonYT=dataNum.buttonAllY*7+dataNum.buttonMargin
    

def movingMatrix(dataNum,matrixOriginal):
    rows,cols=len(matrixOriginal),len(matrixOriginal[0])
    matrix=copy.deepcopy(matrixOriginal)
    for row in range(rows):
        for col in range(cols):
            x1=(dataNum.matrix1X+col*(
                    dataNum.matrixBlockWidth+dataNum.matrixBlockDis)
                    +dataNum.matrixBlockWidth/2)
            y1=(dataNum.matrix1Y+row*(
            dataNum.matrixBlockHeight+dataNum.matrixBlockDis)
            +dataNum.matrixBlockHeight/2)
            x2=(dataNum.matrix1X+col*(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)+
            dataNum.matrixBlockWidth+dataNum.matrixBlockWidth/2)
            y2=dataNum.matrix1Y+(row*(dataNum.matrixBlockHeight+
            dataNum.matrixBlockDis)+dataNum.matrixBlockHeight+
            dataNum.matrixBlockHeight/2
            )
            cx=(x1+x2)/2
            cy=(y1+y2)/2
            if matrix[row][col]=='_':
                matrix[row][col]='0'
            matrix[row][col]=MovingNumber(matrix[row][col],row,col,cx,cy)
    return matrix
            

def initMatrix(dataNum,MATRIX,newRows,newCols):
    if MATRIX==dataNum.MATRIX1:
        oldRows,oldCols=len(dataNum.matrix1),len(dataNum.matrix1[0])
        if newRows>oldRows:
            diffRows=newRows-oldRows
            dataNum.matrix1+=[['_']*oldCols for row in range(diffRows)]
        elif newRows<oldRows:
            dataNum.matrix1=copy.deepcopy(dataNum.matrix1[:newRows])
        if newCols>oldCols:
            diffCols=newCols-oldCols
            for row in range(len(dataNum.matrix1)):
                dataNum.matrix1[row]+=['_']*diffCols
        elif newCols<oldCols:
            diffCols=oldCols-newCols
            for row in range(len(dataNum.matrix1)):
                dataNum.matrix1[row]=dataNum.matrix1[row][:-diffCols]
        updateMatrixPosition(dataNum,dataNum.MATRIX1)
    elif MATRIX==dataNum.MATRIX2:
        oldRows,oldCols=len(dataNum.matrix2),len(dataNum.matrix2[0])
        if newRows>oldRows:
            diffRows=newRows-oldRows
            dataNum.matrix2+=[['_']*oldCols for row in range(diffRows)]
        elif newRows<oldRows:
            dataNum.matrix2=copy.deepcopy(dataNum.matrix2[:newRows])
        if newCols>oldCols:
            diffCols=newCols-oldCols
            for row in range(len(dataNum.matrix2)):
                dataNum.matrix2[row]+=['_']*diffCols
        elif newCols<oldCols:
            diffCols=oldCols-newCols
            for row in range(len(dataNum.matrix2)):
                dataNum.matrix2[row]=dataNum.matrix2[row][:-diffCols]
        updateMatrixPosition(dataNum,dataNum.MATRIX2)

def mousePressedNum(event,dataNum):
    if dataNum.mode==dataNum.OPERATION:
        operationMousePress(event,dataNum)

def keyPressedNum(event,dataNum):
    if (dataNum.mode==dataNum.INPUT and
                    dataNum.inputTime>=dataNum.instructionTime):
        inputKeyPress(event,dataNum)
    elif  (dataNum.mode==dataNum.OPERATION and
                dataNum.operationTime>=dataNum.freezeTime):
        operationKeyPress(event,dataNum)
    elif dataNum.mode==dataNum.ADD:
            addKeyPress(event,dataNum)
    elif dataNum.mode==dataNum.MULTIPLY:
            multiplyKeyPress(event,dataNum)
    elif dataNum.mode==dataNum.OUTPUT:
            outputKeyPress(event,dataNum)

def outputKeyPress(event,dataNum):
    if event.keysym=='r':
        initNum(dataNum)

def inputKeyPress(event,dataNum):
    if event.keysym=='Return':
        if validInput(dataNum.matrix1):
            rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
            cx,cy=dataNum.width/2,dataNum.height/2
            dataNum.operationMatrix1=operationMatrix(dataNum.matrix1)
            dataNum.matrix1=movingMatrix(dataNum,dataNum.matrix1)
            X1=(dataNum.matrix1X+cols*(
                    dataNum.matrixBlockWidth+dataNum.matrixBlockDis)+
                    dataNum.matrixBlockWidth/2)
            Y1=(dataNum.matrix1Y+rows*(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)
            +dataNum.matrixBlockHeight/2)
            dataNum.bracketLeft=X1
            dataNum.bracketTop=Y1
            dataNum.bracketHeight=(cx-Y1)*2
            dataNum.bracketWidth=(cy-X1)*2
            dataNum.matrix1X,dataNum.matrix1Y=X1,Y1
            print(dataNum.matrix1)
            dataNum.mode=dataNum.OPERATION
        else:
            dataNum.inputTime=0
    if event.keysym.isdigit() or event.keysym=='slash' or event.keysym=='minus':
        key=event.keysym
        if key=='minus':
            insertEntry(dataNum,dataNum.MATRIX1,'-')
        elif key=='slash':
            insertEntry(dataNum,dataNum.MATRIX1,'/')
        else:
            insertEntry(dataNum,dataNum.MATRIX1,key)
    elif event.keysym=='BackSpace':
        deletEntry(dataNum,dataNum.MATRIX1)
    elif event.keysym=='Right':
        dataNum.matrix1InputCol+=1
        if dataNum.matrix1InputCol>=len(dataNum.matrix1[0]):
            newRows,newCols=len(dataNum.matrix1),dataNum.matrix1InputCol+1
            initMatrix(dataNum,dataNum.MATRIX1,newRows,newCols)
    elif event.keysym=='Left':
        if dataNum.matrix1InputCol==0:return
        dataNum.matrix1InputCol-=1
        if not checkRight(dataNum,dataNum.MATRIX1):
            newRows,newCols=len(dataNum.matrix1),dataNum.matrix1InputCol+1
            initMatrix(dataNum,dataNum.MATRIX1,newRows,newCols)
    elif event.keysym=='Up':
        if dataNum.matrix1InputRow==0:return
        dataNum.matrix1InputRow-=1
        if not checkBottom(dataNum,dataNum.MATRIX1):
            newRows,newCols=dataNum.matrix1InputRow+1,len(dataNum.matrix1[0])
            initMatrix(dataNum,dataNum.MATRIX1,newRows,newCols)
    elif event.keysym=='Down':
        dataNum.matrix1InputRow+=1
        if dataNum.matrix1InputRow>=len(dataNum.matrix1):
            newRows,newCols=dataNum.matrix1InputRow+1,len(dataNum.matrix1[0])
            initMatrix(dataNum,dataNum.MATRIX1,newRows,newCols)

def operationKeyPress(eveny,dataNum):
    pass

def operationMousePress(event,dataNum):
    x,y=event.x,event.y
    if (dataNum.buttonX-dataNum.buttonXwidth<=
                    x<=dataNum.buttonX+dataNum.buttonXwidth):
        if (-dataNum.buttonYblock/2+dataNum.buttonYM<=y<=
                    +dataNum.buttonYblock+dataNum.buttonYM):
            dataNum.mode=dataNum.MULTIPLY
        elif (-dataNum.buttonYblock/2+dataNum.buttonYA<=y<=
                    +dataNum.buttonYblock/2+dataNum.buttonYA):
            dataNum.mode=dataNum.ADD
        elif(-dataNum.buttonYblock/2+dataNum.buttonYI<=y<=
                    +dataNum.buttonYblock/2+dataNum.buttonYI):
            dataNum.output=(dataNum.operationMatrix1.inverse().elements())
            print(dataNum.output)
            dataNum.mode=dataNum.OUTPUT
        elif(-dataNum.buttonYblock/2+dataNum.buttonYL<=y<=
                    +dataNum.buttonYblock/2+dataNum.buttonYL):
            dataNum.output2=(dataNum.operationMatrix1.decomp())
            dataNum.mode=dataNum.OUTPUT2
        elif(-dataNum.buttonYblock/2+dataNum.buttonYR<=y<=
                    +dataNum.buttonYblock/2+dataNum.buttonYR):
            dataNum.output=(dataNum.operationMatrix1.rank())
            dataNum.mode=dataNum.OUTPUT
        elif(-dataNum.buttonYblock/2+dataNum.buttonYD<=y<=
                    +dataNum.buttonYblock/2+dataNum.buttonYD):
            dataNum.output=(dataNum.operationMatrix1.det())
            dataNum.mode=dataNum.OUTPUT
        elif (-dataNum.buttonYblock/2+dataNum.buttonYT<=y<=
                    +dataNum.buttonYblock/2+dataNum.buttonYT):
            dataNum.output=(dataNum.operationMatrix1.transpose().elements())
            dataNum.mode=dataNum.OUTPUT


def addKeyPress(event,dataNum):
    if event.keysym=='Return':
        if validInput(dataNum.matrix2):
            rows,cols=len(dataNum.matrix2),len(dataNum.matrix2[0])
            cx,cy=dataNum.width/2,dataNum.height/2
            dataNum.operationMatrix2=operationMatrix(dataNum.matrix2)
            dataNum.matrix2=movingMatrix(dataNum,dataNum.matrix2)
            print(dataNum.matrix2)
            X2=(dataNum.matrix2X+cols*(
                    dataNum.matrixBlockWidth+dataNum.matrixBlockDis)+
                    dataNum.matrixBlockWidth/2)
            Y2=(dataNum.matrix2Y+rows*(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)
            +dataNum.matrixBlockHeight/2)
            dataNum.bracketLeft=X2
            dataNum.bracketTop=Y2
            dataNum.bracketHeight=(cx-Y2)*2
            dataNum.bracketWidth=(cy-X2)*2
            dataNum.matrix2X,dataNum.matrix2Y=X2,Y2
            dataNum.output=(
                        dataNum.operationMatrix1.add(dataNum.operationMatrix2)
                        .elements())
            print(dataNum.output)
            dataNum.mode=dataNum.OUTPUT
        else:
            dataNum.inputTime=0
    if event.keysym.isdigit() or event.keysym=='slash' or event.keysym=='minus':
        key=event.keysym
        if key=='minus':
            insertEntry(dataNum,dataNum.MATRIX2,'-')
        elif key=='slash':
            insertEntry(dataNum,dataNum.MATRIX2,'/')
        else:
            insertEntry(dataNum,dataNum.MATRIX2,key)
    elif event.keysym=='BackSpace':
        deletEntry(dataNum,dataNum.MATRIX2)
    elif event.keysym=='Right':
        dataNum.matrix2InputCol+=1
        if dataNum.matrix2InputCol>=len(dataNum.matrix2[0]):
            newRows,newCols=len(dataNum.matrix2),dataNum.matrix2InputCol+1
            initMatrix(dataNum,dataNum.MATRIX2,newRows,newCols)
    elif event.keysym=='Left':
        if dataNum.matrix2InputCol==0:return
        dataNum.matrix2InputCol-=1
        if not checkRight(dataNum,dataNum.MATRIX2):
            newRows,newCols=len(dataNum.matrix2),dataNum.matrix2InputCol+1
            initMatrix(dataNum,dataNum.MATRIX2,newRows,newCols)
    elif event.keysym=='Up':
        if dataNum.matrix2InputRow==0:return
        dataNum.matrix2InputRow-=1
        if not checkBottom(dataNum,dataNum.MATRIX2):
            newRows,newCols=dataNum.matrix2InputRow+1,len(dataNum.matrix2[0])
            initMatrix(dataNum,dataNum.MATRIX2,newRows,newCols)
    elif event.keysym=='Down':
        dataNum.matrix2InputRow+=1
        if dataNum.matrix2InputRow>=len(dataNum.matrix1):
            newRows,newCols=dataNum.matrix2InputRow+1,len(dataNum.matrix2[0])
            initMatrix(dataNum,dataNum.MATRIX2,newRows,newCols)

def multiplyKeyPress(event,dataNum):
    if event.keysym=='Return':
        if validInput(dataNum.matrix2):
            rows,cols=len(dataNum.matrix2),len(dataNum.matrix2[0])
            cx,cy=dataNum.width/2,dataNum.height/2
            dataNum.operationMatrix2=operationMatrix(dataNum.matrix2)
            dataNum.matrix2=movingMatrix(dataNum,dataNum.matrix2)
            print(dataNum.matrix2)
            X2=(dataNum.matrix2X+cols*(
                    dataNum.matrixBlockWidth+dataNum.matrixBlockDis)+
                    dataNum.matrixBlockWidth/2)
            Y2=(dataNum.matrix2Y+rows*(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)
            +dataNum.matrixBlockHeight/2)
            dataNum.bracketLeft=X2
            dataNum.bracketTop=Y2
            dataNum.bracketHeight=(cx-Y2)*2
            dataNum.bracketWidth=(cy-X2)*2
            dataNum.matrix2X,dataNum.matrix2Y=X2,Y2
            dataNum.output=(
                        dataNum.operationMatrix1.mul(dataNum.operationMatrix2)
                        .elements())
            print(dataNum.output)
            dataNum.mode=dataNum.OUTPUT
        else:
            dataNum.inputTime=0
    if event.keysym.isdigit() or event.keysym=='slash' or event.keysym=='minus':
        key=event.keysym
        if key=='minus':
            insertEntry(dataNum,dataNum.MATRIX2,'-')
        elif key=='slash':
            insertEntry(dataNum,dataNum.MATRIX2,'/')
        else:
            insertEntry(dataNum,dataNum.MATRIX2,key)
    elif event.keysym=='BackSpace':
        deletEntry(dataNum,dataNum.MATRIX2)
    elif event.keysym=='Right':
        dataNum.matrix2InputCol+=1
        if dataNum.matrix2InputCol>=len(dataNum.matrix2[0]):
            newRows,newCols=len(dataNum.matrix2),dataNum.matrix2InputCol+1
            initMatrix(dataNum,dataNum.MATRIX2,newRows,newCols)
    elif event.keysym=='Left':
        if dataNum.matrix2InputCol==0:return
        dataNum.matrix2InputCol-=1
        if not checkRight(dataNum,dataNum.MATRIX2):
            newRows,newCols=len(dataNum.matrix2),dataNum.matrix2InputCol+1
            initMatrix(dataNum,dataNum.MATRIX2,newRows,newCols)
    elif event.keysym=='Up':
        if dataNum.matrix2InputRow==0:return
        dataNum.matrix2InputRow-=1
        if not checkBottom(dataNum,dataNum.MATRIX2):
            newRows,newCols=dataNum.matrix2InputRow+1,len(dataNum.matrix2[0])
            initMatrix(dataNum,dataNum.MATRIX2,newRows,newCols)
    elif event.keysym=='Down':
        dataNum.matrix2InputRow+=1
        if dataNum.matrix2InputRow>=len(dataNum.matrix1):
            newRows,newCols=dataNum.matrix2InputRow+1,len(dataNum.matrix2[0])
            initMatrix(dataNum,dataNum.MATRIX2,newRows,newCols)

def updateMatrixPosition(dataNum,MATRIX):
    if MATRIX==dataNum.MATRIX1:
        newRows,newCols=len(dataNum.matrix1),len(dataNum.matrix1[0])
        dataNum.matrix1X=(dataNum.width/2-(
                dataNum.matrixBlockWidth+dataNum.matrixBlockDis)*(newCols/2)-
                dataNum.matrixBlockWidth/2)
        dataNum.matrix1Y=(dataNum.height/2-(
                dataNum.matrixBlockHeight+dataNum.matrixBlockDis)*(newRows/2)-
                dataNum.matrixBlockHeight/2)
    elif MATRIX==dataNum.MATRIX2:
        newRows,newCols=len(dataNum.matrix2),len(dataNum.matrix2[0])
        dataNum.matrix2X=(dataNum.width*2/3-(
                dataNum.matrixBlockWidth+dataNum.matrixBlockDis)*(newCols/2)-
                dataNum.matrixBlockWidth/2)
        dataNum.matrix2Y=(dataNum.height/2-(
                dataNum.matrixBlockHeight+dataNum.matrixBlockDis)*(newRows/2)-
                dataNum.matrixBlockHeight/2)



def insertEntry(dataNum,MATRIX,digitString):
    if MATRIX==dataNum.MATRIX1:
        row,col=dataNum.matrix1InputRow,dataNum.matrix1InputCol
        if dataNum.matrix1[row][col]=='_':
            dataNum.matrix1[row][col]=digitString
        else:
            dataNum.matrix1[row][col]+=digitString
    elif MATRIX==dataNum.MATRIX2:
        row,col=dataNum.matrix2InputRow,dataNum.matrix2InputCol
        if dataNum.matrix2[row][col]=='_':
            dataNum.matrix2[row][col]=digitString
        else:
            dataNum.matrix2[row][col]+=digitString


def deletEntry(dataNum,MATRIX):
    if MATRIX==dataNum.MATRIX1:
        row,col=dataNum.matrix1InputRow,dataNum.matrix1InputCol
        if dataNum.matrix1[row][col]=='_':
            return
        elif len(dataNum.matrix1[row][col])==1:
            dataNum.matrix1[row][col]='_'
        else:
            dataNum.matrix1[row][col]=dataNum.matrix1[row][col][:-1]
    else:
        row,col=dataNum.matrix2InputRow,dataNum.matrix2InputCol
        if dataNum.matrix2[row][col]=='_':
            return
        elif len(dataNum.matrix2[row][col])==1:
            dataNum.matrix1[row][col]='_'
        else:
            dataNum.matrix2[row][col]=dataNum.matrix2[row][col][:-1]          
 
def operationMatrix(matrixOriginal):
    rows,cols=len(matrixOriginal),len(matrixOriginal[0])
    matrix=copy.deepcopy(matrixOriginal)
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col]=='_':
                matrix[row][col]=0
            elif matrix[row][col].startswith('-'):
                matrix[row][col]=-int(matrix[row][col][1:])
            else:
                matrix[row][col]=matrix[row][col]
    return Matrix(matrix)
    
          
def validInput(matrix):
    rows,cols=len(matrix),len(matrix[0])
    flagHasNumber=False
    flagValidInput=True
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col]!='_':
                flagHasNumber=True
            elif '-' in matrix[row][col]:
                if (matrix[row][col].count('-')>1 or 
                            not matrix[row][col].startswith('-')):
                    flagValidInput=False
    return flagHasNumber and flagValidInput

def checkBottom(dataNum,MATRIX):
    if MATRIX==dataNum.MATRIX1:
        rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
        flag=False
        for col in range(cols):
            if dataNum.matrix1[rows-1][col]!='_':
                flag=True
        return flag
    elif MATRIX==dataNum.MATRIX2:
        rows,cols=len(dataNum.matrix2),len(dataNum.matrix2[0])
        flag=False
        for col in range(cols):
            if dataNum.matrix2[rows-1][col]!='_':
                flag=True
        return flag

def checkRight(dataNum,MATRIX):
    if MATRIX==dataNum.MATRIX1:
        rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
        flag=False
        for row in range(rows):
            if dataNum.matrix1[row][cols-1]!='_':
                flag=True
        return flag
    elif MATRIX==dataNum.MATRIX2:
        rows,cols=len(dataNum.matrix2),len(dataNum.matrix2[0])
        flag=False
        for row in range(rows):
            if dataNum.matrix2[row][cols-1]!='_':
                flag=True
        return flag

def timerFiredNum(canvas,dataNum):
    if dataNum.mode==dataNum.INPUT:
        if dataNum.inputTime<dataNum.instructionTime:
            moveInstruction(dataNum)
            dataNum.inputTime+=1
            dataNum.time+=1
    elif dataNum.mode==dataNum.OPERATION:
        if dataNum.operationTime<dataNum.freezeTime:
            vanishInstruction(dataNum)
            moveLeftMatrix1(dataNum)
            dataNum.operationTime+=1
            dataNum.time+=1
    elif dataNum.mode==dataNum.ADD:
        if dataNum.inputTime<dataNum.instructionTime:
            moveInstruction(dataNum)
            dataNum.inputTime+=1
            dataNum.time+=1
    elif dataNum.mode==dataNum.OUTPUT:
        return
    elif dataNum.mode==dataNum.OUTPUT2:
        return
    

def moveLeftMatrix1(dataNum):
    interv=dataNum.freezeTime-dataNum.operationTime
    left=dataNum.matrix1[0][0].x-dataNum.matrixBlockWidth/2
    dis=(-dataNum.leftMargin+left)/interv
    rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
    dataNum.matrix1X-=dis
    for row in range(rows):
        for col in range(cols):
            dataNum.matrix1[row][col].left(dis)

def moveInstruction(dataNum):
    target=dataNum.height/8
    interv=(target-dataNum.inputInstY)/(
                                    dataNum.instructionSpeed-dataNum.inputTime)
    dataNum.inputInstY+=interv
    
def vanishInstruction(dataNum):
    pass

def redrawAllNum(canvas,dataNum):
    if dataNum.mode==dataNum.INPUT:
        drawInput(canvas,dataNum)
    elif dataNum.mode==dataNum.OPERATION:
        drawOperation(canvas,dataNum)
    elif dataNum.mode==dataNum.ADD:
        drawAdd(canvas,dataNum)
    elif dataNum.mode==dataNum.OUTPUT:
        drawOutput(canvas,dataNum)
    elif dataNum.mode==dataNum.OUTPUT2:
        index=0
        for stuff in dataNum.output2:
            index+=1
            dataNum.output=stuff
            drawOutput(canvas,dataNum,index)
    elif dataNum.mode==dataNum.MULTIPLY:
        drawMultiply(canvas,dataNum)
            

def drawOperation(canvas,dataNum):
    rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
    X1=dataNum.matrix1X
    Y1=dataNum.matrix1Y
    cx,cy=(X1+dataNum.bracketWidth/2,Y1+dataNum.bracketHeight/2)
    r=((X1-cx)**2+(Y1-cy)**2)**0.5
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=120,extent=120,style='arc',outline='grey')
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=-60,extent=120,style='arc',outline='grey')
    canvas.create_text(dataNum.buttonX,dataNum.buttonYM,text='Multiply',
                        fill='grey')
    canvas.create_text(dataNum.buttonX,dataNum.buttonYA,text='Add',
                        fill='grey')
    canvas.create_text(dataNum.buttonX,dataNum.buttonYI,text='Inverse',
                        fill='grey')
    canvas.create_text(dataNum.buttonX,dataNum.buttonYL,text='LUdecomposition',
                        fill='grey')
    canvas.create_text(dataNum.buttonX,dataNum.buttonYR,text='rank',
                        fill='grey')
    canvas.create_text(dataNum.buttonX,dataNum.buttonYD,text='determinant',
                        fill='grey')
    canvas.create_text(dataNum.buttonX,dataNum.buttonYT,text='transpose',
                        fill='grey')
    for row in range(rows):
        for col in range(cols):
            num=dataNum.matrix1[row][col].returnstr()
            x,y=dataNum.matrix1[row][col].position()
            size=str(int(dataNum.matrixBlockWidth*2/5))
            canvas.create_text(x,y,text=num,font='Helvetica '+size,fill='grey')
    
    

def drawInput(canvas,dataNum):
    rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
    canvas.create_text(dataNum.inputInstX,dataNum.inputInstY,
            text=dataNum.inputInstruction,fill='grey',
                                    font='Helvetica 30 bold')
    X1=(dataNum.matrix1X+cols*(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)+
            dataNum.matrixBlockWidth/2)
    Y1=(dataNum.matrix1Y+rows*(
    dataNum.matrixBlockWidth+dataNum.matrixBlockDis)
    +dataNum.matrixBlockHeight/2)
    cx,cy=dataNum.width/2,dataNum.height/2
    r=((X1-cx)**2+(Y1-cy)**2)**0.5
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=120,extent=120,style='arc')
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=-60,extent=120,style='arc')
    for row in range(rows):
        for col in range(cols):
            x1=(dataNum.matrix1X+col*(
                    dataNum.matrixBlockWidth+dataNum.matrixBlockDis)
                    +dataNum.matrixBlockWidth/2)
            y1=(dataNum.matrix1Y+row*(
            dataNum.matrixBlockHeight+dataNum.matrixBlockDis)
            +dataNum.matrixBlockHeight/2)
            x2=(dataNum.matrix1X+col*(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)+
            dataNum.matrixBlockWidth+dataNum.matrixBlockWidth/2)
            y2=dataNum.matrix1Y+(row*(dataNum.matrixBlockHeight+
            dataNum.matrixBlockDis)+dataNum.matrixBlockHeight+
            dataNum.matrixBlockHeight/2
            )
            cx=(x1+x2)/2
            cy=(y1+y2)/2
            size=str(int(dataNum.matrixBlockWidth*2/5))
            number=dataNum.matrix1[row][col]
            if (dataNum.matrix1InputRow==row and 
                dataNum.matrix1InputCol==col):
                canvas.create_rectangle(x1,y1,x2,y2,outline='black')
                if number=='_':
                    continue
                canvas.create_text(cx,
                        cy,text=number,fill='black',font='helvetica '+size)
            else:
                canvas.create_rectangle(x1,y1,x2,y2,outline='grey')
                if number=='_':
                    continue
                canvas.create_text(cx,cy,text=number,
                                    fill='grey',font='helvetica '+size)

def drawMultiply(canvas,dataNum):
    rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
    drawFirst(canvas,dataNum)
    cx,cy=dataNum.width/2,dataNum.height/2
    canvas.create_text(cx,cy,text='x',fill='darkgrey',font='helvetica 32')
    drawSecond(canvas,dataNum)


def drawAdd(canvas,dataNum):
    rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
    drawFirst(canvas,dataNum)
    cx,cy=dataNum.width/2,dataNum.height/2
    canvas.create_text(cx,cy,text='+',fill='darkgrey',font='helvetica 32')
    drawSecond(canvas,dataNum)

def drawAddAnimation(canvas,dataNum):
    if data.addingTime<dataNum.freezeTime:
        rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
        drawAnimation1(canvas,dataNum)
        drawAnimation2(canvas,dataNum)
    else:
        drawOutput(canvas,dataNum)

def drawOutput(canvas,dataNum,index=0):
    canvas.create_text(dataNum.width/2,dataNum.height/10,
                                text='Press r to reset',fill='grey',
                            font='helvetica 30')
    if index==0:
        if type(dataNum.output)==type(None):
            canvas.create_text(dataNum.width/2,dataNum.height/2,
                                text='None',fill='grey',
                            font='helvetica 30')
        if isinstance(dataNum.output,int):
            canvas.create_text(dataNum.width/2,dataNum.height/2,
                            text=str(dataNum.output),fill='grey',
                            font='helvetica 30')
        elif isinstance(dataNum.output,Rational):
            canvas.create_text(dataNum.width/2,dataNum.height/2,
                            text=str(dataNum.output),fill='grey',
                            font='helvetica 30')
        else:
            rows,cols=len(dataNum.output),len(dataNum.output[0])
            X1=(dataNum.outputX+cols*(
                    dataNum.matrixBlockWidth+dataNum.matrixBlockDis)+
                    dataNum.matrixBlockWidth/2)
            Y1=(dataNum.outputY+rows*(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)
            +dataNum.matrixBlockHeight/2)
            cx,cy=dataNum.width/2,dataNum.height/2
            r=((X1-cx)**2+(Y1-cy)**2)**0.5
            canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
            start=120,extent=120,style='arc')
            canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
            start=-60,extent=120,style='arc')
            for row in range(rows):
                for col in range(cols):
                    x1=(dataNum.outputX+col*(
                            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)
                            +dataNum.matrixBlockWidth/2)
                    y1=(dataNum.outputY+row*(
                    dataNum.matrixBlockHeight+dataNum.matrixBlockDis)
                    +dataNum.matrixBlockHeight/2)
                    x2=(dataNum.outputX+col*(
                    dataNum.matrixBlockWidth+dataNum.matrixBlockDis)+
                    dataNum.matrixBlockWidth+dataNum.matrixBlockWidth/2)
                    y2=dataNum.outputY+(row*(dataNum.matrixBlockHeight+
                    dataNum.matrixBlockDis)+dataNum.matrixBlockHeight+
                    dataNum.matrixBlockHeight/2
                    )
                    cx=(x1+x2)/2
                    cy=(y1+y2)/2
                    size=str(int(dataNum.matrixBlockWidth*2/5))
                    number=dataNum.output[row][col]
                    canvas.create_rectangle(x1,y1,x2,y2,outline='grey')
                    if number=='_':
                        continue
                    canvas.create_text(cx,cy,text=number,
                                        fill='grey',font='helvetica '+size)
    else:
        x=dataNum.width/6*index
        if type(dataNum.output)==type(None):
            canvas.create_text(dataNum.width/2,dataNum.height/2,color='grey',
                            font='helvetica 30')
        else:
            rows,cols=len(dataNum.output),len(dataNum.output[0])
            X1=x
            Y1=dataNum.matrix1Y
            cx,cy=(X1+dataNum.bracketWidth/2,Y1+dataNum.bracketHeight/2)
            r=((X1-cx)**2+(Y1-cy)**2)**0.5
            canvas.create_arc(x-r,cy-6*r/5,cx+r,cy+6*r/5,
            start=120,extent=120,style='arc',outline='grey')
            canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
            start=-60,extent=120,style='arc',outline='grey')
            for row in range(rows):
                for col in range(cols):
                    x1=(x+col*(
                            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)
                            +dataNum.matrixBlockWidth/2)
                    y1=(dataNum.outputY+row*(
                    dataNum.matrixBlockHeight+dataNum.matrixBlockDis)
                    +dataNum.matrixBlockHeight/2)
                    x2=(x+col*(
                    dataNum.matrixBlockWidth+dataNum.matrixBlockDis)+
                    dataNum.matrixBlockWidth+dataNum.matrixBlockWidth/2)
                    y2=dataNum.outputY+(row*(dataNum.matrixBlockHeight+
                    dataNum.matrixBlockDis)+dataNum.matrixBlockHeight+
                    dataNum.matrixBlockHeight/2
                    )
                    cx=(x1+x2)/2
                    cy=(y1+y2)/2
                    size=str(int(dataNum.matrixBlockWidth*2/5))
                    number=dataNum.output[row][col]
                    canvas.create_rectangle(x1,y1,x2,y2,outline='grey')
                    if number=='_':
                        continue
                    canvas.create_text(cx,cy,text=number,
                                        fill='grey',font='helvetica '+size)
    


def drawFirst(canvas,dataNum):
    rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
    X1=dataNum.matrix1X
    Y1=dataNum.matrix1Y
    cx,cy=(X1+dataNum.bracketWidth/2,Y1+dataNum.bracketHeight/2)
    r=((X1-cx)**2+(Y1-cy)**2)**0.5
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=120,extent=120,style='arc',outline='grey')
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=-60,extent=120,style='arc',outline='grey')
    for row in range(rows):
        for col in range(cols):
            num=dataNum.matrix1[row][col].returnstr()
            x,y=dataNum.matrix1[row][col].position()
            size=str(int(dataNum.matrixBlockWidth*2/5))
            canvas.create_text(x,y,text=num,font='Helvetica '+size,fill='grey')


def drawAnimation1(canvas,dataNum):
    rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
    X1=dataNum.matrix1X
    Y1=dataNum.matrix1Y
    '''
    cx,cy=(X1+dataNum.bracketWidth/2,Y1+dataNum.bracketHeight/2)
    r=((X1-cx)**2+(Y1-cy)**2)**0.5
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=120,extent=120,style='arc',outline='grey')
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=-60,extent=120,style='arc',outline='grey')
    '''
    for row in range(rows):
        for col in range(cols):
            num=dataNum.matrix1[row][col].returnstr()
            x,y=dataNum.matrix1[row][col].position()
            size=str(int(dataNum.matrixBlockWidth*2/5))
            canvas.create_text(x,y,text=num,font='Helvetica '+size,fill='grey')

def drawAnimation2(canvas,dataNum):
    rows,cols=len(dataNum.matrix1),len(dataNum.matrix1[0])
    X1=dataNum.matrix2X
    Y1=dataNum.matrix2Y
    '''
    cx,cy=(X2+dataNum.bracketWidth/2,Y2+dataNum.bracketHeight/2)
    r=((X2-cx)**2+(Y1-cy)**2)**0.5
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=120,extent=120,style='arc',outline='grey')
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=-60,extent=120,style='arc',outline='grey')
    '''
    for row in range(rows):
        for col in range(cols):
            num=dataNum.matrix2[row][col].returnstr()
            x,y=dataNum.matrix2[row][col].position()
            size=str(int(dataNum.matrixBlockWidth*2/5))
            canvas.create_text(x,y,text=num,font='Helvetica '+size,fill='grey')

def drawSecond(canvas,dataNum):
    rows,cols=len(dataNum.matrix2),len(dataNum.matrix2[0])
    canvas.create_text(dataNum.inputInstX,dataNum.inputInstY,
            text=dataNum.inputInstruction,fill='grey',
                                    font='Helvetica 30 bold')
    X1=(dataNum.matrix2X+cols*(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)+
            dataNum.matrixBlockWidth/2)
    Y1=(dataNum.matrix2Y+rows*(
    dataNum.matrixBlockWidth+dataNum.matrixBlockDis)
    +dataNum.matrixBlockHeight/2)
    cx,cy=dataNum.width*2/3,dataNum.height/2
    r=((X1-cx)**2+(Y1-cy)**2)**0.5
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=120,extent=120,style='arc')
    canvas.create_arc(cx-r,cy-6*r/5,cx+r,cy+6*r/5,
    start=-60,extent=120,style='arc')
    for row in range(rows):
        for col in range(cols):
            x1=(dataNum.matrix2X+col*(
                    dataNum.matrixBlockWidth+dataNum.matrixBlockDis)
                    +dataNum.matrixBlockWidth/2)+10
            y1=(dataNum.matrix2Y+row*(
            dataNum.matrixBlockHeight+dataNum.matrixBlockDis)
            +dataNum.matrixBlockHeight/2)
            x2=(dataNum.matrix2X+col*(
            dataNum.matrixBlockWidth+dataNum.matrixBlockDis)+
            dataNum.matrixBlockWidth+dataNum.matrixBlockWidth/2)+10
            y2=dataNum.matrix2Y+(row*(dataNum.matrixBlockHeight+
            dataNum.matrixBlockDis)+dataNum.matrixBlockHeight+
            dataNum.matrixBlockHeight/2
            )
            cx=(x1+x2)/2
            cy=(y1+y2)/2
            size=str(int(dataNum.matrixBlockWidth*2/5))
            number=dataNum.matrix2[row][col]
            if (dataNum.matrix2InputRow==row and 
                dataNum.matrix2InputCol==col):
                canvas.create_rectangle(x1,y1,x2,y2,outline='black')
                if number=='_':
                    continue
                canvas.create_text(cx,
                        cy,text=number,fill='black',font='helvetica '+size)
            else:
                canvas.create_rectangle(x1,y1,x2,y2,outline='grey')
                if number=='_':
                    continue
                canvas.create_text(cx,cy,text=number,
                                    fill='grey',font='helvetica '+size)
    

def goMatrix(width=600, height=600):
    def redrawAllWrapper(canvas, dataNum):
        canvas.delete(ALL)
        redrawAllNum(canvas, dataNum)
        canvas.update()    

    def mousePressedWrapper(event, canvas, dataNum):
        mousePressedNum(event, dataNum)
        redrawAllWrapper(canvas, dataNum)

    def keyPressedWrapper(event, canvas, dataNum):
        keyPressedNum(event, dataNum)
        redrawAllWrapper(canvas, dataNum)

    def timerFiredWrapper(canvas, dataNum):
        timerFiredNum(canvas,dataNum)
        redrawAllWrapper(canvas, dataNum)
        # pause, then call timerFired again
        canvas.after(dataNum.timerDelay, timerFiredWrapper, canvas, dataNum)
    # Set up dataNum and call init
    class Struct(object): pass
    dataNum = Struct()
    dataNum.width = width
    dataNum.height = width # so grid is width x width
    dataNum.fullHeight = height
    dataNum.timerDelay = 50 # milliseconds
    initNum(dataNum)
    # create the root and the canvas
    root = Toplevel()
    dataNum.root = root # for showMessageBox parent
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, dataNum))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, dataNum))
    timerFiredWrapper(canvas, dataNum)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

def runMatrix():
        goMatrix()
