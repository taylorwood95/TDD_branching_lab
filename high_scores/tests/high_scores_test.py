import unittest

# from src.high_scores import latest, personal_best, personal_top_three
from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    # Tests
    def setUp(self):

        self.high_scores = [1, 2, 3, 4, 5]

    # Test latest score (the last thing in the list)
    def test_latest_score(self):

        self.assertEqual(5, latest(self.high_scores))

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(5, personal_best(self.high_scores))

    # Test top three from list of scores
    def test_personal_top_three(self):
        self.assertEqual([5, 4, 3], personal_top_three(self.high_scores))

    # Test ordered from highest tp lowest
    def test_high_to_low(self):
        self.assertEqual([5, 4, 3, 2, 1], high_to_low(self.high_scores))

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
