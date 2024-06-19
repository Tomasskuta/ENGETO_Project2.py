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
            playerIn = input(f"Player {player_tick} | Please enter your move numbers 'row column': ")

            player = playerIn.split()

            if len(player) != 2:
                raise ValueError("Input must be in format: row column")
            
            if not (player[0].isdigit() and player[1].isdigit()):
                raise ValueError("Both row and column must be digits")

            if not ((1 <= int(player[0]) <= 3 and 1 <= int(player[1]) <= 3)):
                raise ValueError("Input is not between 1-3")

            playerR = int(player[0]) - 1
            playerC = int(player[1]) - 1

            if field[playerR][playerC] == " ":
                field[playerR][playerC] = player_tick
            else:
                raise ValueError("There is already something!")

        except ValueError as exception:
            print(exception)
            continue

        winner_quest = input("Do we have winner?: ")
        if winner_quest == "Y":
            winner = True
        else:
            winner = False

        if check_winner(winner):
            print(f"Player {player_tick} won!!!!")
            if end_game():
                main()
            else:
                exit()

        if player_tick != "X":
            player_tick = "X"
        else:
            player_tick = "O"

        print_field(field)

def end_game():
    play_again = input("Do you wanna play again (Y/N)?: ")
    if play_again == "Y":
        return True
    else:
        return False
        
def check_winner(winner):
    if winner == True:
        return True
    else:
        return False

def main():
    field = [[" " for _ in range(3)] for _ in range(3)]
    player_tick = "O"
    print_field(field)
    play(field,player_tick)

if __name__ == "__main__":
    main()

        





