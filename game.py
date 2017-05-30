
class Game():
    __live_cells = []
    __neighboring_cells = [ (-1, -1), (-1, 0), (-1, 1),
                            ( 0, -1),          ( 0, 1),
                            ( 1, -1), ( 1, 0), ( 1, 1)]

    def	__init__(self,	x,	y,	setup=[]):
        self.__live_cells = setup
        self.__x = x
        self.__y = y

    def	__str__(self):
        board = ''
        x_range = range(self.__x)
        for y in range(self.__y):
            line = ['X' if (x, y) in self.__live_cells else '-' for x in x_range]
            board += ' '.join(line) + '\n'
        return board[:-2]

    def	next_generation(self):
        counts = {}
        for cell in self.__live_cells:
            for neighbor in self.__offset(self.__neighboring_cells, cell):
                counts.setdefault(neighbor, 0)
                counts[neighbor] += 1

        self.__live_cells = {c for c in counts
                if counts[c] == 3
                    or (counts[c] == 2
                    and c in self.__live_cells)}

    def __offset(self, cells, delta):
        (dx, dy) = delta
        return {self.__getNeighbor(dx, dy, x, y) for (x, y) in cells}

    def __getNeighbor(self, delta_x, delta_y, x, y):
        return (self.__getPosition(x, delta_x, self.__x),
                self.__getPosition(y, delta_y, self.__y))

    def __getPosition(self, value, delta, length):
        position = (value + delta) % length
        if position < 0:
            return length - delta

        return position
