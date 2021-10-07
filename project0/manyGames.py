gameList = ['overwatch', 'valorant', 'octagon', 'among us']
running = True
x = 0
while running:
    newGame = input("would you like to add a game to a favorite list, or say 'stop' to print out list of games: " )
    gameList.append(newGame)
    if (newGame == "stop"):
        while x < len(gameList):
            print (" I like the game " + gameList[x])
            x = x + 1
        running = False
