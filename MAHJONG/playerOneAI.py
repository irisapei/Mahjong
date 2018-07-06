import random 
from hu import *
# Player One 
def playerOneAIMousePressed(event,data):
    for i in range (len(data.playerOnePieces)):
        x1 = (data.playerOnePieces[i][0])-19
        y1 = (data.playerOnePieces[i][1])-19
        currImage = data.playerOnePieces[i][2] 
        x2 = x1+currImage.width()
        y2 = y1+currImage.height() 
        if (x1 < event.x < x1+currImage.width()):
            if (y1 < event.y < y1+currImage.height()):
                data.tileNumber = i  
                
def playerOneAIKeyPressed(event,data):
    if event.keysym == "space":
        data.p1turn = True  
        data.p2turn = False 
        data.mode = "AI Player Two Game" 
        data.tileNumber = 0 
    if isHu(data.playerOneHand,data.playedTileName):
        data.p2win = True
        #data.winNumber = 2 

    if event.keysym == "Up" and len(data.playerOnePieces)>13:
       
        image = data.playerOnePieces[data.tileNumber][2]
        if data.played == []: 
            data.played.append([data.x2, data.y2, data.playerOnePieces[data.tileNumber][2]])
        elif data.played!=[]: 
          
            if 187<data.x2<500: 
                if data.p1peng == True or data.p1Chi == True: 
                    data.played.append([data.x2, data.y2, data.playerOnePieces[data.tileNumber][2]])
                else: 
                    data.x2 = data.x2+image.width()+7 
                    data.played.append([data.x2, data.y2, data.playerOnePieces[data.tileNumber][2]])
            elif data.x2>500:
                data.x2 = 235
                data.y2 += image.height()
                data.played.append([data.x2, data.y2, data.playerOnePieces[data.tileNumber][2]])

        data.playerOnePieces.pop(data.tileNumber)
        #names 
        data.playedTileName = data.playerOneHand[data.tileNumber]
        data.playerOneHand.remove(data.playedTileName)
        #shifting everything to the left 
        for i in range (data.tileNumber, len(data.playerOnePieces)):
            original = data.playerOnePieces[i][0]
            image = data.playerOnePieces[i][2]
            data.playerOnePieces[i][0] = original-image.width()-9
        data.p1turn = True
        data.chi = False 
        data.peng = False 
        data.p4turn = False 
        
    #re-putting the piece back in
    #r stands for random 
    if event.keysym == "r" and data.p1turn == False and len(data.playerOnePieces)<15:   
        length = len(data.playerOnePieces)-1
        randomKey = random.choice(data.keys) 
        randomTile = data.objectPics[randomKey]  
        data.playerOneHand.append(randomKey)
        data.playerOnePieces.append([(data.playerOnePieces[length][0]+(data.playerOnePieces[data.tileNumber][2]).width()+9), 600, randomTile])
    #print (isHu(data.playerOneHand))
    
        
def playerOneAIGameRedrawAll(canvas,data):
    canvas.create_text(125,60, text = "Player One's Turn!", font = "chalkboard 15")
    for picture in data.playerOnePieces:  
        canvas.create_image(picture[0], picture[1], image = picture[2])
    if data.chi == False and data.peng == False and data.p1turn == True: 
        canvas.create_text(280,145, text = "P1 has gone! Press the space bar for CP2 to go.", font = "BrushScriptMT 25", fill = "white")
    
    
    