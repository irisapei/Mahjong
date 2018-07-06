import random 
from hu import * 
def playerThreeAIMousePressed(event,data): 
    pass 
    
def playerThreeAIKeyPressed(event,data): 
    if event.keysym == "space":
        data.mode = "AI Player Four Game"
        data.p3turn = True 
        data.p4turn = False
    randomTileNumber = random.randint(0, 12)
    if event.keysym == "r" and data.p3turn == False and len(data.playerThreePieces)<15:   
        length = len(data.playerThreePieces)-1
        randomKey = random.choice(data.keys) 
        randomTile = data.objectPics[randomKey]  
        data.playerThreeHand.append(randomKey) 
        data.playerThreePieces.append([(data.playerThreePieces[length][0]+(data.playerThreePieces[randomTileNumber][2]).width()+10), 600, randomTile])
        data.p3tookpiece = True 

    if isHu(data.playerThreeHand,data.playedTileName):
        data.p3win = True
        #data.winNumber = 3
        
    if event.keysym == "Up":
        
        image = data.playerThreePieces[randomTileNumber][2]
        if data.played == []: 
            data.played.append([data.x2, data.y2, data.playerThreePieces[randomTileNumber][2]])
        elif data.played!=[]: 
           
            if 187<data.x2<500: 
                if data.p3peng == True or data.p3Chi == True: 
                    
                    data.played.append([data.x2, data.y2, data.playerThreePieces[randomTileNumber][2]])
                else: 
                    
                    data.x2 = data.x2+image.width()+7 
                    data.played.append([data.x2, data.y2, data.playerThreePieces[randomTileNumber][2]])
            elif data.x2>500:
                data.x2 = 235
                data.y2 += image.height()
                data.played.append([data.x2, data.y2, data.playerThreePieces[randomTileNumber][2]])

        data.playerThreePieces.pop(randomTileNumber)
        #names 
        data.leftturn = "Player Three"
        data.playedTileName = data.playerThreeHand[randomTileNumber]
        data.playerThreeHand.remove(data.playedTileName)
        data.p3turn = True
        data.p3tookpiece = False 
        data.peng = False 
        data.chi = False 
        data.p2turn = False 

def playerThreeAIGameRedrawAll(canvas,data):
    canvas.create_text(125,60, text = "CP3's Turn!", font = "chalkboard 15")
    if data.p3tookpiece == False and data.p3turn == False:
        canvas.create_text(600, 50, text = "Press R for CP3 to pick up a tile!", font = "GillSans", fill = "white")
    if data.p3tookpiece == True and data.peng == False: 
        canvas.create_text(600,100, text = "CP3 picked a random tile!",font = "GillSans", fill = "white")
        canvas.create_text(600, 130, text = "Press Up to see what CP3 will put out.",font = "GillSans", fill = "white")
    if data.p3turn == True and data.peng == False and data.chi == False: 
        canvas.create_text(280,145, text = "CP3 has gone! Press the space bar for CP4 to go.", font = "BrushScriptMT 25", fill = "white")

    if data.peng == True and len(data.playerThreePieces)>13:

        canvas.create_text(550, 100, text = "CP3 Peng!",font = "GillSans", fill = "white")
        canvas.create_text(550,130, text = "Press Up to see what CP3 will put out.",font = "GillSans", fill = "white")
    if data.chi == True and len(data.playerThreePieces)>13:
        canvas.create_text(600, 100, text = "CP3 Chi!",font = "GillSans", fill = "white")
        canvas.create_text(600,130, text = "Press Up to see what CP3 will put out.",font = "GillSans", fill = "white")
    

def playerThreeAITimerFired(data):
    pass