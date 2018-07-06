import copy 
######CHI 
def containsConsecutive(list):
    list.sort() 
    counter = 0 
    if len(list)>2:
        for i in range (len(list)-1):
            if counter ==1 :
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
        
        if containsConsecutive(bingNumbers) == False:
            bingNumbers.append(nameValuesBing[givenTile])
            if containsConsecutive(bingNumbers):
                return True 
    return False 


#################
#The first Hu instance: results from a random Tile getting put in your deck 

def containsPeng(hand): 
    for i in hand:
        if hand.count(i) == 3:
            return True 
            
def countsPeng(hand):
    seen = set() 
    counter = 0 
    for i in hand:
        if hand.count(i) == 3:
            seen.add(i)
    for j in seen: 
        if hand.count(j) == 3:
            counter+=3 
    return counter 

def containsChi(hand):
    wanTiles, tiaoTiles, bingTiles = [], [], []
    nameValuesWan = {"yiwan":1, "erwan":2, "sanwan":3, "siwan":4, "wuwan":5, "liuwan":6, "qiwan":7, "bawan": 8, "jiuwan":9} 
    
    nameValuesTiao = {"yitiao":1, "ertiao":2, "santiao":3, "sitiao":4, "wutiao":5, "liutiao":6, "qitiao":7, "batiao": 8, "jiutiao":9} 
    
    nameValuesBing = {"yibing":1, "liangbing":2, "sanbing":3, "sibing":4, "wubing":5, "liubing":6, "qibing":7, "babing": 8, "jiubing":9}
    #adds each type of tile to their own individual list 
    for tile in hand: 
        if "wan" in tile: wanTiles.append(tile)
        elif "tiao" in tile: tiaoTiles.append(tile)
        elif "bing" in tile: bingTiles.append(tile)
    wanNumbers, tiaoNumbers, bingNumbers = [], [], []  
    if wanTiles!=[]:
        for wan in wanTiles: 
            wanNumbers.append(nameValuesWan[wan])
            if containsConsecutive(wanNumbers):
                return True 
    if tiaoTiles !=[]:
        for tiao in tiaoTiles: 
            tiaoNumbers.append(nameValuesTiao[tiao])
            if containsConsecutive(tiaoNumbers):
                    
                return True 
    if bingTiles !=[]:
        for bing in bingTiles: 
            bingNumbers.append(nameValuesBing[bing])
            if containsConsecutive(bingNumbers):
                return True 
    return False 
def countsChi(hand): 
    counter = 0 
    wanTiles, tiaoTiles, bingTiles = [], [], []
    nameValuesWan = {"yiwan":1, "erwan":2, "sanwan":3, "siwan":4, "wuwan":5, "liuwan":6, "qiwan":7, "bawan": 8, "jiuwan":9} 
    
    nameValuesTiao = {"yitiao":1, "ertiao":2, "santiao":3, "sitiao":4, "wutiao":5, "liutiao":6, "qitiao":7, "batiao": 8, "jiutiao":9} 
    
    nameValuesBing = {"yibing":1, "liangbing":2, "sanbing":3, "sibing":4, "wubing":5, "liubing":6, "qibing":7, "babing": 8, "jiubing":9}
    
    reverseWan = {1:"yiwan", 2: "erwan", 3: "sanwan", 4:"siwan", 5: "wuwan", 6: "liuwan", 7 :"qiwan", 8: "bawan", 9 : "jiuwan"}
    reverseTiao= {1:"yitiao", 2: "ertiao", 3: "santiao", 4:"sitiao", 5: "wutiao", 6: "liutiao", 7 :"qitiao", 8: "batiao", 9 : "jiutiao"}
    reverseBing= {1:"yibing", 2: "liangbing", 3: "sanbing", 4:"sibing", 5: "wubing", 6: "liubing", 7 :"qibing", 8: "babing", 9 : "jiubing"}
    answer = []
    newList = [] 
    othersList = [] 
    #adds each type of tile to their own individual list 
    for tile in hand: 
        if "wan" in tile: wanTiles.append(tile)
        elif "tiao" in tile: tiaoTiles.append(tile)
        elif "bing" in tile: bingTiles.append(tile)
    wanNumbers, tiaoNumbers, bingNumbers = [], [], [] 
    #print (wanTiles)
    for wan in wanTiles: 
        wanNumbers.append(nameValuesWan[wan])
        #print (wanNumbers)
    if containsConsecutive(wanNumbers):
        counter+=3
    for tiao in tiaoTiles: 
        tiaoNumbers.append(nameValuesTiao[tiao])
    if containsConsecutive(tiaoNumbers):
        counter+=3 
    for bing in bingTiles: 
        bingNumbers.append(nameValuesBing[bing])
    if containsConsecutive(bingNumbers):
        #print ("!!")
        counter+=3 
    return counter

hand = ['yiwan', 'erwan', "sanwan", 'wuwan', 'wuwan', 'wuwan', 'yitiao', 'yitiao', 'yitiao', 'siwan', 'siwan', 'siwan', 'Fa']
playedTile = "Fa"

def containsDouble(hand):
    counter = 0 
    for i in hand:
        if hand.count(i) == 2:
            counter +=2 
            return counter
    return 0 


def isHu(hand, playedTile):
    hand1 = copy.deepcopy(hand) 
    hand1.append(playedTile)
    #print (hand)
    pengNumber = countsPeng(hand1)
    #print (pengNumber)
    chiNumber = countsChi(hand1)
    doubleNumber = containsDouble(hand1)
    answer = pengNumber+chiNumber+doubleNumber
    if answer == 14 and len(hand1)<15: 
        return True 
    return False 


    
    
