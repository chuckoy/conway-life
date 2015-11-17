import unittest

from nose.tools import *

import life

life = Life(5, None)


class BlinkerTest(unittest.TestCase):

    def test_blinker():
        self.failIf(life.size != 3)
        self.failUnless(life.is_blinker())
        life.step()
        self.failUnless(life.is_blinker())

    def setup():
        live_cell = Cell(1)
        dead_cell = Cell(0)
        board = [(dead_cell, dead_cell, dead_cell),
                 (live_cell, live_cell, live_cell),
                 (dead_cell, dead_cell, dead_cell)]
        life.manually_create_board(board)

    def teardown():
        print("TEAR DOWN!")
