# Sodoku - Backtracking Algorithm

import time


class Solver:

    def __init__(self):
        """
            init sodoku solver
        """

        self.subscribers = set()

    def register(self, root):
        """
            register board root as subscriber
            to receive solver updates
        """

        self.subscribers.add(root)

    def dispatch(self, zero, val):
        """
            dispatch node info
        """

        for sub in self.subscribers:
            sub.update_root(zero, val)

    @staticmethod
    def print_sodoku_board(board):
        """
            print sodoku matrix
        """

        print()
        n = len(board)
        for i in range(n):
            for j in range(n):
                if len(str(board[i][j])) == 2:
                    print('{}'.format(board[i][j]), end=' ')
                else:
                    print(' {}'.format(board[i][j]), end=' ')
            print()
        print()

    @staticmethod
    def is_on_board(zero, board):
        """
            check if i,j are valid indexes for N*N board
        """

        n = len(board)
        if n > zero[0] >= 0 and 0 <= zero[1] < n:
            return True
        return False

    @staticmethod
    def get_zeros(board):
        """
            return all zero index paths on board
        """

        zeros = []
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if board[row_index][col_index] == 0:
                    zeros.append([row_index, col_index])
        return zeros

    @staticmethod
    def get_row_and_col(board, zero):
        """
            get row and column for zero
        """

        row = board[zero[0]]
        c = zero[1]
        col = []
        for r in board:
            col.append(r[c])
        return row, col

    def validate_entry(self, board, zero, val, grid_size):
        """
            validate value is a possible solution in given row, column and grid
        """

        row, col = self.get_row_and_col(board, zero)
        if val in row or val in col:
            return False

        grid_x = zero[1] // grid_size
        grid_y = zero[0] // grid_size

        for i in range(grid_y * grid_size, (grid_y * grid_size) + grid_size):
            for j in range(grid_x * grid_size, (grid_x * grid_size) + grid_size):
                if board[i][j] == val and (i, j) != zero:
                    return False

        return True

    def solve_sodoku(self, board, nodes):
        """
            solve sodoku board using Backtracking.
            sets initial values for recursive utility function
        """

        self.print_sodoku_board(board)
        zeros = self.get_zeros(board)
        grid_size = int(len(board) ** (1 / 2))

        if not self.solve_sokodu_util(board, zeros, 0, grid_size, nodes):
            print("Solution does not exist")
        else:
            self.print_sodoku_board(board)

    def solve_sokodu_util(self, board, zeros, pos, grid_size, nodes):
        """
            recursive function for solving
        """

        if not any(0 in row for row in board):
            return True

        zero = zeros[pos]

        for val in range(1, len(board) + 1):
            if self.validate_entry(board, zero, val, grid_size):
                board[zero[0]][zero[1]] = val
                pos += 1
                self.dispatch(zero, val)
                if self.solve_sokodu_util(board, zeros, pos, grid_size, nodes):
                    return True
                board[zero[0]][zero[1]] = 0
                self.dispatch(zero, ' ')
                pos -= 1

        return False
