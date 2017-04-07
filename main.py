from tkinter import *
import random
import new_solver
import minesweeper_hashbrown
import matrixCalc

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def makeRandList(n):
    result=[]
    for i in range(n):
        result.append(str(random.randint(0,9)))
    return result
        
def init5(data5):
    data5.mode="start"
    data5.numberList=makeRandList(100)

def mousePressed5(event, data5):
    if data5.mode=="start":
        data5.mode="menu"
    elif data5.mode=="menu":
        if event.x>220 and event.x<400 and event.y>80 and event.y<260:
            new_solver.runPlay24()
        elif event.x>60 and event.x<240 and event.y>300 and event.y<480:
            matrixCalc.runMatrix()
        elif event.x>360 and event.x<540 and event.y>300 and event.y<480:
            minesweeper_hashbrown.f()
            
            
        
        
        
        

def keyPressed5(event, data5):
    pass


def timerFired5(data5):
    if data5.mode=="start":
        init5(data5)

def inits5(canvas):
    backGround=PhotoImage(file="hash2.gif")
    canvas.data5["backGround"]=backGround
    backGround2=PhotoImage(file="menu.gif")
    canvas.data5["backGround2"]=backGround2

def draw112(canvas,data5):
    image2=canvas.data5["backGround2"]
    imageSize=(image2.width(),image2.height())
    canvas.create_image(0,0,anchor=NW, image=image2)

def draw0(canvas,data5):
    image=canvas.data5["backGround"]
    imageSize=(image.width(),image.height())
    canvas.create_image(0,0,anchor=NW, image=image)

def draw1(canvas,data5):
    msg=data5.numberList[0]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(100,200,text=msg,fill=color,font="Helvetica 14 bold")

def draw2(canvas,data5):
    msg=data5.numberList[1]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(100,185,text=msg,fill=color,font="Helvetica 14 bold")

def draw3(canvas,data5):
    msg=data5.numberList[2]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(100,170,text=msg,fill=color,font="Helvetica 14 bold")

def draw4(canvas,data5):
    msg=data5.numberList[3]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(100,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw5(canvas,data5):
    msg=data5.numberList[4]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(100,140,text=msg,fill=color,font="Helvetica 14 bold")

def draw6(canvas,data5):
    msg=data5.numberList[5]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(100,125,text=msg,fill=color,font="Helvetica 14 bold")

def draw7(canvas,data5):
    msg=data5.numberList[6]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(100,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw8(canvas,data5):
    msg=data5.numberList[7]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(115,125,text=msg,fill=color,font="Helvetica 14 bold")

def draw9(canvas,data5):
    msg=data5.numberList[8]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(130,140,text=msg,fill=color,font="Helvetica 14 bold")

def draw10(canvas,data5):
    msg=data5.numberList[9]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(145,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw11(canvas,data5):
    msg=data5.numberList[10]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(160,140,text=msg,fill=color,font="Helvetica 14 bold")

def draw12(canvas,data5):
    msg=data5.numberList[11]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(175,125,text=msg,fill=color,font="Helvetica 14 bold")

def draw13(canvas,data5):
    msg=data5.numberList[12]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(190,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw14(canvas,data5):
    msg=data5.numberList[13]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(190,125,text=msg,fill=color,font="Helvetica 14 bold")

def draw15(canvas,data5):
    msg=data5.numberList[14]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(190,140,text=msg,fill=color,font="Helvetica 14 bold")

def draw16(canvas,data5):
    msg=data5.numberList[15]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(190,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw17(canvas,data5):
    msg=data5.numberList[16]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(190,170,text=msg,fill=color,font="Helvetica 14 bold")   
    
def draw18(canvas,data5):
    msg=data5.numberList[17]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(190,185,text=msg,fill=color,font="Helvetica 14 bold")

def draw19(canvas,data5):
    msg=data5.numberList[18]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(190,200,text=msg,fill=color,font="Helvetica 14 bold")

def draw20(canvas,data5):
    msg=data5.numberList[19]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(210,200,text=msg,fill=color,font="Helvetica 14 bold")

def draw21(canvas,data5):
    msg=data5.numberList[20]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(216,185,text=msg,fill=color,font="Helvetica 14 bold")

def draw22(canvas,data5):
    msg=data5.numberList[21]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(222,170,text=msg,fill=color,font="Helvetica 14 bold")

def draw23(canvas,data5):
    msg=data5.numberList[22]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(228,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw24(canvas,data5):
    msg=data5.numberList[23]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(234,140,text=msg,fill=color,font="Helvetica 14 bold")

def draw25(canvas,data5):
    msg=data5.numberList[24]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(240,125,text=msg,fill=color,font="Helvetica 14 bold")

def draw26(canvas,data5):
    msg=data5.numberList[25]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(246,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw27(canvas,data5):
    msg=data5.numberList[26]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(252,125,text=msg,fill=color,font="Helvetica 14 bold")

def draw28(canvas,data5):
    msg=data5.numberList[27]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(258,140,text=msg,fill=color,font="Helvetica 14 bold")

def draw29(canvas,data5):
    msg=data5.numberList[28]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(264,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw30(canvas,data5):
    msg=data5.numberList[29]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(270,170,text=msg,fill=color,font="Helvetica 14 bold")

def draw31(canvas,data5):
    msg=data5.numberList[30]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(276,185,text=msg,fill=color,font="Helvetica 14 bold")

def draw32(canvas,data5):
    msg=data5.numberList[31]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(282,200,text=msg,fill=color,font="Helvetica 14 bold")

def draw33(canvas,data5):
    msg=data5.numberList[32]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(258,170,text=msg,fill=color,font="Helvetica 14 bold")

def draw34(canvas,data5):
    msg=data5.numberList[33]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(246,170,text=msg,fill=color,font="Helvetica 14 bold")

def draw35(canvas,data5):
    msg=data5.numberList[34]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(234,170,text=msg,fill=color,font="Helvetica 14 bold")

def draw36(canvas,data5):
    msg=data5.numberList[35]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(295,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw37(canvas,data5):
    msg=data5.numberList[36]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(310,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw38(canvas,data5):
    msg=data5.numberList[37]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(325,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw39(canvas,data5):
    msg=data5.numberList[38]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(340,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw40(canvas,data5):
    msg=data5.numberList[39]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(355,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw41(canvas,data5):
    msg=data5.numberList[40]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(370,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw42(canvas,data5):
    msg=data5.numberList[41]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(385,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw43(canvas,data5):
    msg=data5.numberList[42]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(340,125,text=msg,fill=color,font="Helvetica 14 bold")

def draw44(canvas,data5):
    msg=data5.numberList[43]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(340,140,text=msg,fill=color,font="Helvetica 14 bold")

def draw45(canvas,data5):
    msg=data5.numberList[44]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(340,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw46(canvas,data5):
    msg=data5.numberList[45]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(340,170,text=msg,fill=color,font="Helvetica 14 bold")

def draw47(canvas,data5):
    msg=data5.numberList[46]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(340,185,text=msg,fill=color,font="Helvetica 14 bold")

def draw48(canvas,data5):
    msg=data5.numberList[47]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(340,200,text=msg,fill=color,font="Helvetica 14 bold")

def draw49(canvas,data5):
    msg=data5.numberList[48]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(410,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw50(canvas,data5):
    msg=data5.numberList[49]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(410,125,text=msg,fill=color,font="Helvetica 14 bold")

def draw51(canvas,data5):
    msg=data5.numberList[50]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(410,140,text=msg,fill=color,font="Helvetica 14 bold")

def draw52(canvas,data5):
    msg=data5.numberList[51]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(410,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw53(canvas,data5):
    msg=data5.numberList[52]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(410,170,text=msg,fill=color,font="Helvetica 14 bold")

def draw54(canvas,data5):
    msg=data5.numberList[53]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(410,185,text=msg,fill=color,font="Helvetica 14 bold")

def draw55(canvas,data5):
    msg=data5.numberList[54]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(410,200,text=msg,fill=color,font="Helvetica 14 bold")

def draw56(canvas,data5):
    msg=data5.numberList[55]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(425,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw57(canvas,data5):
    msg=data5.numberList[56]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(440,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw58(canvas,data5):
    msg=data5.numberList[57]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(455,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw59(canvas,data5):
    msg=data5.numberList[58]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(470,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw60(canvas,data5):
    msg=data5.numberList[59]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(485,110,text=msg,fill=color,font="Helvetica 14 bold")

def draw61(canvas,data5):
    msg=data5.numberList[60]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(485,125,text=msg,fill=color,font="Helvetica 14 bold")

def draw62(canvas,data5):
    msg=data5.numberList[61]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(485,140,text=msg,fill=color,font="Helvetica 14 bold")

def draw63(canvas,data5):
    msg=data5.numberList[62]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(485,155,text=msg,fill=color,font="Helvetica 14 bold")

def draw64(canvas,data5):
    msg=data5.numberList[63]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(485,170,text=msg,fill=color,font="Helvetica 14 bold")

def draw65(canvas,data5):
    msg=data5.numberList[64]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(485,185,text=msg,fill=color,font="Helvetica 14 bold")

def draw66(canvas,data5):
    msg=data5.numberList[65]
    redColor=random.randint(200,255)
    greenColor=random.randint(100,255)
    blueColor=random.randint(0,125)
    color=rgbString(redColor,greenColor,blueColor)
    canvas.create_text(485,200,text=msg,fill=color,font="Helvetica 14 bold")


def redrawAll5(canvas, data5):
    if data5.mode=="start":
        draw0(canvas,data5)
        draw1(canvas,data5)
        draw2(canvas,data5)
        draw3(canvas,data5)
        draw4(canvas,data5)
        draw5(canvas,data5)
        draw6(canvas,data5)
        draw7(canvas,data5)
        draw8(canvas,data5)
        draw9(canvas,data5)
        draw10(canvas,data5)
        draw11(canvas,data5)
        draw12(canvas,data5)
        draw13(canvas,data5)
        draw14(canvas,data5)
        draw15(canvas,data5)
        draw16(canvas,data5)
        draw17(canvas,data5)
        draw18(canvas,data5)
        draw19(canvas,data5)
        draw20(canvas,data5)
        draw21(canvas,data5)
        draw22(canvas,data5)
        draw23(canvas,data5)
        draw24(canvas,data5)
        draw25(canvas,data5)
        draw26(canvas,data5)
        draw27(canvas,data5)
        draw28(canvas,data5)
        draw29(canvas,data5)
        draw30(canvas,data5)
        draw31(canvas,data5)
        draw32(canvas,data5)
        draw33(canvas,data5)
        draw34(canvas,data5)
        draw35(canvas,data5)
        draw36(canvas,data5)
        draw37(canvas,data5)
        draw38(canvas,data5)
        draw39(canvas,data5)
        draw40(canvas,data5)
        draw41(canvas,data5)
        draw42(canvas,data5)
        draw43(canvas,data5)
        draw44(canvas,data5)
        draw45(canvas,data5)
        draw46(canvas,data5)
        draw47(canvas,data5)
        draw48(canvas,data5)
        draw49(canvas,data5)
        draw50(canvas,data5)
        draw51(canvas,data5)
        draw52(canvas,data5)
        draw53(canvas,data5)
        draw54(canvas,data5)
        draw55(canvas,data5)
        draw56(canvas,data5)
        draw57(canvas,data5)
        draw58(canvas,data5)
        draw59(canvas,data5)
        draw60(canvas,data5)
        draw61(canvas,data5)
        draw62(canvas,data5)
        draw63(canvas,data5)
        draw64(canvas,data5)
        draw65(canvas,data5)
        draw66(canvas,data5)
    elif data5.mode=="menu":
        draw112(canvas,data5)
    

####################################
# use the run function as-is
####################################

def run5(width=600, height=600):
    def redrawAllWrapper5(canvas, data5):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data5.width, data5.height,
                                fill='white', width=0)
        redrawAll5(canvas, data5)
        canvas.update()    

    def mousePressedWrapper5(event, canvas, data5):
        mousePressed5(event, data5)
        redrawAllWrapper5(canvas, data5)

    def keyPressedWrapper5(event, canvas, data5):
        keyPressed5(event, data5)
        redrawAllWrapper5(canvas, data5)

    def timerFiredWrapper5(canvas, data5):
        timerFired5(data5)
        redrawAllWrapper5(canvas, data5)
        # pause, then call timerFired again
        canvas.after(data5.timerDelay, timerFiredWrapper5, canvas, data5)
    # Set up data5 and call init
    class Struct(object): pass
    data5 = Struct()
    data5.width = width
    data5.height = height
    data5.timerDelay =30
    init5(data5)
    # create the root and the canvas
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(root, width=data5.width, height=data5.height)
    canvas.pack()
    # set up events
    root.canvas=canvas.canvas=canvas
    canvas.data5={ }
    inits5(canvas)
    
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper5(event, canvas, data5))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper5(event, canvas, data5))
    timerFiredWrapper5(canvas, data5)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run5(600, 600)
