import unittest
from game import Game

def extract_live_cells(game):
    representation = str(game)
    return [(x,y)
        for y,line in enumerate(representation.split('\n'))
            for x,status in enumerate(line.split(' ')) if(status == 'X')]

class TestGameRules(unittest.TestCase):

    def test_board_size_100x80(self):
        game = Game(100,80,[])
        representation = str(game)
        y = representation.split('\n')
        x = y[0].split(' ')


        self.assertEqual(100, len(x))
        self.assertEqual(80, len(y))

    def test_live_cell_with_two_neghbours_lives(self):
        blinker = {(1,1),(1,2),(1,3)}
        game = Game(10,10, blinker)

        game.next_generation()
        live_cells = extract_live_cells(game)

        self.assertTrue((1,2) in live_cells)

    def test_live_cell_with_three_neghbours_lives(self):
        symbol = {(6,5),(7,4),(7,5),(7,6)}
        game = Game(10,10, symbol)

        game.next_generation()
        live_cells = extract_live_cells(game)

        self.assertTrue((7,5) in live_cells)

    def test_dead_cell_with_exactly_three_live_neghbours_lives(self):
        symbol = {(6,5),(7,4),(7,6)}
        game = Game(10,10, symbol)

        game.next_generation()
        live_cells = extract_live_cells(game)

        self.assertTrue((7,5) in live_cells)


    def test_live_cell_with_fewer_than_two_live_neghbours_dies(self):
        blinker = {(1,1),(1,2),(1,3)}
        game = Game(10,10, blinker)

        game.next_generation()
        live_cells = extract_live_cells(game)

        self.assertFalse((1,1) in live_cells)

    def test_live_cell_with_more_than_three_neghbours_dies(self):
        symbol = {(6,5),(7,4),(7,5),(7,6),(8,5)}
        game = Game(10,10, symbol)

        game.next_generation()
        live_cells = extract_live_cells(game)

        self.assertFalse((7,5) in live_cells)


if __name__ == '__main__':
    unittest.main()
