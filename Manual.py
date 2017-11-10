
import numpy

class TicTacToe:

    def __init__(self):
        self.board = numpy.zeros((3, 3))
        print(self.board.shape)
        self.winner = 0

    def game(self):

        while not self.winner:
            if 0 in self.board[:, :]:
                move_1, move_2 = self.ask_input(1)
                self.update_board(1, move_1, move_2)
                self.winner = self.is_over()
                if 0 == self.winner:
                    move_1, move_2 = self.ask_input(-1)
                    self.update_board(2, move_1, move_2)
                    self.winner = self.is_over()
                else:
                    break

        if 0 == self.winner:
            print('Game Over, its a draw')
        else:
            print('Game Over')
            print('winner is player {}'.format(self.winner))

    def update_board(self, num_player, player_move_1, player_move_2 ):
        i = int(player_move_1)
        j = int(player_move_2)
        self.board[i][j] = num_player

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

    def ask_input(self, player_no):
        print('player' '{}'.format(player_no))
        print('please make your move, board state is shown')
        print(self.board)
        row_num = input()
        col_num = input()
        return row_num, col_num


if __name__ == "__main__":

    s = TicTacToe()
    s.game()


