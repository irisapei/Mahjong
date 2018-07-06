import random 
from hu import * 
def playerTwoAIMousePressed(event,data): 
    pass 
    
def playerTwoAIKeyPressed(event,data): 
    if event.keysym == "space":
        data.mode = "AI Player Three Game"
        data.p2turn = True 
        data.p3turn = False
    randomTileNumber = random.randint(0, 12)
    if event.keysym == "r" and data.p2turn == False and len(data.playerTwoPieces)<15:   
        length = len(data.playerTwoPieces)-1
        randomKey = random.choice(data.keys) 
        randomTile = data.objectPics[randomKey]  
        data.playerTwoHand.append(randomKey) 
        data.playerTwoPieces.append([(data.playerTwoPieces[length][0]+(data.playerTwoPieces[randomTileNumber][2]).width()+10), 600, randomTile])
        data.p2tookpiece = True 
    if isHu(data.playerTwoHand,data.playedTileName):
        data.p2win = True
        #data.winNumber = 2 
    if event.keysym == "Up":
        #randomTileNumber = random.randint(0, len(data.playerTwoPieces))
        image = data.playerTwoPieces[randomTileNumber][2]
        if data.played == []: 
            data.played.append([data.x2, data.y2, data.playerTwoPieces[randomTileNumber][2]])
        elif data.played!=[]: 
           
            if 187<data.x2<500: 
                if data.p2peng == True or data.p2Chi == True: 
                    
                    data.played.append([data.x2, data.y2, data.playerTwoPieces[randomTileNumber][2]])
                else: 
                    data.x2 = data.x2+image.width()+13 
                    data.played.append([data.x2, data.y2, data.playerTwoPieces[randomTileNumber][2]])
            elif data.x2>500:
                data.x2 = 235
                data.y2 += image.height()
                data.played.append([data.x2, data.y2, data.playerTwoPieces[randomTileNumber][2]])

        data.playerTwoPieces.pop(randomTileNumber)
        #names 
        data.leftturn = "Player Two"
        data.playedTileName = data.playerTwoHand[randomTileNumber]
        data.playerTwoHand.remove(data.playedTileName)
        data.p2turn = True
        data.p2tookpiece = False 
        data.peng = False
        data.chi = False
        data.p1turn = False 

def playerTwoAIGameRedrawAll(canvas,data):
    canvas.create_text(125,60, text = "CP2's Turn!", font = "chalkboard 15")
    if data.p2tookpiece == False and data.p2turn == False:
        canvas.create_text(600, 50, text = "Press R for CP2 to pick up a tile!", font = "GillSans", fill = "white")
    if data.p2tookpiece == True and data.peng == False: 
        canvas.create_text(600,100, text = "CP2 picked a random tile!",font = "GillSans", fill = "white")
        canvas.create_text(600, 130, text = "Press Up to see what CP2 will put out.",font = "GillSans", fill = "white")
    if data.p2turn == True and data.peng == False and data.chi == False: 
        canvas.create_text(280,145, text = "CP2 has gone! Press the space bar for CP3 to go.", font = "BrushScriptMT 25", fill = "white")

    if data.peng == True and len(data.playerTwoPieces)>13:

        canvas.create_text(500, 100, text = "CP2 Peng!",font = "GillSans", fill = "white")
        canvas.create_text(550,130, text = "Press Up to see what CP2 will put out.",font = "GillSans", fill = "white")
    if data.chi == True and len(data.playerTwoPieces)>13:
        canvas.create_text(200, 100, text = "CP2 Chi!",font = "GillSans", fill = "white")
        canvas.create_text(200,130, text = "Press Up to see what CP2 will put out.",font = "GillSans", fill = "white")
    

def playerTwoAITimerFired(data):
    pass

        