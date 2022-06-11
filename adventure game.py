#Student's Name
#Professor's Name
#Course
#Date
                #########Shadow Demon Adventure Text Game#############
rooms = {
        'ColdHarbor Hall': {'North': 'Slaughterhouse', 'East': 'Arcane Library', 'South': 'Putrid Garden',
                            'West': 'Crystal Cave','item':'An Empty room; go north, east, south or west'},
        'Crystal Cave': { 'East': 'ColdHarbor Hall', 'item':'A Ward Crystal'},
        'Slaughterhouse': {'East': 'Coliseum', 'South': 'ColdHarbor Hall','item':'Food'},
        'Coliseum': {'West': 'Slaughterhouse', 'South': 'Arcane Library',
                     'item':'An Obsidian Sword and Quartz Shield'},
        'Arcane Library': {'North': 'Coliseum', 'East': 'ColdHarbor Hall',
                           'South': 'Blacksmiths Forge','item':'A Book of Spells'},
        'Blacksmiths Forge': {'North': 'Arcane Library', 'South': 'Boss Room',
                              'item':'A Diamond Armor and Helmet'},
        'Boss Room': {'North': 'Blacksmiths Forge', 'West': 'Putrid Garden',
                      'item':'The Shadow Demons throne Room; go north or west to get more items'},
        'Putrid Garden': {'East': 'Boss Room', 'North': 'ColdHarbor Hall',
                          'item':'An Ascendent Mushroom (consumable)'}
    } #This states the rooms and their possible directions

current_room = 'ColdHarbor Hall' #This sets the starting room
running= True #is True if the player is playing the game, otherwise, it ends the game when player types exit

#Used to change rooms when player moves to a specific direction
def get_new_room(current_room, direction):
    new_room = current_room
    for i in rooms:
        if i == current_room:
            if direction in rooms[i]:
                new_room = rooms[i][direction]
    return new_room

#gets items from romms
def get_item(current_room):
    return rooms[current_room]['item']

#prints game instructions
def instructions():
    print('Shadow Demon Text Adventure Game')
    print('Collect items to win the game, or be terminated by the Shadow Demon.')
    print('Move commands: go North, go South, go East, go West')
    print("Add to Inventory: get 'item name'")
    print('Type "Exit" to exit the game.')
instructions() #displays instructions
inventory = [] #Sets the starting inventory at 0

#Game Loop
while running:  #This runs game when player doesn't type 'Exit'
    print('You are in', current_room)    #This states current room
    print('Inventory:', inventory)
    item = get_item(current_room)          #This specifies item in the room
    print('You see', '---->', item)
    #Allow player to collect an item in the current room or move to a different room
    direction = input('Enter your move:')
    if (direction == 'go East' or direction == 'go West' or direction == 'go North' or direction == 'go South'):
        direction = direction[3:]
        new_room = get_new_room(current_room, direction)  #Changes room based on player's direction
        #Gets and display the possible directions of a room
        possible_moves= list(rooms[new_room].keys())[:-1]
        print('-'*5,"Possible moves: ", *possible_moves, 'or get','-'*5)
        if new_room == current_room: #Error message if player's direction is unchanged
            print('You are about to run into the dark! Enter another direction!')
        else:
            current_room = new_room #Changes location
    elif direction == 'Exit': #if player types 'Exit', the game quits
        running= False
    elif direction == 'get':   #Lets player collect current room items
        if item in inventory:
            print('You already have that item! Collect the others!') #Stops player from recollecting an item
        else:
            inventory.append(item) #Adds item to inventory
            print('-'*5,"Possible moves: ", *possible_moves, 'or get','-'*5)
    else:
        print('invalid move!') #Error message when player makes an invalid input
    #Counts inventory items and returns a message when all items are collected
    if len(inventory) == 6:
        print('Congratulations! You have collected all items')
        running= False