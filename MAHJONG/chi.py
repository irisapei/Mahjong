import copy 
def containsConsecutive(list):
    list.sort() 
    counter = 0 
    if len(list)>2:
        for i in range (len(list)-1):
            if counter ==2 :
                return True 
            if list[i]+1 == list[i+1]:
                counter +=1
            if list[i]+1 != list[i+1]:
                counter = 0
    return False 

def isChi(lst, givenTile):
    wanTiles, tiaoTiles, bingTiles = [], [], []
    nameValuesWan = {"yiwan":1, "erwan":2, "sanwan":3, "siwan":4, "wuwan":5, "liuwan":6, "qiwan":7, "bawan": 8, "jiuwan":9} 
    
    nameValuesTiao = {"yitiao":1, "ertiao":2, "santiao":3, "sitiao":4, "wutiao":5, "liutiao":6, "qitiao":7, "batiao": 8, "jiutiao":9} 
    
    nameValuesBing = {"yibing":1, "liangbing":2, "sanbing":3, "sibing":4, "wubing":5, "liubing":6, "qibing":7, "babing": 8, "jiubing":9}
    #adds each type of tile to their own individual list 
    for tile in lst: 
        if "wan" in tile: wanTiles.append(tile)
        elif "tiao" in tile: tiaoTiles.append(tile)
        elif "bing" in tile: bingTiles.append(tile)
    wanNumbers, tiaoNumbers, bingNumbers = [], [], []  
    if "wan" in givenTile: 
        for wan in wanTiles: 
            wanNumbers.append(nameValuesWan[wan])
        if containsConsecutive(wanNumbers) == False:
            wanNumbers.append(nameValuesWan[givenTile])
            if containsConsecutive(wanNumbers):
                return True 
    elif "tiao" in givenTile:  
        for tiao in tiaoTiles: 
            tiaoNumbers.append(nameValuesTiao[tiao])
        if containsConsecutive(tiaoNumbers) == False:
            tiaoNumbers.append(nameValuesTiao[givenTile])
            if containsConsecutive(tiaoNumbers):
                return True 
    elif "bing" in givenTile: 
        for bing in bingTiles: 
            bingNumbers.append(nameValuesBing[bing])
        #print (bingNumbers)
        if containsConsecutive(bingNumbers) == False:
            bingNumbers.append(nameValuesBing[givenTile])
            #print (bingNumbers)
            if containsConsecutive(bingNumbers):
                return True 
    return False 



def chiRedrawAll(canvas,data):  
    #player one Chi works out 
    if isChi(data.playerOneHand, data.playedTileName) and data.p1turn == False and data.leftturn == "Player Four" and len(data.playerOneHand)<14 and data.peng==False:
        #print (data.playerOneHand)
        #print (data.playedTileName)
        canvas.create_text(90, 500, text = "Player One can Chi!", font = "BrushScriptMT 20 ", fill = "white")
        canvas.create_text(90, 550, text = "Press C to Chi!", font = "BrushScriptMT 20", fill = "white")
        data.chi = True 
        data.p1turn = False 
        data.p1Chi = True 
   

    #player two Chi works out 
    if isChi(data.playerTwoHand, data.playedTileName)and data.p2tookpiece == False and data.p2turn == False and data.leftturn == "Player One" and len(data.playerTwoHand)<14 and data.peng == False:
        #print (data.playerTwoHand)
        #print (data.playedTileName)
        canvas.create_text(90, 500, text = "Player Two can Chi!", font = "BrushScriptMT 20", fill = "white")
        canvas.create_text(90, 550, text = "Press C to Chi", font = "BrushScriptMT 20", fill = "white") 
        data.chi = True 
        data.p2turn = False 
        data.p2Chi = True 
    #data.chi = True 
    
    if isChi(data.playerThreeHand, data.playedTileName) and data.p3tookpiece == False and data.p3turn == False and data.leftturn == "Player Two" and len(data.playerThreeHand)<14 and data.peng == False: 
       # print (data.playerThreeHand)
        #print (data.playedTileName)
        canvas.create_text(90, 500, text = "Player Three can Chi!", font = "BrushScriptMT 20 ", fill = "white")
        canvas.create_text(90, 550, text = "Press C to Chi!", font = "BrushScriptMT 20 ", fill = "white")
        data.chi = True  
        data.p3turn = False 
        data.p3Chi = True 
   
        
    #player 4 Chi works out 
    if isChi(data.playerFourHand,data.playedTileName) and data.p4tookpiece == False and data.p4turn == False and data.leftturn == "Player Three" and len(data.playerFourHand)<14 and data.peng == False: 
       # print (data.playerFourHand)
        #print (data.playedTileName)
        canvas.create_text(90, 500, text = "Player Four can Chi!", font = "BrushScriptMT 20 ", fill = "white")
        canvas.create_text(90, 550, text = "Press C to Chi", font = "BrushScriptMT 20", fill = "white")
        data.chi = True 
        data.p4turn = False 
        data.p4Chi = True 
  

def chiKeyPressed(event,data):    
    if event.keysym == "c" or event.keysym == "C":
        
        if data.p1Chi == True and data.p1peng == False and data.p2peng == False and data.p3peng == False and data.p4peng == False and data.leftturn == "Player Four": 
            if data.played!=[]:
                tile = data.played.pop()
            data.mode = "Player One Game" 
            length = len(data.playerOnePieces)-1
            data.playerOneHand.append(data.playedTileName) 
            tile[0] = data.playerOnePieces[length][0]+37
            tile[1] = 600
            data.playerOnePieces.append(tile) 
       
       
        #player 2 Chi 
        if data.p2Chi == True and data.p1peng == False and data.p2peng == False and data.p3peng == False and data.p4peng == False and data.leftturn == "Player One":
            if data.played!=[]:
                tile = data.played.pop()
            data.mode = "Player Two Game" 
            length = len(data.playerTwoPieces)-1
            data.playerTwoHand.append(data.playedTileName) 
            #tile = data.played.pop()
           # print (length)
            #print (data.playerTwoPieces)
            #print (data.playerTwoPieces[length][0])
            #print (data.playerTwoPieces[data.tileNumber][2])
            tile[0] = data.playerTwoPieces[length][0]+(data.playerTwoPieces[data.tileNumber][2]).width()+7
            tile[1] = 600 
            data.playerTwoPieces.append(tile) 
       
        
        #player 3 Chi 
        if data.p3Chi == True and data.p1peng == False and data.p2peng == False and data.p3peng == False and data.p4peng == False and data.leftturn == "Player Two": 
            if data.played!=[]:
                tile = data.played.pop()
            data.mode = "Player Three Game" 
            length = len(data.playerThreePieces)-1
            data.playerThreeHand.append(data.playedTileName) 
            #tile = data.played.pop() 
            tile[0] = data.playerThreePieces[length][0]+(data.playerThreePieces[data.tileNumber][2]).width()+7
            tile[1] = 600
            data.playerThreePieces.append(tile) 
       
        #player 4 Chi 
        if data.p4Chi == True and data.p1peng == False and data.p2peng == False and data.p3peng == False and data.p4peng == False and data.leftturn == "Player Three":
            if data.played!=[]:
                tile = data.played.pop()
            data.mode = "Player Four Game"
            length = len(data.playerFourPieces)-1
            data.playerFourHand.append(data.playedTileName) 
            #tile = data.played.pop()
            tile[0] = data.playerFourPieces[length][0]+(data.playerFourPieces[data.tileNumber][2]).width()+7
            tile[1]=600
            data.playerFourPieces.append(tile) 
  