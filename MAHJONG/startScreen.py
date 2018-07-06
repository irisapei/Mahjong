#################
#Start Screen
#################
def startScreenRedrawAll(canvas,data): 
    if data.blink == False:
        canvas.create_text(390, 60, text = "WELCOME TO MAHJONG", font = "Monaco 50")
    canvas.create_text(390, 160, text = "Click to play with a certain mode!", font  = "Chalkboard 25") 
    canvas.create_rectangle(325,275, 475, 325, fill = "white", width = 5 )
    canvas.create_rectangle(325, 350, 475, 400, fill = "white", width = 5 )
    canvas.create_text(400,300, text = "MULTIPLAYER", font = "papyrus 15 bold")
    canvas.create_text(400,375, text = "AI", font = "papyrus 15 bold")
    canvas.create_text(400, 200, text = "Press H for help!", font = "Chalkboard 20")
    if data.chicken == True: 
        canvas.create_image(100,100, image = data.realicon)
    
def startScreenTimerFired(data):
    pass
def startScreenMousePressed(event,data):
    if 325<event.x<475 and 275<event.y<325: 
        data.mode = "Player One Game"
        data.playingGame = True 
        data.chicken = False 
        data.gametype = "Multiplayer" 
    elif 325<event.x<475 and 350<event.y<400: 
        data.mode = "AI Player One Game"
        data.playerGame = True 
        data.chicken = False 
        data.gametype = "AI" 

def startScreenKeyPressed(event,data):
    if event.keysym == "h":
        data.mode = "Help" 
        
   
    
