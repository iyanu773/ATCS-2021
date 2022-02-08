import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = []
        self.columns = 3
        self.rows = 3

        for i in range(self.columns):
            row = []
            for t in range(self.rows):
                dash = "-"
                row.append(dash.strip())
            self.board.append(row)



    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!")
        print("Player 1 is X and Player 2 is O")
        print("Take turns placing your pieces - the first to 3 in a row wins!")



    def print_board(self):
        # TODO: Print the board
        print("   0 1 2")
        for t in range(self.columns):
            print(str(t), end='  ')
            print(*self.board[t])



    def is_valid_move(self, player):
        # TODO: Check if the move is valid
        while (True):
            try:
                rowInput = int(input("Enter an empty row index from 0-2: "))
                colInput = int(input("Enter an empty column index from 0-2: "))
                if (self.board[rowInput][colInput] == '-'):
                    if (player == 0):
                        self.place_player(0,rowInput,colInput)
                    elif (player == 1):
                        self.place_player(1,rowInput,colInput)
                else:
                    # manually throwing an error if space isnt empty, i know its lazy, im sorry
                    self.board[100][100] == '-'
            except IndexError:
                print("this is not a valid response")
                continue
            except ValueError:
                print("this is not a valid response")
                continue
            return

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        if(player == 0):
            self.board[row][col] = 'X'

        if (player == 1):
            self.board[row][col] = 'O'

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot

        self.is_valid_move(player)







    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print()
        print("it is now Player " + str(player) + "'s turn")
        self.take_manual_turn(player)

    def check_col_win(self, player):
        # TODO: Check col win
        if(player == 0):
            for i in range(self.columns):
                winCondition = True
                for t in range(self.columns):
                    if self.board[t][i] != 'X':
                        winCondition = False
                if (winCondition == True):
                    print("col win")
                    return True
        if (player == 1):
            for i in range(self.columns):
                winCondition = True
                for t in range(self.columns):
                    if self.board[t][i] != 'O':
                        winCondition = False
                if(winCondition == True):
                    print("col win")
                    return True

        return False



    def check_row_win(self, player):
        # TODO: Check row win
        if (player == 0):
            for i in range(self.columns):
                winCondition = True
                for t in range(self.columns):
                    if self.board[i][t] != 'X':
                        winCondition = False
                if (winCondition == True):
                    print("row win")
                    return True
        if (player == 1):
            for i in range(self.columns):
                winCondition = True
                for t in range(self.columns):
                    if self.board[i][t] != 'O':
                        winCondition = False
                if (winCondition == True):
                    print("row win")
                    return True

        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if (player == 0):
            winCondition = True
            for i in range(self.columns):
                if (self.board[i][i] != 'X'):
                    winCondition = False
            if (winCondition == True):
                return True
            elif(self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X'):
                return True

        elif (player == 1):
            winCondition = True
            for i in range(self.columns):
                if (self.board[i][i] != 'O'):
                    winCondition = False
            if(winCondition == True):
                return True
            elif (self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X'):
                return True


        return False

    def check_win(self, player):
        # TODO: Check win

        if(self.check_col_win(player) == True or self.check_row_win(player) == True or self.check_diag_win(player) == True):
            return True
        else:
            return False

    def check_tie(self):
        allEmpty = True
        for i in range(self.columns):
            for i in range(self.columns):
                if(self.board[i][t] == '-'):
                    allEmpty = False
        if (allEmpty == True):
            return True

        return False

    def play_game(self):
        # TODO: Play game
        playerTurn = 0
        self.print_instructions()
        self.print_board()

        while(self.check_win(0) != True and self.check_win(1) != True):
            playerTurn += 1
            if(playerTurn % 2 == 1):
                self.take_turn(0)
                print("player 1 turn")
            elif(playerTurn % 2 == 0):
                self.take_turn(1)
                print("player 2 turn")
            self.print_board()

        if(self.check_win(0) == True):
            self.print_board()
            print("X wins!")


        elif (self.check_win(1) == True):
            self.print_board()
            print("O wins!")


