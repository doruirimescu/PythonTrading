import unittest
from Trading.utils.calculations import (calculate_percentage_losers,
                                        calculate_sharpe_ratio,
                                        calculate_max_consecutive_losers)


class ReturnsCalculationsTest(unittest.TestCase):
    def test_calculate_sharpe_ratio(self):
        returns = [1, 2, 3, -1, -2, -3]
        r = calculate_sharpe_ratio(returns)
        self.assertEqual(0, r)

        returns = [1, 2, 3, -1, -2, 4]
        r = calculate_sharpe_ratio(returns)
        self.assertEqual(0.55, r)

    def test_calculate_percentage_losers(self):
        returns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        p = calculate_percentage_losers(returns)
        self.assertEqual(0.0, p)

        returns = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        p = calculate_percentage_losers(returns)
        self.assertEqual(1.0, p)

        returns = [1, 2, 3, -1, -2, -3]
        p = calculate_percentage_losers(returns)
        self.assertEqual(0.5, p)

        returns = [1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        p = calculate_percentage_losers(returns)
        self.assertEqual(0.9, p)

    def test_calculate_max_consecutive_losers(self):
        returns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = calculate_max_consecutive_losers(returns)
        self.assertEqual(0, m)

        returns = [-1, -2, -3, -4, 5, 6, 7, 8, 9, 10]
        m = calculate_max_consecutive_losers(returns)
        self.assertEqual(4, m)


        returns = [-1, 2, -3, -4, 5, -6, 7, -8, -9, -10]
        m = calculate_max_consecutive_losers(returns)
        self.assertEqual(3, m)

        returns = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        m = calculate_max_consecutive_losers(returns)
        self.assertEqual(10, m)

        returns = [-1, -2, -3, -4, -5, -6, -7, -8, 9, -10]
        m = calculate_max_consecutive_losers(returns)
        self.assertEqual(8, m)
