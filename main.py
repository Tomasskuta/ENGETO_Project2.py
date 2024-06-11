play_field = [[" " for _ in range(3)] for _ in range(3)]

while True:

    playerX = input("Where do you want to place your X (row column)? ")
    playerXr = int(playerX[0]) - 1
    playerXc = int(playerX[2]) - 1
    print(playerXr)
    print(playerXc)

    play_field[playerXr][playerXc] = "X"
    print("\n".join(str(play_field[i]) for i in range(3)))
    while True:

        try:
            playerY = input("Where do you want to place your Y (row column)? ")


            if not ((1 <= int(playerY[0]) <= 3 or 1 <= int(playerY[1]) <= 3)):
                break
            playerYr = int(playerY[0]) - 1
            playerYc = int(playerY[2]) - 1
            break

        except ValueError:
            print("Wrong input, try again")
            continue
        except InputOutsideRange:
            print("Numbers outside of the range 1-3")
             

        playerYr = int(playerY[0]) - 1
        playerYc = int(playerY[2]) - 1
        print(playerYr)
        print(playerYc)

    play_field[playerYr][playerYc] = "Y"
    print("\n".join(str(play_field[i]) for i in range(3)))





