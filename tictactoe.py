cells = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def draw_board():

    print("---------")
    print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
    print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
    print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
    print("---------")


count = 0


def coordinates():

    global count
    print("Enter the coordinates: ")
    x, y = input().split()
    valid = ["1", "2", "3"]
    if x.isnumeric() is False or y.isnumeric() is False:
        print("You should enter numbers!")
        coordinates()
    elif x not in valid or y not in valid:
        print("Coordinates should be 1 to 3!")
        coordinates()
    else:
        if x == "1":
            location = int(y) - int(x)
            if cells[location] == "X" or cells[location] == "O":
                print("This cell is occupied! Choose another one!")
                coordinates()
            elif count % 2 == 0:
                cells[location] = "X"
            else:
                cells[location] = "O"
        elif x == "2":
            location = int(y) + int(x)
            if cells[location] == "X" or cells[location] == "O":
                print("This cell is occupied! Choose another one!")
                coordinates()
            elif count % 2 == 0:
                cells[location] = "X"
            else:
                cells[location] = "O"
        elif x == "3":
            location = int(y) + 5
            if cells[location] == "X" or cells[location] == "O":
                print("This cell is occupied! Choose another one!")
                coordinates()
            elif count % 2 == 0:
                cells[location] = "X"
            else:
                cells[location] = "O"

        count = count + 1

    draw_board()


def win_check():

    global cells
    global winner
    if cells[0] is not ' ' and cells[0] == cells[1] == cells[2] or\
        cells[0] == cells[3] == cells[6] or\
            cells[0] == cells[4] == cells[8]:
        print(cells[0], "wins")
        winner = True
    elif cells[2] != ' ' and cells[2] == cells[5] == cells[8] or\
            cells[2] == cells[4] == cells[6]:
        print(cells[2], "wins")
        winner = True
    elif cells[1] != ' ' and cells[1] == cells[4] == cells[7]:
        print(cells[1], "wins")
        winner = True
    elif cells[3] != ' ' and cells[3] == cells[4] == cells[5]:
        print(cells[3], "wins")
        winner = True
    elif cells[6] != ' ' and cells[6] == cells[7] == cells[8]:
        print(cells[6], "wins")
        winner = True
    elif " " not in cells:
        print("Draw")
        winner = True


winner = False


while winner is False:

    coordinates()
    if count >= 5:
        win_check()
