import os

def print_field(field):

    os.system("cls")
    print("Welcome to Tic Tac Toe")
    print("============================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("============================================")
    print("Let's start the game")
    print("--------------------------------------------")
    print("o---o---o---o")
    for row in field:
        print("| {} | {} | {} |".format(*row))
        print("o---o---o---o")
    print("============================================")

def play(field,player_tick):

    while True:

        try:
            playerYin = input(f"Player {player_tick} | Please enter your move numbers 'row column': ")

            player = playerYin.split()

            if len(player) != 2:
                raise ValueError("Input must be in format: row column")
            
            if not (player[0].isdigit() and player[1].isdigit()):
                raise ValueError("Both row and column must be digits")

            if not ((1 <= int(player[0]) <= 3 and 1 <= int(player[1]) <= 3)):
                raise ValueError("Input is not between 1-3")

        except ValueError as exception:
            print(exception)
            continue

        playerYr = int(player[0]) - 1
        playerYc = int(player[1]) - 1

        field[playerYr][playerYc] = player_tick
        if player_tick != "X":
            player_tick = "X"
        else:
            player_tick = "O"
   
        print_field(field)

def main():
    field = [[" " for _ in range(3)] for _ in range(3)]
    player_tick = "O"
    print_field(field)
    play(field,player_tick)

if __name__ == "__main__":
    main()

        





