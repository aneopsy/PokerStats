'''
Unittest for Montecarlosimulation. Checks if the differnt type of hands and their corresponding probability to win (equity)
is calculated correctly and within a given amount of time without a timeout
'''

import time
import unittest

import numpy as np

import montecarlo as mc


class TestMonteCarlo(unittest.TestCase):
    def test_evaluator(self):  # unittest to make sure the evaluator returns the corret winner hand 1 or 2 (returned as index of 0 or 1)
        Simulation = mc.MonteCarlo()

        Simulation.player_final_cards = [['8h', '8d', 'Qh', '7h', '9h', 'Jh', 'Th'],
                                         ['Kh', '6c', 'Qh', '7h', '9h', 'Jh', 'Th']]  # two straight flush
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            1)

        Simulation.player_final_cards = [['As', 'Ks', 'Ts', '9s', '7s', '2h', '2h'],
                                         ['As', 'Ks', 'Ts', '9s', '8s', '2h', '2h']]  # two flush
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            1)

        Simulation.player_final_cards = [['8s', 'Ts', '8h', 'Ks', '9s', 'Th', 'Kh'],
                                         ['Td', '7s', '8h', 'Ks', '9s', 'Th', 'Kh']]  # two pairs
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            0)

        Simulation.player_final_cards = [['2d', '2h', 'As', 'Ad', 'Ah', '8s', '7h'],
                                         ['7c', '7s', '7h', 'Ad', 'As', '8s', '8h']]  # FULLHOUSES
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            0)

        Simulation.player_final_cards = [['7c', '7s', '7h', 'Ad', 'Ks', '5s', '8h'],
                                         ['2d', '3h', 'As', '4d', '5h', '8s', '7h']]  # THREE OF A KIND AND STRAIGHT
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            1)

        Simulation.player_final_cards = [['7c', '7c', 'Ac', 'Ac', '8c', '8s', '7h'],
                                         ['2c', '3c', '4c', '5c', '6c', '8s', 'Kh']]  # FULL OF ACE AND STRAIGHT FLUSH
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            1)

        Simulation.player_final_cards = [['Ac', 'Js', 'As', '2d', '5h', '3s', '3h'],
                                         ['Qd', 'Jd', 'Ts', '9d', '6h', '8s', 'Kh'],
                                         ['2d', '3d', '4s', '5d', '6h', '8s', 'Kh']]  # STRAIGHTS and twoPair
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            1)

        Simulation.player_final_cards = [['7c', '5s', '3s', 'Jd', '8h', '2s', 'Kh'],
                                         ['Ad', '3d', '4s', '5d', '9h', '8s', 'Kh']]  # Highcardds
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            1)

        Simulation.player_final_cards = [['2c', '2d', '4s', '4d', '4h', '8s', 'Kh'],
                                         ['7c', '7s', '7d', '7h', '8h', '8s', 'Jh']]  # Fullhouse and four of a kind
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            1)

        Simulation.player_final_cards = [['7c', '5s', '3s', 'Jd', '8h', '2s', 'Kh'],
                                         ['Ad', '3d', '3s', '5d', '9h', '8s', 'Kh']]  # Highcard and Pair
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            1)

        Simulation.player_final_cards = [['7h', '7s', '3s', 'Jd', '8h', '2s', 'Kh'],
                                         ['7d', '3d', '3s', '7c', '9h', '8s', 'Kh']]  # Two pairs over one pair
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            1)

        Simulation.player_final_cards = [['As', '8h', 'Ts', 'Jh', '3h', '2h', 'Ah'],
                                         ['Qd', 'Qh', 'Ts', 'Jh', '3h', '2h', 'Ah']]  # Two flushes
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            1)

        Simulation.player_final_cards = [['9s', '7h', 'Ks', 'Kh', 'Ah', 'As', 'Ac'],
                                         ['8d', '2h', 'Ks', 'Kh', 'Ah', 'As', 'Ac']]  # Full house on table that is draw
        print(Simulation.eval_best_hand(Simulation.player_final_cards)[1])
        print("\r")
        self.assertEqual(
            Simulation.player_final_cards.index(Simulation.eval_best_hand(Simulation.player_final_cards)[0]),
            0)

    def test_monteCarlo(self):  # Unittest to ensure correct winning probabilities are returned
        def testRun(Simulation, my_cards, cards_on_table, players, expected_results):
            maxRuns = 15000  # maximum number of montecarlo runs
            testRuns = 5  # make several testruns to get standard deviation of winning probability
            secs = 5  # cut simulation short if amount of seconds are exceeded

            total_result = []
            for n in range(testRuns):
                start_time = time.time()
                Simulation.run_montecarlo(my_cards, cards_on_table, players, 5, 1, maxRuns=maxRuns, timeout=secs)
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

        Simulation = mc.MonteCarlo()

        my_cards = [['As', 'Ah']]
        cards_on_table = []
        expected_results = 63.8
        players = 10
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['8h', '8d']]
        cards_on_table = ['Qh', '7h', '9h', 'Jh', 'Th']
        expected_results = 95.6
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['As', 'Ks']]
        cards_on_table = []
        expected_results = 48.4
        players = 3
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['As', 'Ks']]
        cards_on_table = []
        expected_results = 64.88
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['8s', 'Ts']]
        cards_on_table = ['8h', 'Ks', '9s', 'Th', 'Kh']
        expected_results = 71.5 + 5.9
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['8s', 'Ts']]
        cards_on_table = ['2s', '3s', '4s', 'Ks', 'As']
        expected_results = 87
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['8s', '2s']]
        cards_on_table = ['5s', '3s', '4s', 'Ks', 'As']
        expected_results = 100
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['8s', 'Ts']]
        cards_on_table = []
        expected_results = 22.6 + 2.9
        players = 5
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['2c', 'Qs']]
        cards_on_table = []
        expected_results = 49.6  # 45 win and 4 tie
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['7h', '7s']]
        cards_on_table = ['7c', '8c', '8s', 'Ac', 'Ah']
        expected_results = 86.7
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['3s', 'Qh']]
        cards_on_table = ['2c', '5h', '7c']
        expected_results = 30.9 + 2.2
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['5c', 'Js']]
        cards_on_table = []
        expected_results = 23
        players = 4
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['Tc', 'Th']]
        cards_on_table = ['4d', 'Qd', 'Kc']
        expected_results = 66.7 + 0.38
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['Jh', 'Qs']]
        cards_on_table = ['5c', 'Jd', 'As', 'Ks', 'Qd']
        expected_results = 77
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['2h', '8s']]
        cards_on_table = ['Ac', 'Ad', 'As', 'Ks', 'Kd']
        expected_results = 95
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['Kd', 'Ks']]
        cards_on_table = ['4d', '6s', '9c', '9s', 'Tc']
        expected_results = 88
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['5h', 'Kd']]
        cards_on_table = ['Kh', 'Js', '2c', 'Qs']
        expected_results = 75.6 + 3.6
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['Jd', 'Js']]
        cards_on_table = ['8c', 'Tc', 'Jc', '5h', 'Qc']
        expected_results = 26
        players = 3
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

        my_cards = [['Td', '7d']]
        cards_on_table = ['8d', 'Qd', '7c', '5d', '6d']
        expected_results = 87
        players = 2
        testRun(Simulation, my_cards, cards_on_table, players, expected_results)

if __name__ == '__main__':
    unittest.main()
