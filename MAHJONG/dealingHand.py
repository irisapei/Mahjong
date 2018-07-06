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
    for i in range (1,15):
        randomKey = random.choice(data.keys)
        data.playerOneHand.append(randomKey) 
        randomTile = data.objectPics[randomKey] 
        #puts the images in a list to be drawn 
        data.playerOnePieces.append([data.x1*(i*2), data.y1, randomTile])
    #Player Two's Hand 
    for i in range (1,15): 
        randomKey = random.choice(data.keys)
        data.playerTwoHand.append(randomKey) 
        #randomNumber = random.randint(0,len(data.playerImages )-1)
        randomTile = data.objectPics[randomKey] 
        data.playerTwoPieces.append([data.x1*(i*2), data.y1, randomTile])
    #Player Three's Hand 
    for i in range(1,15):
        randomKey = random.choice(data.keys)
        data.playerThreeHand.append(randomKey)
        #randomNumber = random.randint(0,len(data.playerImages )-1)
        randomTile = data.objectPics[randomKey] 
        data.playerThreePieces.append([data.x1*(i*2), data.y1, randomTile])
    #Player Four's Hand 
    for i in range (1,15):
        randomKey = random.choice(data.keys)
        data.playerFourHand.append(randomKey) 
        #randomNumber = random.randint(0,len(data.playerImages )-1)
        randomTile = data.objectPics[randomKey]  
        data.playerFourPieces.append([data.x1*(i*2), data.y1, randomTile])