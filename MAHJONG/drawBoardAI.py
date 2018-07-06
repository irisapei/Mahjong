##################
#Drawing Generic Rest of Board/
##################
def drawBoardAI(canvas,data): 
    canvas.create_rectangle(0,0,data.width,data.height, fill = "springgreen4")
    xstart = 175
    #top row 
    canvas.create_rectangle(175,160, 205,190, fill = "white")
    canvas.create_rectangle(205,160,235,190, fill = "white")
    canvas.create_rectangle(235,160,265,190, fill = "white")
    canvas.create_rectangle(265,160,295,190, fill = "white")
    canvas.create_rectangle(295,160,325,190, fill = "white")
    canvas.create_rectangle(325,160,355,190, fill = "white")
    canvas.create_rectangle(355,160,385,190, fill = "white")
    canvas.create_rectangle(385,160,415,190, fill = "white")
    canvas.create_rectangle(415,160,445,190, fill = "white")
    canvas.create_rectangle(445,160,475,190, fill = "white")
    canvas.create_rectangle(475,160,505,190, fill = "white")
    canvas.create_rectangle(505,160,535,190, fill = "white")
    canvas.create_rectangle(535,160,565,190, fill = "white")
    canvas.create_rectangle(565,160,595,190, fill = "white")
    #left row 
    canvas.create_rectangle(175,190, 205,220, fill = "white")
    canvas.create_rectangle(175,220, 205,250, fill = "white")
    canvas.create_rectangle(175,250, 205,280, fill = "white")
    canvas.create_rectangle(175,280, 205,310, fill = "white")
    canvas.create_rectangle(175,310, 205,340, fill = "white")
    canvas.create_rectangle(175,340, 205,370, fill = "white")
    canvas.create_rectangle(175,370, 205,400, fill = "white")
    canvas.create_rectangle(175,400, 205,430, fill = "white")
    canvas.create_rectangle(175,430, 205,460, fill = "white")
    canvas.create_rectangle(175,460, 205,490, fill = "white")
    canvas.create_rectangle(175,490, 205,520, fill = "white")
    canvas.create_rectangle(175,520, 205,550, fill = "white")
    #right row 
    canvas.create_rectangle(565,190, 595,220, fill = "white")
    canvas.create_rectangle(565,220, 595,250, fill = "white")
    canvas.create_rectangle(565,250, 595,280, fill = "white")
    canvas.create_rectangle(565,280, 595,310, fill = "white")
    canvas.create_rectangle(565,310, 595,340, fill = "white")
    canvas.create_rectangle(565,340, 595,370, fill = "white")
    canvas.create_rectangle(565,370, 595,400, fill = "white")
    canvas.create_rectangle(565,400, 595,430, fill = "white")
    canvas.create_rectangle(565,430, 595,460, fill = "white")
    canvas.create_rectangle(565,460, 595,490, fill = "white")
    canvas.create_rectangle(565,490, 595,520, fill = "white")
    canvas.create_rectangle(565,520, 595,550, fill = "white")
    canvas.create_rectangle(50,50, 350,75, fill = "white", width = 4)
    if data.gametype == "Multiplayer":
        canvas.create_text(750, 40, text = "P1", fill = data.p1color, font = "Papyrus")
        canvas.create_text(750, 60, text = "P2", fill = data.p2color, font = "Papyrus")
        canvas.create_text(750, 80, text = "P3", fill = data.p3color, font = "Papyrus")
        canvas.create_text(750, 100, text = "P4", fill = data.p4color, font = "Papyrus")
    elif data.gametype == "AI": 
        canvas.create_text(750, 40, text = "P1", fill = data.p1color, font = "Papyrus")
        canvas.create_text(750, 60, text = "CP2", fill = data.p2color, font = "Papyrus")
        canvas.create_text(750, 80, text = "CP3", fill = data.p3color, font = "Papyrus")
        canvas.create_text(750, 100, text = "CP4", fill = data.p4color, font = "Papyrus")
    canvas.create_rectangle(50, 100, 350, 125, fill = "white", width = 4)
    canvas.create_text(175,115, text = ("You've selected Tile "+str(data.tileNumber)), font = "courier 15") 
    
def drawMiddleTiles(canvas,data): 
    if data.played!=None: 
        for tile in data.played: 
            canvas.create_image(tile[0], tile[1], image = tile[2]) 