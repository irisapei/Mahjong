##################
#Player Three Stuff
##################
import random
from hu import * 

def playerThreeMousePressed(event,data):
    #for i in range (len(data.playerThreePieces)):
        #print ("player3 pieces:", data.playerThreePieces[i])
    for i in range (len(data.playerThreePieces)):
        x1 = (data.playerThreePieces[i][0])-19
        y1 = (data.playerThreePieces[i][1])-19
        currImage = data.playerThreePieces[i][2] 
        x2 = x1+currImage.width()
        y2 = y1+currImage.height() 
        if (x1 < event.x < x1+currImage.width()):
            if (y1 < event.y < y1+currImage.height()):
                data.clicked = True 
                data.tileNumber = i 
                
def playerThreeKeyPressed(event,data): 
    if event.keysym == "space":
        data.mode = "Player Four Game"
        data.p3turn = True 
        data.p4turn = False 
        data.tileNumber = 0 
        data.leftturn = "Player Three"
        #print (data.playerTwoHand)
        #print (data.playerTwoPieces)
    if event.keysym == "Up"and len(data.playerThreePieces)>13:
        #print ("reached") 
        if data.played == []: 
            data.played.append([data.x2, data.y2, data.playerThreePieces[data.tileNumber][2]])
        elif data.played != []:
            image = data.playerThreePieces[data.tileNumber][2]
            if 187<data.x2<500: 
                if data.peng == True or data.chi == True: 
                    data.played.append([data.x2, data.y2, data.playerThreePieces[data.tileNumber][2]])
                else: 
                    data.x2 = data.x2+image.width()+7 
                    data.played.append([data.x2, data.y2, data.playerThreePieces[data.tileNumber][2]])
            elif data.x2>500:
                data.x2 = 235 
                data.y2 += image.height()
                data.played.append([data.x2, data.y2, data.playerThreePieces[data.tileNumber][2]])
        data.playerThreePieces.pop(data.tileNumber)
        #names 
        data.playedTileName = data.playerThreeHand[data.tileNumber]
        data.playerThreeHand.remove(data.playedTileName)
        #shifting everything to the left 
        for i in range (data.tileNumber, len(data.playerThreePieces)):
            original = data.playerThreePieces[i][0]
            image = data.playerThreePieces[i][2]
            data.playerThreePieces[i][0] = original-image.width()-9
        data.p3turn = True
        data.leftturn = "Player Three"
        data.p3tookpiece = False 
        data.chi = False 
        data.peng = False 
    
    #puts a random tile in 
    if event.keysym == "r" and data.p3turn == False:  
        length = len(data.playerThreePieces)-1
        randomKey = random.choice(data.keys) 
        randomTile = data.objectPics[randomKey]  
        data.playerThreeHand.append(randomKey) 
        data.playerThreePieces.append([(data.playerThreePieces[length][0]+(data.playerThreePieces[data.tileNumber][2]).width()+9), 600, randomTile]) 
    #print (isHu(data.playerThreeHand))   
        
def playerThreeGameRedrawAll(canvas,data):
    canvas.create_text(150,60, text = "Player Three's Turn!", font = "verdana 15" )
    for i in range (len(data.playerThreePieces)): 
        #print (data.playerThreePieces[i][0],data.playerThreePieces[i][1],data.playerThreePieces[i][2] )
        canvas.create_image(data.playerThreePieces[i][0], data.playerThreePieces[i][1], image = data.playerThreePieces[i][2])
    if data.p3turn == True and data.peng == False and data.chi == False: 
        canvas.create_text(280,145, text = "P3 has gone! Press the space bar to advance to P4's turn.", font = "BrushScriptMT 25", fill = "white")
    #data.p3turn = False 
        