def ispeng(lst, givenTile):
    wanTiles, tiaoTiles, bingTiles, characters = [], [], [], [] 
    for tile in lst: 
        if "wan" in tile: wanTiles.append(tile)
        elif "tiao" in tile: tiaoTiles.append(tile)
        elif "bing" in tile: bingTiles.append(tile)
        else: characters.append(tile)
    if givenTile != None: 
    #peng for the wan tiles 
        if len(wanTiles)> 2: 
            seenWan = set()
            for wan in wanTiles: 
                if wan not in seenWan: seenWan.add(wan) 
                for i in seenWan: 
                    if wanTiles.count(i)==2:
                        if "wan" in givenTile:
                            if givenTile == i: return True 
                            else: continue 
        #peng for the tiao tiles 
        if len(tiaoTiles)> 2: 
            seenTiao = set() 
            for tiao in tiaoTiles: 
                if tiao not in seenTiao: seenTiao.add(tiao) 
                for i in seenTiao:
                    if tiaoTiles.count(i) == 2:
                        if "tiao" in givenTile: 
                            if givenTile == i: return True 
                            else: continue 
        #peng for the bing tiles 
        if len(bingTiles)> 2: 
            seenBing = set()
            for bing in bingTiles: 
                if bing not in seenBing: seenBing.add(bing) 
                for i in seenBing:
                    if bingTiles.count(i)==2: 
                        if "bing" in givenTile: 
                            if givenTile == i: 
                                if bingTiles.count(i) ==2: return True
                        else:continue  
        #peng for character tiles 
        if len(characters)> 2: 
            seenChar = set()
            for char in characters: 
                if char not in seenChar: seenChar.add(char) 
                for i in seenChar:
                    if characters.count(i)==2:
                        if givenTile == i: return True 
    return False 
    
    
def pengRedrawAll(canvas,data):  
    if data.p1turn == False and ispeng(data.playerOneHand, data.playedTileName) and data.leftturn != "Player One":
        #print (data.playerOneHand)
        #print (data.playedTileName)
        data.peng = True
        canvas.create_text(90, 500, text = "Player One can Peng!", font = "BrushScriptMT 20", fill = "white")
        canvas.create_text(90, 550, text = "Press P to Peng!", font = "BrushScriptMT 20", fill = "white") 
        data.p1turn = False 
        data.p1peng = True 

    #player two peng works out 
    if ispeng(data.playerTwoHand, data.playedTileName) and data.p2tookpiece == False and data.p2turn == False and data.leftturn!="Player Two":
        #print (data.playerTwoHand)
        #print (data.playedTileName)
        canvas.create_text(90, 500, text = "Player Two can Peng!", font = "BrushScriptMT 20", fill = "white")
        canvas.create_text(90, 550, text = "Press P to Peng!", font = "BrushScriptMT 20", fill = "white")  
        data.p2turn = False 
        data.p2peng = True 
        data.peng = True 
        
    # player three peng works out 
    if ispeng(data.playerThreeHand, data.playedTileName) and data.p3tookpiece == False and data.p3turn == False and data.leftturn!="Player Three": 
        #print (data.playerThreeHand)
        #print (data.playedTileName)
        canvas.create_text(90, 500, text = "Player Three can Peng!", font = "BrushScriptMT 20", fill = "white")
        canvas.create_text(90, 550, text = "Press P to Peng!", font = "BrushScriptMT 20", fill = "white")  
        data.p3turn = False 
        data.p3peng = True 
        data.peng = True 
        
    #player 4 peng works out 
    if ispeng(data.playerFourHand,data.playedTileName) and data.p4tookpiece == False and data.p4turn == False and data.leftturn!="Player Four":
        #print (data.playerFourHand)
        #print (data.playedTileName)
        canvas.create_text(90, 500, text = "Player Four can Peng!", font = "BrushScriptMT 20", fill = "white")
        canvas.create_text(90, 550, text = "Press P to Peng!", fill = "white", font = "BrushScriptMT 20") 
        data.p4turn = False 
        data.p4peng = True 
        data.peng = True 


def pengKeyPressed(event,data):    
    if event.keysym == "p" or event.keysym == "P":
        #player one peng
        if data.p1peng == True: 
            if data.played!=[]:
                tile = data.played.pop()
            data.mode = "Player One Game" 
            length = len(data.playerOnePieces)-1
            data.playerOneHand.append(data.playedTileName) 
            #print (data.playerOnePieces) 
            #print (data.tileNumber)
            tile[0] = data.playerOnePieces[length][0]+(data.playerOnePieces[data.tileNumber][2]).width()+7
            tile[1] = 600
            data.playerOnePieces.append(tile) 
        #data.p1peng = False 
        #player 2 peng 
        if data.p2peng == True:
            if data.played !=[]:
                tile = data.played.pop()
            data.mode = "Player Two Game" 
            length = len(data.playerTwoPieces)-1
            data.playerTwoHand.append(data.playedTileName) 
            tile[0] = data.playerTwoPieces[length][0]+(data.playerTwoPieces[data.tileNumber][2]).width()+7
            tile[1] = 600
            data.playerTwoPieces.append(tile) 
        #data.p2peng = False 
        
        #player 3 peng 
        if data.p3peng == True: 
            if data.played!=[]:
                tile = data.played.pop()
            data.mode = "Player Three Game" 
            length = len(data.playerThreePieces)-1
            data.playerThreeHand.append(data.playedTileName) 
            #print (data.playerThreePieces) 
            #print (data.tileNumber)
            tile[0] = data.playerThreePieces[length][0]+(data.playerThreePieces[data.tileNumber][2]).width()+7
            tile[1] = 600
            data.playerThreePieces.append(tile) 
        #data.p3peng = False 
        
        #player 4 peng 
        if data.p4peng == True:
            if data.played!=[]:
                tile = data.played.pop()
            data.mode = "Player Four Game"
            length = len(data.playerFourPieces)-1
            data.playerFourHand.append(data.playedTileName) 
            #print (data.playerFourPieces) 
            #print (data.tileNumber) 
            tile[0] = data.playerFourPieces[length][0]+(data.playerFourPieces[data.tileNumber][2]).width()+7
            tile[1]=600
            data.playerFourPieces.append(tile) 
        #data.p4peng = False 
    data.p1peng = False
    data.p2peng = False
    data.p3peng = False
    data.p4peng = False
    #data.peng = False 