###15-112 TERM PROJECT YUH!!! ### 
from tkinter import *
import copy
import math
import random
import string
from startScreen import *
from AIinit import *
from drawBoardAI import *
from peng import *
from chi import *
from hu import *
from bouncingTile import *
from playerOneLM import *
from playerTwoLM import *
from playerThreeLM import *
from playerFourLM import *
from pengAI import *
from chiAI import *
from playerOneAI import *
from playerTwoAI import *
from playerThreeAI import *
from playerFourAI import *
from win import *
from helpScreen import *
#################
#Animation Initializations
#################

def init(data):
    data.gametype = ""
    data.chicken = False
    data.tempup = False
    randomInit(data)
    dealingHandinit(data)
    data.blink = False
    data.icon = (PhotoImage(file = "start.gif"))
    data.leftturn = ""
    data.fa = PhotoImage(file = "Fa.gif")
    data.bing = PhotoImage(file = "yibing.gif")
    data.tiao = PhotoImage(file = "santiao.gif")
    data.number = PhotoImage(file = "yiwan.gif")

def mousePressed(event,data):
    if data.mode == "Start Screen":
        startScreenMousePressed(event,data)
    elif data.mode == "Player One Game":
        playerOneMousePressed(event,data)
    elif data.mode == "Player Two Game":
        playerTwoMousePressed(event,data)
    elif data.mode == "Player Three Game":
        playerThreeMousePressed(event,data)
    elif data.mode == "Player Four Game":
        playerFourMousePressed(event,data)
    elif data.mode == "AI Player One Game":
        playerOneAIMousePressed(event,data)

def keyPressed(event,data):
    if event.keysym == "a":
        data.test = True
        #print (data.test)
    if event.keysym == "b":
        data.test1 = True
    if event.keysym == "o":
        init(data)
    if event.keysym == "Up":
        data.tempup = True
    if data.mode == "Start Screen":
        startScreenKeyPressed(event,data)
    elif data.mode == "Player One Game":
        playerOneKeyPressed(event,data)
        pengKeyPressed(event,data)
        chiKeyPressed(event,data)
    elif data.mode == "Player Two Game":
        playerTwoKeyPressed(event,data)
        pengKeyPressed(event,data)
        chiKeyPressed(event,data)
    elif data.mode == "Player Three Game":
        playerThreeKeyPressed(event,data)
        pengKeyPressed(event,data)
        chiKeyPressed(event,data)
    elif data.mode == "Player Four Game":
        playerFourKeyPressed(event,data)
        chiKeyPressed(event,data)
        pengKeyPressed(event,data)
    elif data.mode == "AI Player One Game":
        data.p4turn = True
        playerOneAIKeyPressed(event,data)
        pengAIKeyPressed(event,data)
        chiAIKeyPressed(event,data)
    elif data.mode == "AI Player Two Game":
        data.p1turn = True
        playerTwoAIKeyPressed(event,data)
        pengAIKeyPressed(event,data)
        chiAIKeyPressed(event,data)
    elif data.mode == "AI Player Three Game":
        data.p2turn = True
        playerThreeAIKeyPressed(event,data)
        pengAIKeyPressed(event,data)
        chiAIKeyPressed(event,data)
    elif data.mode == "AI Player Four Game":
        data.p3turn = True
        playerFourAIKeyPressed(event,data)
        pengAIKeyPressed(event,data)
        chiAIKeyPressed(event,data)

def timerFired(data):
    if data.mode == "Start Screen":
        startScreenTimerFired(data)
    if data.blink == False:
        data.blink = True
    elif data.blink == True:
        data.blink = False

def redrawAll(canvas, data):
    if data.mode == "Start Screen":
        canvas.create_image(data.width//2,data.height//2, image = data.icon)
        startScreenRedrawAll(canvas, data)
    elif data.mode == "Player One Game":
        data.p1color = "yellow"
        data.p2color = "black"
        data.p3color = "black"
        data.p4color = "black"
        data.p4turn = False
        if data.test == True:
            data.playerOneHand, data.playerOnePieces = [], []
            data.playerOneHand = ["yiwan", "erwan", "sanwan", "yibing", "liangbing", "sanbing", "Fa", "Fa", "Fa", "yitiao", "yitiao", "yitiao", "Zhong", "jiutiao"]
            for i in range(len(data.playerOneHand)):
                data.playerOnePieces.append ([data.x1*(i*2)+35, data.y1, data.objectPics[(data.playerOneHand[i])]])
            if data.tempup == True:
                data.playerOnePieces.pop()
                data.playerOneHand.pop()
        drawBoardAI(canvas,data)
        playerOneGameRedrawAll(canvas,data)
        pengRedrawAll(canvas,data)
        chiRedrawAll(canvas,data)
    elif data.mode == "Player Two Game":
        data.p2color = "yellow"
        data.p1color = "black"
        data.p3color = "black"
        data.p4color = "black"
        data.p1turn = False
        if data.test1 == True:
            data.playerTwoHand, data.playerTwoPieces = [], []
            data.playerTwoHand = ["yiwan", "erwan", "sanwan", "yibing", "liangbing", "sanbing", "Fa", "Fa", "Fa", "yitiao", "yitiao", "yitiao", "Zhong"]
            for i in range(len(data.playerTwoHand)):
                data.playerTwoPieces.append([data.x1*(i*2)+35, data.y1, data.objectPics[(data.playerTwoHand[i])]])
        drawBoardAI(canvas,data)
        playerTwoGameRedrawAll(canvas,data)
        pengRedrawAll(canvas,data)
        chiRedrawAll(canvas,data)
    elif data.mode == "Player Three Game":
        data.p3color = "yellow"
        data.p1color = "black"
        data.p2color = "black"
        data.p4color = "black"
        data.p2turn = False
        drawBoardAI(canvas,data)
        playerThreeGameRedrawAll(canvas,data)
        pengRedrawAll(canvas,data)
        chiRedrawAll(canvas,data)
    elif data.mode == "Player Four Game":
        data.p4color = "yellow"
        data.p1color = "black"
        data.p3color = "black"
        data.p2color = "black"
        data.p3turn = False
        drawBoardAI(canvas,data)
        playerFourGameRedrawAll(canvas,data)
        pengRedrawAll(canvas,data)
        chiRedrawAll(canvas,data)

    elif data.mode == "AI Player One Game":
        data.p1color = "yellow"
        data.p2color = "black"
        data.p3color = "black"
        data.p4color = "black"
        data.p4turn = False
        drawBoardAI(canvas,data)
        playerOneAIGameRedrawAll(canvas,data)
        chiAIRedrawAll(canvas,data)
        pengAIRedrawAll(canvas,data)

    elif data.mode == "AI Player Two Game":
        data.p2color = "yellow"
        data.p1color = "black"
        data.p3color = "black"
        data.p4color = "black"
        data.p1turn = False
        drawBoardAI(canvas,data)
        for picture in data.playerOnePieces:
            canvas.create_image(picture[0], picture[1], image = picture[2])
        playerTwoAIGameRedrawAll(canvas,data)
        chiAIRedrawAll(canvas,data)
        pengAIRedrawAll(canvas,data)

    elif data.mode == "AI Player Three Game":
        data.p3color = "yellow"
        data.p1color = "black"
        data.p2color = "black"
        data.p4color = "black"
        data.p2turn = False
        drawBoardAI(canvas,data)
        for picture in data.playerOnePieces:
            canvas.create_image(picture[0], picture[1], image = picture[2])
        playerThreeAIGameRedrawAll(canvas,data)
        chiAIRedrawAll(canvas,data)
        pengAIRedrawAll(canvas,data)

    elif data.mode == "AI Player Four Game":
        data.p4color = "yellow"
        data.p1color = "black"
        data.p3color = "black"
        data.p2color = "black"
        data.p3turn = False
        drawBoardAI(canvas,data)
        for picture in data.playerOnePieces:
            canvas.create_image(picture[0], picture[1], image = picture[2])
        playerFourAIGameRedrawAll(canvas,data)
        chiAIRedrawAll(canvas,data)
        pengAIRedrawAll(canvas,data)
    drawMiddleTiles(canvas,data)
    winDrawing(canvas,data)
    if data.mode == "Help":
        drawHelp(canvas,data)
##################
#Run Function
#Taken from 15-112 Class Notes on Animation - Time Based Animations in Tkinter
##################
def run(width=300, height=500):
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
    data.timerDelay = 700 # milliseconds
    root = Toplevel()
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    init(data)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(790, 800)
