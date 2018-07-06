import random 
from hu import *
def playerFourAIMousePressed(event,data): 
    pass 
    
def playerFourAIKeyPressed(event,data): 
    if event.keysym == "space":
        data.mode = "AI Player One Game"
        data.p4turn = True
        data.p1turn = False
        
    randomTileNumber = random.randint(0, 12)
    if event.keysym == "r" and data.p4turn == False and len(data.playerFourPieces)<15:   
        length = len(data.playerFourPieces)-1
        randomKey = random.choice(data.keys) 
        randomTile = data.objectPics[randomKey]  
        data.playerFourHand.append(randomKey) 
        data.playerFourPieces.append([(data.playerFourPieces[length][0]+(data.playerFourPieces[randomTileNumber][2]).width()+10), 600, randomTile])
    if isHu(data.playerFourHand, data.playedTileName):
        data.p4win = True 
        #data.winNumber = 4 
    data.p4tookpiece = True 
    if event.keysym == "Up":
        #randomTileNumber = random.randint(0, len(data.playerFourPieces))
        image = data.playerFourPieces[randomTileNumber][2]
        if data.played == []: 
            data.played.append([data.x2, data.y2, data.playerFourPieces[randomTileNumber][2]])
        elif data.played!=[]: 
           
            if 187<data.x2<500: 
                if data.p4peng == True or data.p4Chi == True: 
                    
                    data.played.append([data.x2, data.y2, data.playerFourPieces[randomTileNumber][2]])
                else: 
                    data.x2 = data.x2+image.width()+7 
                    data.played.append([data.x2, data.y2, data.playerFourPieces[randomTileNumber][2]])
            elif data.x2>500:
                data.x2 = 235
                data.y2 += image.height()
                data.played.append([data.x2, data.y2, data.playerFourPieces[randomTileNumber][2]])

        data.playerFourPieces.pop(randomTileNumber)
        #names 
        data.leftturn = "Player Four"
        data.playedTileName = data.playerFourHand[randomTileNumber]
        data.playerFourHand.remove(data.playedTileName)
        data.p4turn = True
        data.p4tookpiece = False 
        data.chi = False 
        data.peng = False 
        data.p3turn = False 
def playerFourAIGameRedrawAll(canvas,data):
    canvas.create_text(125,60, text = "CP4's Turn!", font = "chalkboard 15")
    if data.p4tookpiece == False and data.p4turn == False:
        canvas.create_text(600, 50, text = "Press R for CP4 to pick up a tile!", font = "GillSans", fill = "white")
    if data.p4tookpiece == True and data.peng == False: 
        canvas.create_text(600,100, text = "CP4 picked a random tile!",font = "GillSans", fill = "white")
        canvas.create_text(600, 130, text = "Press Up to see what CP4 will put out.",font = "GillSans", fill = "white")
    if data.p4turn == True and data.peng == False and data.chi == False: 
        canvas.create_text(280,145, text = "CP4 has gone! Press the space bar for P1 to go.", font = "BrushScriptMT 25", fill = "white")

    if data.peng == True and len(data.playerFourPieces)>13:
        canvas.create_text(500, 100, text = "CP4 Peng!",font = "GillSans", fill = "white")
        canvas.create_text(550,130, text = "Press Up to see what CP4 will put out.",font = "GillSans", fill = "white")
    if data.chi == True and len(data.playerFourPieces)>13:
        canvas.create_text(200, 100, text = "CP4 Chi!",font = "GillSans", fill = "white")
        canvas.create_text(200,130, text = "Press Up to see what CP4 will put out.",font = "GillSans", fill = "white")
def playerFourAITimerFired(data):
    pass