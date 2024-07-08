"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Škuta
email: tomasskuta@seznam.cz
discord: smajlikskutik
"""
import os

def print_field(field: list[list]):
    '''
    Printing play field to console
    '''
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
        print("| {} | {} | {} |".format(*row))  #* is basically unpacking the row list - ['X', 'O', 'X'] will be unpacked to X O X
        print("o---o---o---o")
    print("============================================")

def play():
    '''
    Main game function
    '''
    field = [[" ", " ", " "],[" ", " ", " "], [" ", " ", " "]]
    player_tick = "O"
    print_field(field)

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

            row = int(player[0]) - 1
            col = int(player[1]) - 1

            if field[row][col] == " ":
                field[row][col] = player_tick
            else:
                raise ValueError("There is already something!")

        except ValueError as exception:
            print(exception)
            continue

        if check_winner(field):
            print_field(field)
            print(f"Player {player_tick} won!!!!")
            end_game()

        field_sum = sum(sum(1 for i in row if i == ' ') for row in field)
        if field_sum == 0:
            print("Its a tie!")
            end_game()

        player_tick = "X" if player_tick == "O" else "O"

        print_field(field)

def end_game():
    '''
    Asking players if they want to play again, if yes calling main() again, if not exiting application
    '''
    play_again = input("Do you wanna play again (Y/N)?: ").upper()
    if play_again == "Y":
        main()
    else:
        exit()
        
def check_winner(field: list[list]) -> bool:
    '''
    Checking playing field, if there is some winner. Returning true/false
    '''
    for row in field:
        if row[0] == row[1] == row[2] != " ":
            return True
        
    for col in range(len(field)):
        if field[0][col] == field[1][col] == field[2][col] != " ":
            return True
        
    if field[0][0] == field[1][1] == field[2][2] != " " or field[0][2] == field[1][1] == field[2][0] != " ":
        return True
       
    return False

def main():
    '''
    Main app function
    '''
    play()

if __name__ == "__main__":
    main()

        





