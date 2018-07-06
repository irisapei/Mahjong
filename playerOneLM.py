import random 
from hu import * 
# Player One 
def playerOneMousePressed(event,data):
    for i in range (len(data.playerOnePieces)):
        x1 = (data.playerOnePieces[i][0])-19
        y1 = (data.playerOnePieces[i][1])-19
        currImage = data.playerOnePieces[i][2] 
        x2 = x1+currImage.width()
        y2 = y1+currImage.height() 
        if (x1 < event.x < x1+currImage.width()):
            if (y1 < event.y < y1+currImage.height()):
                data.tileNumber = i  
                
def playerOneKeyPressed(event,data): 
    if event.keysym == "space":
        data.mode = "Player Two Game"
        data.p1turn = True  
        data.p2turn = False 
        data.tileNumber = 0 
        data.leftturn = "Player One"
        #print (isHu(data.playerOneHand))
        #print (data.playerOneHand)
    if event.keysym == "Up" and len(data.playerOnePieces)>13:
        image = data.playerOnePieces[data.tileNumber][2]
        if data.played == []: 
            data.played.append([data.x2, data.y2, data.playerOnePieces[data.tileNumber][2]])
        elif data.played!=[]: 
            if 187<data.x2<500: 
                if data.chi == True or data.peng == True: 
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
        data.leftturn = "Player One"
        data.p1turn = True
        data.p1tookpiece = False 
        data.chi = False 
        data.peng = False 
    #re-putting the piece back in
    #r stands for random 
    if event.keysym == "r" and data.p1turn == False: 
        #print ("!")
        length = len(data.playerOnePieces)-1
        randomKey = random.choice(data.keys) 
        randomTile = data.objectPics[randomKey]  
        data.playerOneHand.append(randomKey) 
        data.playerOnePieces.append([(data.playerOnePieces[length][0]+(data.playerOnePieces[data.tileNumber][2]).width()+13), 600, randomTile])
       

    
        
def playerOneGameRedrawAll(canvas,data):
    canvas.create_text(150,60, text = "Player One's Turn!", font = "chalkboard 15")
   # print (len(data.wtf))
    for picture in data.playerOnePieces:  
        canvas.create_image(picture[0], picture[1], image = picture[2])
    if data.p1turn == True and data.peng == False and data.chi == False: 
        canvas.create_text(280,145, text = "P1 has gone! Press the space bar to advance to P2's turn.", font = "BrushScriptMT 25", fill = "white")

    
    
    