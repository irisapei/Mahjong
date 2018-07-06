from hu import *
def winDrawing(canvas,data):
    if data.playedTileName!="":
        if isHu(data.playerOneHand,data.playedTileName):
            data.p1win = True
        elif isHu(data.playerTwoHand,data.playedTileName):
            data.p2win = True 
        elif isHu(data.playerThreeHand,data.playedTileName):
            data.p3win = True 
        elif isHu(data.playerFourHand,data.playedTileName):
            data.p4win = True 
    if data.p1win == True:
        length = len(data.playerOnePieces)-1
        if len(data.playerOnePieces)<14:
            tile = data.objectPics[data.playedTileName]  
            data.playerOnePieces.append([(data.playerOnePieces[length][0]+(data.playerOnePieces[data.tileNumber][2]).width()+9), 600, tile])
        canvas.create_rectangle(0,0,data.width,data.height, fill = "springgreen4")
        canvas.create_rectangle(200,200,600,300, fill = "black")
        canvas.create_text (400, 250, text = "PLAYER ONE WINS!", fill = "white", font = "Monaco 35")
        #print (len(data.playerOnePieces))
        for piece in data.playerOnePieces:
            canvas.create_image(piece[0], piece[1], image = piece[2])
    elif data.p2win == True:
        length = len(data.playerTwoPieces)-1
        tile = data.objectPics[data.playedTileName]  
        data.playerTwoPieces.append([(data.playerTwoPieces[length][0]+(data.playerTwoPieces[data.tileNumber][2]).width()+9), 600, tile])
        canvas.create_rectangle(0,0,data.width,data.height, fill = "springgreen4")
        canvas.create_rectangle(200,200,600,300, fill = "black")
        canvas.create_text (400, 250, text = "PLAYER TWO WINS!", fill = "white", font = "Monaco 35")
        for piece in data.playerTwoPieces:
            canvas.create_image(piece[0], piece[1], image = piece[2])
    elif data.p3win == True:
        length = len(data.playerThreePieces)-1
        tile = data.objectPics[data.playedTileName]  
        data.playerThreePieces.append([(data.playerThreePieces[length][0]+(data.playerThreePieces[data.tileNumber][2]).width()+9), 600, tile])
        canvas.create_rectangle(0,0,data.width,data.height, fill = "springgreen4")
        canvas.create_rectangle(200,200,600,300, fill = "black")
        canvas.create_text (400, 250, text = "PLAYER THREE WINS!", fill = "white", font = "Monaco 35")
        for piece in data.playerThreePieces:
            canvas.create_image(piece[0], piece[1], image = piece[2])
    elif data.p4win == True:
        length = len(data.playerFourPieces)-1
        tile = data.objectPics[data.playedTileName]  
        data.playerFourPieces.append([(data.playerFourPieces[length][0]+(data.playerOnePieces[data.tileNumber][2]).width()+9), 600, tile])
        canvas.create_rectangle(0,0,data.width,data.height, fill = "springgreen4")
        canvas.create_rectangle(200,200,600,300, fill = "black")
        canvas.create_text (400, 250, text = "PLAYER Four WINS!", fill = "white", font = "Monaco 35")
        for piece in data.playerFourPieces:
            canvas.create_image(piece[0], piece[1], image = piece[2])