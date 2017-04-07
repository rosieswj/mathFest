import os
import sys
import random
import imghdr
from pygame import *

firstClickProtector = []
cellStatus = []
answers =[]

def f():

        init()
        board=Surface((520,520))
        board.fill(-1)
        height,width=board.get_size()
        rowNumber=25
        colNumber=15
        mineNumber=50
        safeCell=rowNumber*colNumber-mineNumber
        gridLength=26
        playBoard=display.set_mode((rowNumber*gridLength,colNumber*gridLength),0,32)
        playBoard.blit(board,(-(height-rowNumber*26)//2,-(width-colNumber*26)//2))
        board=playBoard.copy()
        police=font.Font(font.get_default_font(),gridLength)
        police0=font.Font(font.get_default_font(),gridLength+2)
        blankCell=Surface((gridLength,gridLength))
        blankCell.fill(transform.average_color(board)[:-1])
        blankCell.fill(-1,(0,0,gridLength-1,gridLength-1))
        imageOfCell=[blankCell]+[blankCell.copy()for i in range(8)]
        imageOfFail=image.load('zhadan.png')
        imageOfMine=image.load('mine.png')
        imageOfFlag=image.load('hehe.gif')
        imageOfClickedCell=image.load('1111.png')
        imageOfHint=image.load('haha.png')
        display.set_icon(imageOfMine)
        temp=[]
        flags=[]
        rowNumber+=2;
        outerSize=rowNumber*(colNumber+2)
        cases=[playBoard.blit(imageOfClickedCell,((x%rowNumber)*gridLength,(x//rowNumber)*gridLength)) for x in range(-rowNumber-1,outerSize)]	
        display.flip()
        timeCount=0
        firstClick = True
        time.set_timer(USEREVENT,1000)
        i=0

        for index1 in range(1,9):	
                fill=police.render(str(index1),1,(index1%2*124,index1%8*31,index1%4*62))
                frameWork=fill.get_rect()
                frameWork.center=(gridLength-1)//2,(gridLength-1)//2
                imageOfCell[index1].blit(fill,frameWork.topleft)
#########################################
        def createBoard(cell):
                global firstClickProtector
                global cellStatus
                global answers
                firstClickProtector=sum([list(range(x,rowNumber-2+x))for x in range(rowNumber+1,outerSize-rowNumber-1,rowNumber)],[])
                cellStatus=["Empty"] * outerSize
                for i in firstClickProtector:
                        cellStatus[i]=0
                restMineNumber = mineNumber
                while restMineNumber > 0:
                        index2=firstClickProtector.pop(firstClickProtector.index(random.choice(firstClickProtector)));
                        if cell == index2:
                                continue
                        cellStatus[index2]="Mine"
                        for direction1 in (-1,1,-rowNumber-1,-rowNumber,-rowNumber+1,rowNumber+1,rowNumber,rowNumber-1):
                                try:
                                        cellStatus[index2+direction1]+=1
                                except:
                                        pass
                        restMineNumber-=1

                for i in range(len(cellStatus)):
                        if cellStatus[i] != "Empty":
                                answers.append(cellStatus[i])
                        else:
                                answers.append("Hint")
############################

        def unclickedCellNumber(current,position2):
                count = 0
                for direction2 in (-1,1,-rowNumber-1,-rowNumber,-rowNumber+1,rowNumber+1,rowNumber,rowNumber-1):
                        newPosition = position2+direction2
                        if answers[newPosition] == "Hint":
                                continue
                        if current[newPosition] != "Empty" and newPosition not in flags:
                                count += 1
                return count
##################
        def getHint(current, answers):
                findedeHint = []
                for position3 in range(len(current)):
                        if answers[i] == "Hint":
                                continue
                        if current[position3] == "Empty":
                                if answers[position3] == 0:
                                        continue			
                                if unclickedCellNumber(current, position3) == answers[position3]:
                                        for direction3 in (-1,1,-rowNumber-1,-rowNumber,-rowNumber+1,rowNumber+1,rowNumber,rowNumber-1):
                                                newPosition = position3+direction3
                                                if answers[newPosition] == "Hint":
                                                        continue
                                                if current[newPosition] != "Empty" and newPosition not in flags:
                                                        findedeHint.append(newPosition)
                                        return findedeHint
                return findedeHint
########################


        while True:
                playEvent=event.wait()
                if playEvent.type==MOUSEBUTTONDOWN:
                        press=Rect((mouse.get_pos()),(1,1)).collidelist(cases)
                        if firstClick:
                                createBoard(press)
                                firstClick = False
                        if playEvent.button==1:			
                                if cellStatus[press]=="Mine":
                                        for i in range(outerSize):
                                                if cellStatus[i]=="Mine":
                                                        playBoard.blit(imageOfFail,cases[i])
                                                elif cellStatus[i]!="Empty":
                                                        playBoard.blit(imageOfCell[cellStatus[i]],cases[i])
                                        break

                                elif cellStatus[press]!="Empty":
                                        if cellStatus[press]==0:
                                                temp.append(press)
                                                playBoard.blit(board,cases[press].topleft,cases[press])
                                                playBoard.blit(imageOfCell[0],cases[press].topleft)
                                                cellStatus[press]="Empty";
                                                safeCell-=1
                                                while temp:
                                                        i=temp.pop()
                                                        for direction4 in (-1,1,-rowNumber-1,-rowNumber,-rowNumber+1,rowNumber+1,rowNumber,rowNumber-1):
                                                                if cellStatus[i+direction4]==0:
                                                                        temp.append(i+direction4)
                                                                if cellStatus[i+direction4]!="Empty":
                                                                        playBoard.blit(board,cases[i+direction4].topleft,cases[i+direction4])
                                                                        playBoard.blit(imageOfCell[cellStatus[i+direction4]],cases[i+direction4].topleft);
                                                                        cellStatus[i+direction4]="Empty";
                                                                        safeCell-=1
                                        else:
                                                playBoard.blit(board,cases[press].topleft,cases[press])
                                                playBoard.blit(imageOfCell[cellStatus[press]],cases[press].topleft);
                                                cellStatus[press]="Empty";
                                                safeCell-=1

                                        if not safeCell:
                                                for i in range(outerSize):
                                                        if cellStatus[i]=="Mine":
                                                                playBoard.blit(imageOfMine,cases[i])
                                                break

                        elif playEvent.button==3 and cellStatus[press]!="Empty":
                                if press not in flags:				
                                        playBoard.blit(imageOfFlag,cases[press])
                                        flags.append(press)
                                else:
                                        playBoard.blit(board,cases[press].topleft,cases[press]);
                                        playBoard.blit(imageOfClickedCell,cases[press].topleft)
                                        flags.remove(press)
                        display.flip()

                elif playEvent.type == KEYDOWN and playEvent.key == K_h:		
                        findedeHint = getHint(cellStatus, answers)
                        for press2 in findedeHint:
                                playBoard.blit(board,cases[press2].topleft,cases[press2]);
                                playBoard.blit(imageOfHint,cases[press2].topleft)
                        display.flip()


                elif playEvent.type==USEREVENT:
                        timeCount+=1
                        display.set_caption(str(timeCount//3600).zfill(2)+':'+str(timeCount//60%60).zfill(2)+':'+str(timeCount%60).zfill(2)+'  Go HashBrown! Press h for hint!')


                if playEvent.type==QUIT:
                        event.post(event.Event(QUIT))
                        break

        display.flip()
        while event.wait().type!=QUIT:
                pass
