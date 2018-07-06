##################
#Drawing Generic Rest of Board/
##################
def drawBoard(canvas,data): 
    canvas.create_rectangle(10,10,data.width-10,data.height-10, fill = "dark green")
    canvas.create_rectangle(187, 160, 200, 550, fill = "white") 
    canvas.create_rectangle(187, 160, 561, 173, fill = "white")
    canvas.create_rectangle(561, 160, 574, 550, fill = "white")
    canvas.create_text(data.width//2, data.height//4, text = ("You've selected Tile "+str(data.tileNumber)), font = "courier 20") 
    canvas.create_rectangle(50,50, 350,75, fill = "white", width = 4)
    canvas.create_text(700, 40, text = "P1", fill = data.p1color)
    canvas.create_text(700, 60, text = "P2", fill = data.p2color)
    canvas.create_text(700, 80, text = "P3", fill = data.p3color)
    canvas.create_text(700, 100, text = "P4", fill = data.p4color)
    
    
def drawMiddleTiles(canvas,data): 
    if data.played!=None: 
        for tile in data.played: 
            canvas.create_image(tile[0], tile[1], image = tile[2]) 

