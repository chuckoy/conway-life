import argparse
import random
import sys

from cell import Cell


def main(argv):
    size = 5
    seed = None
    parser = argparse.ArgumentParser(
        description='Implementation of Conway\'s game of life')
    parser.add_argument('-size', metavar='size', nargs=1,
                        help='The size of the board (default=5)')
    parser.add_argument('-seed', metavar='seed', nargs=1,
                        help='Seed to initialise board ' +
                             '(default=datetime.now())')

    args = parser.parse_args()
    if args.size:
        size = args.size[0]
    if args.seed:
        seed = args.seed[0]
    life = Life(size, seed)
    live_cell = Cell(1)
    dead_cell = Cell(0)
    board = [(dead_cell, dead_cell, dead_cell),
             (live_cell, live_cell, live_cell),
             (dead_cell, dead_cell, dead_cell)]
    print("Board = 3")
    life.manually_create_board(board)
    life.print_board()
    if life.size != 3:
        print("Fail")
    if life.is_blinker():
        print("Pass")
    life.step()
    if life.is_blinker():
        print("Pass")
    life.step()


class Life:

    def __init__(self, size, seed):
        self.size = size
        self.board_new = []
        self.board_old = []
        random.seed(seed)
        for y in range(0, size):
            row = []
            for x in range(0, size):
                row.append(Cell(random.randint(0, 1)))
            self.board_old.append(row)

        print("Initial state:")
        self.print_board()
        for i in range(0, 5):
            print("Stepping")
            self.step()

    def step(self):
        self.board_new = []
        for y, row in enumerate(self.board_old):
            new_row = []
            for x, cell in enumerate(row):
                # Get states of cells from old board
                states = self.get_neighbour_states(x, y)
                # Store new state of cell in new row
                new_row.append(Cell(cell.live(states)))
            # Store new row to new board
            self.board_new.append(new_row)
        # Copy new board to old board
        self.board_old = self.board_new
        self.print_board()

    def print_board(self):
        for row in self.board_old:
            for cell in row:
                if cell.get_state() == 0:
                    print('-', end="")
                else:
                    print('O', end="")
            print("")

    def get_neighbour_states(self, x, y):
        # Get states of cell from old board
        states = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                # If we are at the queried cell, do not get its state
                if i == 0 and j == 0:
                    pass
                else:
                    # Get the state of the neighbour
                    try:
                        # Special case for python since index=-1 is treated
                        # as end of list
                        if y + i < 0 or x + j < 0:
                            raise IndexError
                        (states
                         .append((self.board_old[y + i][x + j]
                                  .get_state())))
                    # If we are at the edge of the board, consider it dead
                    except IndexError:
                        states.append(0)
        return states

    def get_states(self):
        states = []
        for row in self.board_old:
            entry = []
            for cell in row:
                entry.append(cell.get_state())
            states.append(entry)
        return states

    def manually_create_board(self, board):
        self.size = len(board)
        self.board_old = board

    def is_blinker(self):
        states = self.get_states()
        if (states == [[0, 0, 0], [1, 1, 1], [0, 0, 0]] or
                states == [[0, 1, 0], [0, 1, 0], [0, 1, 0]]):
            return True
        else:
            return False

if __name__ == "__main__":
    main(sys.argv[1:])
