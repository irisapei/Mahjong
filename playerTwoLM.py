#####################
#Player Two Stuff
#####################
import random 
from hu import *

def playerTwoMousePressed(event,data):
    #for i in range (len(data.playerTwoPieces)): 
        #print ("player2 pieces:", data.playerTwoPieces[i])
    for i in range (len(data.playerTwoPieces)):
        x1 = (data.playerTwoPieces[i][0])-19
        y1 = (data.playerTwoPieces[i][1])-19
        currImage = data.playerTwoPieces[i][2] 
        x2 = x1+currImage.width()
        y2 = y1+currImage.height() 
        if (x1 < event.x < x1+currImage.width()):
            if (y1 < event.y < y1+currImage.height()):
                data.clicked = True 
                data.tileNumber = i 
                
def playerTwoKeyPressed(event,data): 
    if event.keysym == "space":
        data.mode = "Player Three Game"
        data.p2turn = True
        data.p3turn = False 
        data.tileNumber = 0   
        data.leftturn = "Player Two"
        #print (data.playerTwoHand)
        #print (data.playerTwoPieces)
    if event.keysym == "Up" and len(data.playerTwoPieces)>13:
        print ("reached") 
        #pictures
        if data.played == []: 
            data.played.append([data.x2, data.y2, data.playerTwoPieces[data.tileNumber][2]])
        elif data.played != []:
            #print ("reached")
            image = data.playerTwoPieces[data.tileNumber][2]
            if 187<data.x2<500: 
                if data.peng == True or data.chi == True : 
                    data.played.append([data.x2, data.y2, data.playerTwoPieces[data.tileNumber][2]])
                else:
                    data.x2 = data.x2+image.width()+7 
                    data.played.append([data.x2, data.y2, data.playerTwoPieces[data.tileNumber][2]])
            elif data.x2>500:
                data.x2 = 235
                data.y2 += image.height()
                data.played.append([data.x2, data.y2, data.playerTwoPieces[data.tileNumber][2]])
            #print (data.counter)
        #data.counter +=1
        #print (data.played)
        data.playerTwoPieces.pop(data.tileNumber)
        #names 
        data.playedTileName = data.playerTwoHand[data.tileNumber]
        data.playerTwoHand.remove(data.playedTileName)
        #shifting everything to the left 
        for i in range (data.tileNumber, len(data.playerTwoPieces)):
            original = data.playerTwoPieces[i][0]
            image = data.playerTwoPieces[i][2]
            data.playerTwoPieces[i][0] = original-image.width()-9
        data.leftturn = "Player Two"
        data.p2turn = True
        data.p2tookpiece = False 
        data.chi = False 
        data.peng = False  
        
    #re-putting the piece back in 
    #puts a random piece in if you don't pick from the middle 
    if event.keysym == "r" and data.p2turn == False:  
        length = len(data.playerTwoPieces)-1
        randomKey = random.choice(data.keys) 
        randomTile = data.objectPics[randomKey]  
        data.playerTwoHand.append(randomKey) 
        data.playerTwoPieces.append([(data.playerTwoPieces[length][0]+(data.playerTwoPieces[data.tileNumber][2]).width()+9), 600, randomTile])

    #print (isHu(data.playerTwoHand))
def playerTwoGameRedrawAll(canvas,data):
    
    canvas.create_text(150,60, text = "Player Two's Turn!", font = "verdana 15")
    for picture in data.playerTwoPieces:  
        canvas.create_image(picture[0], picture[1], image = picture[2])
    if data.p2turn == True and data.peng == False and data.chi == False: 
        canvas.create_text(280,145, text = "P2 has gone! Press the space bar to advance to P3's turn.", font = "BrushScriptMT 25", fill = "white")
    #data.p2turn = False 
    