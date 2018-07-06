################
#Player Four Stuff
################
import random 
from hu import *
def playerFourMousePressed(event,data):
    #for i in range (len(data.playerFourPieces)):
        #print ("player4 pieces:", data.playerFourPieces[i]) 
    for i in range (len(data.playerFourPieces)):
        x1 = (data.playerFourPieces[i][0])-19
        y1 = (data.playerFourPieces[i][1])-19
        currImage = data.playerFourPieces[i][2] 
        x2 = x1+currImage.width()
        y2 = y1+currImage.height() 
        if (x1 < event.x < x1+currImage.width()):
            if (y1 < event.y < y1+currImage.height()):
                data.clicked = True 
                data.tileNumber = i 
                
def playerFourKeyPressed(event,data): 
    if event.keysym == "space":
        data.p4turn = True
        data.p1turn = False
        data.mode = "Player One Game"
        data.tileNumber = 0 
        data.leftturn = "Player Four"
        #print (data.playerFourHand)
       # print (data.playerFourPieces)
    if event.keysym == "Up" and len(data.playerFourPieces)>13:
        if data.played == []: 
            data.played.append([data.x2, data.y2, data.playerFourPieces[data.tileNumber][2]]) 
        #adding to tiles in the middle 
        elif data.played != []:
            image = data.playerFourPieces[data.tileNumber][2]
            if 187<data.x2<500: 
                if data.peng == True or data.chi == True: 
                    data.played.append([data.x2, data.y2, data.playerFourPieces[data.tileNumber][2]])
                else: 
                    data.x2 = data.x2+image.width()+7 
                    data.played.append([data.x2, data.y2, data.playerFourPieces[data.tileNumber][2]])
            elif data.x2>500:
                data.x2 = 235
                data.y2 += image.height()
                data.played.append([data.x2, data.y2, data.playerFourPieces[data.tileNumber][2]])
        #removing the tile from the actual deck :( 
        data.playerFourPieces.pop(data.tileNumber)
        #names 
        data.playedTileName = data.playerFourHand[data.tileNumber]
        data.playerFourHand.remove(data.playedTileName)
        #shifting everything to the left 
        for i in range (data.tileNumber, len(data.playerFourPieces)):
            original = data.playerFourPieces[i][0]
            image = data.playerFourPieces[i][2]
            data.playerFourPieces[i][0] = original-image.width()-9
        data.p4turn = True
        data.leftturn = "Player Four"
        data.p4tookpiece = False 
        data.chi = False 
        data.peng = False 
    #a random piece 
    if event.keysym == "r" and data.p4turn == False:  
        length = len(data.playerFourPieces)-1
        randomKey = random.choice(data.keys) 
        randomTile = data.objectPics[randomKey]  
        data.playerFourHand.append(randomKey) 
        data.playerFourPieces.append([(data.playerFourPieces[length][0]+(data.playerFourPieces[data.tileNumber][2]).width()+9), 600, randomTile]) 
              
def playerFourGameRedrawAll(canvas,data):
    canvas.create_text(150,60, text = "Player Four's Turn!", font = "verdana 15")
    for picture in data.playerFourPieces:  
        canvas.create_image(picture[0], picture[1], image = picture[2]) 
    if data.p4turn == True and data.peng == False and data.chi == False: 
        canvas.create_text(280,145, text = "P4 has gone! Press the space bar to advance to P1's turn.", font = "BrushScriptMT 25", fill = "white")
    #data.p4turn = False 
