play_field = [[" " for _ in range(3)] for _ in range(3)]

def playgame():

    playerX = input("Where do you want to place your X (row,column)? ")
    playerXr = int(playerX[0]) - 1
    playerXc = int(playerX[2]) - 1
    print(playerXr)
    print(playerXc)

    play_field[playerXr][playerXc] = "X"
    print("\n".join(str(play_field[i]) for i in range(3)))


    playerY = input("Where do you want to place your Y (row,column)? ")
    playerYr = int(playerY[0]) - 1
    playerYc = int(playerY[2]) - 1
    print(playerYr)
    print(playerYc)

    play_field[playerYr][playerYc] = "Y"
    print("\n".join(str(play_field[i]) for i in range(3)))

    checkgame()

def checkgame():
    check_question = input("Wanna play again (Y/N): ")
    while check_question == "Y":
        playgame()

playgame()




