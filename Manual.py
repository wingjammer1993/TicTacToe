import numpy
import random


class TicTacToe:

    def __init__(self):
        self.board = numpy.zeros((3, 3))
        self.values = {}
        print(self.board.shape)
        self.winner = 0
        self.discount = 0.3
        self.reward = 0

    # asks for input from each player, updates the player, checks for a winner, if found, exits
    def game(self):

        while not self.winner:
            if 0 in self.board[:, :]:
                move_1, move_2 = self.ask_input(1)
                self.update_board(1, move_1, move_2)
                self.winner = self.is_over()
                if 0 == self.winner:
                    move_1, move_2 = self.ask_input(2)
                    self.update_board(2, move_1, move_2)
                    self.winner = self.is_over()
                else:
                    break

        if 0 == self.winner:
            self.reward = 50
            print('Game Over, its a draw')
        else:
            if 1 == self.winner:
                self.reward = 100
            else:
                self.reward = -100
            print('Game Over')
            print('winner is player {}'.format(self.winner))

        self.update_state_value()

    # returns the current state of the board
    def give_board(self):
        return self.board

    # updates the board with given move
    def update_board(self, num_player, player_move_1, player_move_2):
        i = int(player_move_1)
        j = int(player_move_2)
        self.board[i][j] = int(num_player)

    # checks if the game is over
    def is_over(self):

        for row in self.board:
            if len(set(row)) == 1:
                if 0 is not row[0]:
                    self.winner = row[0]
                    return self.winner

        for column in self.board.T:
            if len(set(column)) == 1:
                if 0 is not column[0]:
                    self.winner = column[0]
                    return self.winner

        diag_minor = numpy.diag(numpy.fliplr(self.board))
        if len(set(diag_minor)) == 1:
            if 0 is not diag_minor[0]:
                self.winner = diag_minor[0]
                return self.winner

        diag_major = numpy.diag(self.board)
        if len(set(diag_major)) == 1:
            if 0 is not diag_major[0]:
                self.winner = diag_major[0]
                return self.winner

        return self.winner

    # asks for input from players
    def ask_input(self, player_no):
        print('player' '{}'.format(player_no))
        print('please make your move, board state is shown')
        print(self.board)
        if 2 == player_no:
            row_num = input()
            col_num = input()
        else:
            row_num, col_num = self.get_ai_move()
        return row_num, col_num

    # gives the possible action given a current state
    def give_possible_afterstates(self):
        afterstates = zip(*numpy.where(self.board == 0))
        return afterstates

    # get the ai move
    def get_ai_move(self):
        possible_afterstates = self.give_possible_afterstates()
        after_state_values = {}
        for state in possible_afterstates:
            board_config = self.give_rep_from_state(state)
            if board_config in self.values:
                after_state_values[state, board_config] = self.values[board_config]
            else:
                after_state_values[state, board_config] = random.random()

        state_max, config_max = max(after_state_values, key=lambda key: after_state_values[key])
        value_max = after_state_values[state_max, config_max]
        current_state = self.get_rep_from_board()

        if current_state in self.values:
            old_val = self.values[current_state]
        else:
            old_val = 0

        self.values[current_state] = old_val + self.discount*(value_max - old_val)
        return state_max[0], state_max[-1]

    def get_board_config(self, after_state, player_num):
        temp_board = numpy.copy(self.board)
        i = after_state[0]
        j = after_state[-1]
        temp_board[i][j] = int(player_num)
        return numpy.ndarray.flatten(temp_board)

    def update_state_value(self):
        last_state = self.get_rep_from_board()
        self.values[last_state] = self.reward

    def give_rep_from_state(self, state):
        board_config = self.get_board_config(state, 1)
        int_ternary = [int(x) for x in board_config]
        str1 = ''.join(map(str, int_ternary))
        return str1

    def get_rep_from_board(self):
        current_board = numpy.ndarray.flatten(self.board)
        int_ternary = [int(x) for x in current_board]
        str1 = ''.join(map(str, int_ternary))
        return str1

    def board_reset(self):
        self.board = numpy.zeros((3, 3))


if __name__ == "__main__":
    s = TicTacToe()
    for _ in range(10):
        s.game()



