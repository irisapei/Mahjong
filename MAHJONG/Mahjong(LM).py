###15-112 TERM PROJECT YUH!!! ### 
from tkinter import * 
import copy 
import math 
import random
import string 
from startScreen import * 
from LMinit import * 
from drawBoard import * 
from peng import * 
from chi import * 
from hu import * 
from bouncingTile import * 
from playerOneLM import * 
from playerTwoLM import * 
from playerThreeLM import * 
from playerFourLM import * 
#################
#Animation Initializations 
#################

def init(data): 
    randomInit(data)
    dealingHandinit(data) 
    data.blink = False 
    data.icon = (PhotoImage(file = "bitchass!.gif"))
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
        
def keyPressed(event,data):
    if data.mode == "Start Screen":
        startScreenKeyPressed(event,data)
    elif data.mode == "Player One Game" : 
        playerOneKeyPressed(event,data) 
    elif data.mode == "Player Two Game":
        playerTwoKeyPressed(event,data)  
    elif data.mode == "Player Three Game": 
        playerThreeKeyPressed(event,data)
    elif data.mode == "Player Four Game": 
        playerFourKeyPressed(event,data)
    #Peng stuff 
    pengKeyPressed(event,data)
    chiKeyPressed(event,data) 
        
        
def timerFired(data):
    if data.mode == "Start Screen":
        #bounce(data)
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
        drawBoard(canvas,data)
        playerOneGameRedrawAll(canvas,data) 
    elif data.mode == "Player Two Game": 
        data.p2color = "yellow"
        data.p1color = "black"
        data.p3color = "black"
        data.p4color = "black" 
        data.p1turn = False 
        drawBoard(canvas,data)
        playerTwoGameRedrawAll(canvas,data)
    elif data.mode == "Player Three Game":
        data.p3color = "yellow" 
        data.p1color = "black"
        data.p2color = "black"
        data.p4color = "black"
        data.p2turn = False 
        drawBoard(canvas,data)
        playerThreeGameRedrawAll(canvas,data) 
    elif data.mode == "Player Four Game":
        data.p4color = "yellow"
        data.p1color = "black"
        data.p3color = "black"
        data.p2color = "black"
        data.p3turn = False 
        drawBoard(canvas,data) 
        playerFourGameRedrawAll(canvas,data) 
    drawMiddleTiles(canvas,data) 
    pengRedrawAll(canvas,data) 
    chiRedrawAll(canvas,data)

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

run(750, 800)