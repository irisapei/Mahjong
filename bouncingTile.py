#################
#Initial Bouncing Mahjong Tile 
#################
def bounce(data):
    image = data.icon 
    #going left/right
    if (data.headingRight== True):
        if (data.x1+image.width() > data.width):
            data.headingRight = False
        else:
            data.x1 += data.speed
    else:
        if (data.x1<0):
            data.headingRight=True
        else:
            data.x1-=data.speed
    #going up/down 
    if (data.headingDown == True):
        if (data.y1+image.height() > data.height):
            data.headingDown = False
        else:
            data.y1+=data.speed
    else: 
        if (data.y1<0):
            data.headingDown = True
        else:
            data.y1-= data.speed
