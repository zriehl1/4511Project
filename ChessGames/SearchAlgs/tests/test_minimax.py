import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#print(os.path.dirname(os.path.dirname(__file__)))

from heuristic import *
from minimax_search import *
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
#print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Board import *
from Pieces.AllPieces import *

w = "White"
b = "Black"

class TestHeuristic(unittest.TestCase):

    board = None
    white = None
    black = None

    def setUp(self):
        pass
