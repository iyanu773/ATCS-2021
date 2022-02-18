import random
import time


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = []
        self.columns = 3
        self.rows = 3
        self.depth = 4

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



    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if(self.board[row][col] == '-'):
            return True
        return False



    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        if(player == 0):
            self.board[row][col] = 'X'
        if (player == 1):
            self.board[row][col] = 'O'
        if(player == '-'):
            self.board[row][col] = '-'

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot

        while (True):
            try:
                rowInput = int(input("Enter an empty row index from 0-2: "))
                colInput = int(input("Enter an empty column index from 0-2: "))
                if (self.is_valid_move(rowInput, colInput)):
                    if (player == 0):
                        self.place_player(0, rowInput, colInput)
                    elif (player == 1):
                        self.place_player(1, rowInput, colInput)
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










    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print()
        print("it is now Player 1's turn")
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
                    return True
        if (player == 1):
            for i in range(self.columns):
                winCondition = True
                for t in range(self.columns):
                    if self.board[t][i] != 'O':
                        winCondition = False
                if(winCondition == True):
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
                    return True
        if (player == 1):
            for i in range(self.columns):
                winCondition = True
                for t in range(self.columns):
                    if self.board[i][t] != 'O':
                        winCondition = False
                if (winCondition == True):
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
            if (winCondition == True):
                return True
            if(self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O'):
                return True
        return False

    def check_win(self, player):
        # TODO: Check win

        if(self.check_col_win(player) == True or self.check_row_win(player) == True or self.check_diag_win(player) == True):
            return True
        else:
            return False

    def check_tie(self):
        for i in range(self.columns):
            for t in range(self.columns):
                if(self.board[i][t] == '-'):
                    return False
        return True


    def take_random_turn(self, player):
        while(True):
            randomX = random.randrange(3)
            randomY = random.randrange(3)
            if(self.is_valid_move(randomX, randomY) == True):
                print("random X = " + str(randomX))
                print("random Y = " + str(randomY))
                self.place_player(player, randomX, randomY)
                break

    def minimax(self, player, depth):
        if self.check_win(1):
            return (10, None, None)
        if self.check_win(0):
            return (-10, None, None)
        if self.check_tie():
            return (0, None, None)
        if (depth == 0):
            return (0, None, None)

        if (player == 1):
            max = -100
            row = -1
            col = -1
            for i in range(self.columns):
                for t in range(self.rows):
                    if (self.is_valid_move(i, t)):
                        self.place_player(1, i, t)
                        score = self.minimax(0, depth - 1)[0]
                        if (max < score):
                            max = score
                            row = i
                            col = t
                        self.place_player("-", i, t)
            return (max, row, col)
        if (player == 0):
            min = 100
            row = -1
            col = -1
            for i in range(self.columns):
                for t in range(self.rows):
                    if (self.is_valid_move(i, t)):
                        self.place_player(0, i, t)
                        score = self.minimax(1, depth - 1)[0]
                        if (min > score):
                            min = score
                            row = i
                            col = t
                        self.place_player("-", i, t)
            return (min, row, col)

    def minimax_alpha_beta(self, player, depth, alpha, beta):
        if self.check_win(1):
            return (10, None, None)
        if self.check_win(0):
            return (-10, None, None)
        if self.check_tie():
            return (0, None, None)
        if (depth == 0):
            return (0, None, None)

        if (player == 1):
            maximum = -100
            row = -1
            col = -1
            for i in range(self.columns):
                for t in range(self.rows):
                    if (self.is_valid_move(i, t)):
                        self.place_player(1, i, t)
                        score = self.minimax_alpha_beta(0, depth - 1, alpha, beta)[0]
                        alpha = max(alpha, score)
                        if (maximum < score):
                            maximum = score
                            row = i
                            col = t
                        self.place_player("-", i, t)
                        if (alpha >= beta):
                            return (maximum, row, col)
            return (maximum, row, col)
        if (player == 0):
            minimum = 100
            row = -1
            col = -1
            for i in range(self.columns):
                for t in range(self.rows):
                    if (self.is_valid_move(i, t)):
                        self.place_player(0, i, t)
                        score = self.minimax_alpha_beta(1, depth - 1, alpha, beta)[0]
                        beta = min(beta, score)
                        if (minimum > score):
                            minimum = score
                            row = i
                            col = t
                        self.place_player("-", i, t)
                        if (alpha >= beta):
                            return (minimum, row, col)
            return (minimum, row, col)

    def take_minimax_turn(self, player, depth):
        start = time.time()
        score, row, col = self.minimax(player, depth)
        end = time.time()
        print("row is " + str(row))
        print("col is " + str(col))
        print("This took " + str(end - start) + " seconds to run")
        if self.is_valid_move(row, col):
            self.place_player(player, row, col)

        else:
            print("invalid")

    def take_minimaxab_turn(self, player, depth, alpha, beta):
        start = time.time()
        score, row, col = self.minimax_alpha_beta(player, depth, alpha, beta)
        end = time.time()
        print("This took " + str(end-start) + " seconds to run")
        print("row is " + str(row))
        print("col is " + str(col))
        if self.is_valid_move(row, col):
            self.place_player(player, row, col)

        else:
            print("invalid")


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
                #self.take_minimax_turn(1, self.depth)
                self.take_minimaxab_turn(1, self.depth, -1000, 1000)
                print("player 2 turn")
            self.print_board()
            if (self.check_tie()):
                print("The game has ended in a tie")
                break

        if(self.check_win(0) == True):
            self.print_board()
            print("X wins!")

        elif (self.check_win(1) == True):
            self.print_board()
            print("O wins!")





