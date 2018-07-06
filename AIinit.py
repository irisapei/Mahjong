from tkinter import * 
import copy 
import math 
import random
import string 
root = Tk()

def dealingHandinit(data): 
    data.objectPics = {"yiwan": PhotoImage(file = "yiwan.gif"), "erwan": PhotoImage(file = "erwan.gif"), "sanwan": PhotoImage(file = "sanwan.gif"), "siwan": PhotoImage(file = "siwan.gif"), "wuwan": PhotoImage(file="wuwan.gif"), "liuwan": PhotoImage(file="liuwan.gif"), "qiwan": PhotoImage(file="qiwan.gif"), "bawan": PhotoImage(file="bawan.gif"), "jiuwan": PhotoImage(file="jiuwan.gif"), "yibing": PhotoImage(file="yibing.gif"), "liangbing": PhotoImage(file="liangbing.gif"), "sanbing": PhotoImage(file="sanbing.gif"), "sibing": PhotoImage(file="sibing.gif"), "wubing": PhotoImage(file="wubing.gif"), "liubing": PhotoImage(file="liubing.gif"), "qibing": PhotoImage(file="qibing.gif"), "babing": PhotoImage(file="babing.gif"), "jiubing": PhotoImage(file="jiubing.gif"), "yitiao": PhotoImage(file="yitiao.gif"), "ertiao": PhotoImage(file="ertiao.gif"), "santiao": PhotoImage(file="santiao.gif"), "sitiao": PhotoImage(file="sitiao.gif"), "wutiao": PhotoImage(file="wutiao.gif"), "liutiao": PhotoImage(file="liutiao.gif"), "qitiao": PhotoImage(file="qitiao.gif"), "batiao": PhotoImage(file="batiao.gif"), "jiutiao": PhotoImage(file="jiutiao.gif"), "Dong": PhotoImage(file="Dong.gif"), "Nan": PhotoImage(file="Nan.gif"), "Xi": PhotoImage(file="Xi.gif"), "Bei": PhotoImage(file="Bei.gif"), "Fa": PhotoImage(file="Fa.gif"), "Zhong": PhotoImage(file="Zhong.gif")}

    #puts all images into playerImages 
    for key in data.objectPics.keys(): 
        data.playerImages.append(data.objectPics[key])
    data.keys = list(data.objectPics.keys()) 
    #Player One's Hand
    for i in range (1,14):
        randomKey = random.choice(data.keys)
        data.playerOneHand.append(randomKey) 
        randomTile = data.objectPics[randomKey] 
        #puts the images in a list to be drawn 
        data.playerOnePieces.append([data.x1*(i*2), data.y1, randomTile])
    #Player Two's Hand 
    for i in range (1,14): 
        randomKey = random.choice(data.keys)
        data.playerTwoHand.append(randomKey) 
        randomTile = data.objectPics[randomKey] 
        data.playerTwoPieces.append([data.x1*(i*2), data.y1, randomTile])
    #Player Three's Hand 
    for i in range(1,14):
        randomKey = random.choice(data.keys)
        data.playerThreeHand.append(randomKey)
        randomTile = data.objectPics[randomKey] 
        data.playerThreePieces.append([data.x1*(i*2), data.y1, randomTile])
    #Player Four's Hand 
    for i in range (1,14):
        randomKey = random.choice(data.keys)
        data.playerFourHand.append(randomKey) 
        randomTile = data.objectPics[randomKey]  
        data.playerFourPieces.append([data.x1*(i*2), data.y1, randomTile])


    
        
    data.nameValuesWan = {"yiwan":1, "erwan":2, "sanwan":3, "siwan":4, "wuwan":5, "liuwan":6, "qiwan":7, "bawan": 8, "jiuwan":9} 
    
    data.nameValuesTiao = {"yitiao":1, "ertiao":2, "santiao":3, "sitiao":4, "wutiao":5, "liutiao":6, "qitiao":7, "batiao": 8, "jiutiao":9} 
    
    data.nameValuesBing = {"yibing":1, "liangbing":2, "sanbing":3, "sibing":4, "wubing":5, "liubing":6, "qibing":7, "babing": 8, "jiubing":9} 

    
     
def randomInit(data): 
    data.mode = "Start Screen" 
    data.icon = (PhotoImage(file = "start.gif"))
    data.x2 = 235
    data.y2 = 250 
    data.speed = 40
    data.headingRight = True
    data.headingDown = True 
    data.halfHeight = data.height//2
    #The Images, separated from keys 
    data.playerImages = []
    #Hand of IMAGES for each player 
    data.playerOnePieces = [] 
    data.playerTwoPieces = []
    data.playerThreePieces =[]
    data.playerFourPieces = [] 
    #Hand of actual names of tiles for each player
    data.playerOneHand = [] 
    data.playerTwoHand = []
    data.playerThreeHand = [] 
    data.playerFourHand = []
    #the colors for the things on top
    #etc 
    data.x1 = 26.5
    data.y1 = (data.height*3)//4
    data.playingGame = False  
    data.peng = False 
    data.p1peng = False 
    data.p2peng = False 
    data.p3peng = False 
    data.p4peng = False 
    data.chi = False 
    data.p1Chi = False 
    data.p2Chi = False 
    data.p3Chi = False 
    data.p4Chi = False 
    data.played = []
    data.tileNumber = 0 
    data.playedTileName = "" 
    data.p1turn = False 
    data.p2turn = False 
    data.p3turn = False 
    data.p4turn = False 
    data.counter = 0
    data.p1color = "black"
    data.p2color = "black"
    data.p3color = "black"
    data.p4color = "black"
    data.p1tookpiece = False  
    data.p2tookpiece = False 
    data.p3tookpiece = False 
    data.p4tookpiece = False 
    #idk
    data.p2ubitchass = False
    data.p3ubitchass = False
    data.p4ubitchass = False 
    data.allNames = []
    data.winNumber = 0
    data.p1win = False 
    data.p2win = False
    data.p3win = False
    data.p4win = False 
    data.test = False 
    data.test1 = False 
    data.wtf = [] 