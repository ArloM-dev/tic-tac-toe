import random

#name the functions you want to use here
def player_1(data):
    #replace user_bot with your function
    return user_bot(data,1)
def player_2(data):
    #replace user_bot with your function
    return user_bot(data,2)

#bot aiding functions:

#detects if there is a winning possition for a player
def is_danger(z,data):
    for i in range(0,3):
        for a in range(0,3):
            if data[i][a] == 0 and sum(data[i]) == z:
                    return [i,a]
    for i in range(0,3):
        if data[2][i]+data[1][i]+data[0][i] == z:
            for a in range(0,3):
                if data[a][i] == 0:
                    return [a,i]
    column = []
    for i in range(0,3):
        column.append(data[i][i])
    if sum(column) == z:
        for a in range(0,3):
            if column[a] == 0:
                return [a,a]
    column = []
    a = 2
    for i in range(0,3):
        column.append(data[i][a])
        a = a-1
    a = 2
    if sum(column) == z:
        for b in range(0,3):
            if column[b] == 0:
                return [b,a]
            a = a-1

#returns all available positions in a grid        
def possible_cells(data):
    possible_cells = {}
    count = 0
    for i in range(0,3):
        for a in range(0,3):
            if data[i][a] == 0:
                possible_cells[count] = [i,a]
                count = count + 1
    return possible_cells

#example grid to debug bots
debug_grid = [[1,0,0],
              [0,1,0],
              [0,0,0]]

#bots:

#basic user input function
def user_bot(data,player):
    inputs = []
    inputs.append(int(input("Please enter row: "))-1)
    inputs.append(int(input("Please enter column: "))-1)
    return inputs

#chooses random squares even if occupied
def random_bot(data,player):
    inputs = []
    inputs.append(random.randint(0,2))
    inputs.append(random.randint(0,2))
    return inputs

#chooses random unoccupied squares
def nonerror_rand_bot(data,player):
    inputs = 0
    cells = possible_cells(data)
    input_amounts = len(cells)-1
    inputs = (cells[random.randint(0,input_amounts)])  
    return inputs

#will block winning moves and take wining chances
def danger_win_detect_bot(data,player):
    if player == 1:
        a = 8
        b = 2
    elif player == 2:
        a = 2
        b = 8
    inputs = 0
    if is_danger(b,data) != None:
        inputs = is_danger(b,data)
    elif is_danger(a,data) != None:
        inputs = is_danger(a,data)
    else:
        cells = possible_cells(data)
        input_amounts = len(cells)-1
        inputs = (cells[random.randint(0,input_amounts)])    
    return inputs
