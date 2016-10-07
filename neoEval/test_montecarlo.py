'''
Unittest for Montecarlosimulation. Checks if the differnt type of hands and their corresponding probability to win (equity)
is calculated correctly and within a given amount of time without a timeout
'''

import time
import unittest

import numpy as np

from .montecarlo import MonteCarlo
from .card import Card


class TestMonteCarlo(unittest.TestCase):
    def test_evaluator(self):
        Simulation = MonteCarlo()

        Simulation.player_final_cards = [[Card('8h'), Card('8d'), Card('Qh'), Card('7h'), Card('9h'), Card('Jh'), Card('Th')],
                                         [Card('Kh'), Card('6c'), Card('Qh'), Card('7h'), Card('9h'), Card('Jh'), Card('Th')]]  # two straight flush
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            1)

    def test_monteCarlo(self):
        def testRun(Simulation, my_cards, cards_on_table, players, expected_results):
            maxRuns = 15000
            testRuns = 5
            secs = 1

            total_result = []
            for n in range(testRuns):
                start_time = time.time()
                Simulation.run_montecarlo(my_cards, cards_on_table, players, 5, maxRuns=maxRuns, timeout=secs)
                equity = Simulation.equity
                total_result.append(equity * 100)
                print("--- %s seconds ---" % (time.time() - start_time))

                for keys, values in Simulation.winTypesDict:
                    print(keys + ": " + (str(np.round(values * 100, 2))))
                print("Equity: " + str(np.round(equity * 100, 2)))
                self.assertAlmostEqual(sum(Simulation.winnerCardTypeList.values()) - equity, 0, delta=0.0001)

            stdev = np.std(total_result)
            avg = np.mean(total_result)

            print("Mean: " + str(avg))
            print("Stdev: " + str(stdev))


            self.assertAlmostEqual(avg, expected_results, delta=1)
            self.assertAlmostEqual(stdev, 0, delta=1)

        Simulation = MonteCarlo()

        my_cards = [Card('8h'), Card('8d')]
        cards_on_table = [Card('Qh'), Card('7h'), Card('9h'), Card('Jh'), Card('Th')]
        expected_results = 95.6
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)


        my_cards = [Card('8h'), Card('8d')]
        cards_on_table = []
        expected_results = 69.1
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

if __name__ == '__main__':
    unittest.main()
