class Cell:

    def __init__(self, initial_state):
        self.state = initial_state

    def live(self, states):
        alive = states.count(1)
        # Any live cell...
        if self.state == 1:
            # ...with fewer than two live neighbours dies,
            # as if caused by under-population.
            if alive < 2:
                return 0
            # ...with two or three live neighbours lives on
            # to the next generation.
            elif alive < 4:
                return 1
            # ...with more than three live neighbours dies,
            # as if by over-population.
            else:
                return 0
        # Any dead cell with exactly three live neighbours
        # becomes a live cell, as if by reproduction.
        elif alive == 3:
            return 1
        return self.state

    def get_state(self):
        return self.state
