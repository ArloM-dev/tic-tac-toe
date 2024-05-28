import bots

#checks for 3 in a row
def is_win(z):
    column = []
    for i in range(0,3):
        if sum(grid[i]) == z:
            return True
    for a in range(0,3):
        column = []
        for i in range (0,4):
            if sum(column) == z:
                return True
            elif i < 3:
                column.append(grid[i][a])
    column = []
    for i in range (0,4):
        if sum(column) == z:
            return True
        elif i < 3:
            column.append(grid[i][i])
    column = []
    a = 2
    for i in range(0,4):
        if sum(column) == z:
            return True
        elif i < 3:
            column.append(grid[i][a])
            a = a-1

#player functions
def player_1():
    return bots.player_1(grid)
            
def player_2():
    return bots.player_2(grid)

#updates the visual grid to the current grid
def update_grid():
    viewed_grid = []
    for i in range(0,3):
        for a in range(0,3):
            if grid[i][a] == 1:
                viewed_grid.append("X")
            elif grid[i][a] == 4:
                viewed_grid.append("O")
            else: viewed_grid.append("-")
    return viewed_grid

#detects if the game is a draw
def is_draw():
    for i in range(0,3):
        for a in range(0,3):
            if grid[i][a] == 0:
                return True

#draws a text based version of the grid
def view_grid():
    new_grid = update_grid()
    for i in range(1,4):
        print (new_grid[:3])
        new_grid = new_grid[3:]
    print ("---------------")

#the base game
def game(play_go):
    view_grid()
    while True:
        if play_go == True:
            try:
                a,b = player_1()
                if grid[a][b] == 0:
                    grid[a][b] = 1
                    play_go = False
                    view_grid()
                else: print ("Cell already ocupied")
            except:
                print ("Invalid row/column")
        else:
            try:
                a,b = player_2()
                if grid[a][b] == 0:
                    grid[a][b] = 4
                    play_go = True
                    view_grid()
                else: print ("Cell already ocupied")
            except:
                print ("Invalid row/column") 
        if is_win(3) == True:
            print ("player 1 wins!")
            break
        elif is_win(12) == True:
            print ("player 2 wins!")
            break
        if is_draw() != True:
            print ("Draw!")
            break

#records the data of a game
def analize_game(play_go):
    while True:
        if play_go == True:
            try:
                a,b = player_1()
                if grid[a][b] == 0:
                    grid[a][b] = 1
                    play_go = False
            except:
                pass
        else:
            try:
                a,b = player_2()
                if grid[a][b] == 0:
                    grid[a][b] = 4
                    play_go = True
            except:
               pass 
        if is_win(3) == True:
            return "plyr1"
        elif is_win(12) == True:
            return "plyr2"
        if is_draw() != True:
            return "draw"

#menu and game selector
while True:
    grid = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    usr_input = input("Press 1 for game\nPress 2 to analize\nPress 3 to quit\n")
    if usr_input == "1":
        first = input("which player goes first, 1 or 2: ")
        if first == "1":
            player_go = True
        elif first == "2":
            player_go = False
        game(player_go)
    elif usr_input == "3":
        break
    elif usr_input == "2":
        iterations = input("how many iterations would you like: ")
        first = input("which player goes first, 1,2 or alternate (3): ")
        if first == "1":
            player_go = True
            alternate = False
        elif first == "2":
            player_go = False
            alternate = False
        elif first == "3":
            player_go = True
            alternate = True
        i = 1
        stats = [0,0,0]
        while i < int(iterations)+1:
            grid = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]
            output = analize_game(player_go)
            if alternate == True:
                player_go = not player_go
            if output == "plyr1":
                stats[0] = stats[0]+1
            elif output == "plyr2":
                stats[1] = stats[1]+1
            elif output == "draw":
                stats[2] = stats[2]+1
            else: print ("error")
            i = i + 1
            
        print ("player 1: ",stats[0])
        print ("player 2: ",stats[1])
        print ("draw: ",stats[2])

    else:
        print("Invalid input, please try again")