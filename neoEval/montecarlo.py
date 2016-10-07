__author__ = 'AneoPsy'
'''
Runs a Montecarlo simulation to calculate the probability of winning with a certain pokerhand and a given amount of players
'''
import time
import numpy as np
from collections import Counter

from .deck import Deck
from .card import Card


class MonteCarlo(object):

    def eval_best_hand(self, hands):  # evaluate which hand is best
        scores = [(i, self.calc_score(Deck.convert_card_to_string(hand))) for i, hand in enumerate(hands)]
        winner = sorted(scores, key=lambda x: x[1], reverse=True)[0][0]
        return hands[winner], scores[winner][1][-1]

    def calc_score(self, hand):  # assign a calc_score to the hand so it can be compared with other hands
        card_ranks_original = '23456789TJQKA'
        original_suits = 'cdhs'
        rcounts = {card_ranks_original.find(r): ''.join(hand).count(r) for r, _ in hand}.items()
        score, card_ranks = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])

        potential_threeofakind = score[0] == 3
        potential_twopair = score == (2, 2, 1, 1, 1)
        potential_pair = score == (2, 1, 1, 1, 1, 1)

        if score[0:2] == (3, 2) or score[0:2] == (3, 3):  # fullhouse (three of a kind and pair, or two three of a kind)
            card_ranks = (card_ranks[0], card_ranks[1])
            score = (3, 2)
        elif score[0:4] == (2, 2, 2, 1):  # special case: convert three pair to two pair
            score = (2, 2, 1)  # as three pair are not worth more than two pair
            sortedCrdRanks = sorted(card_ranks, reverse=True)  # avoid for example 11,8,6,7
            card_ranks = (sortedCrdRanks[0], sortedCrdRanks[1], sortedCrdRanks[2], sortedCrdRanks[3])
        elif score[0] == 4:  # four of a kind
            score = (4,)
            sortedCrdRanks = sorted(card_ranks, reverse=True)  # avoid for example 11,8,9
            card_ranks = (sortedCrdRanks[0], sortedCrdRanks[1])
        elif len(score) >= 5:  # high card, flush, straight and straight flush
            # straight
            if 12 in card_ranks:  # adjust if 5 high straight
                card_ranks += (-1,)
            sortedCrdRanks = sorted(card_ranks, reverse=True)  # sort again as if pairs the first rank matches the pair
            for i in range(len(sortedCrdRanks) - 4):
                straight = sortedCrdRanks[i] - sortedCrdRanks[i + 4] == 4
                if straight:
                    card_ranks = (
                        sortedCrdRanks[i], sortedCrdRanks[i + 1], sortedCrdRanks[i + 2], sortedCrdRanks[i + 3],
                        sortedCrdRanks[i + 4])
                    break

            # flush
            suits = [s for _, s in hand]
            flush = max(suits.count(s) for s in suits) >= 5
            if flush:
                for flushSuit in original_suits:  # get the suit of the flush
                    if suits.count(flushSuit) >= 5:
                        break

                flushHand = [k for k in hand if flushSuit in k]
                rcountsFlush = {card_ranks_original.find(r): ''.join(flushHand).count(r) for r, _ in flushHand}.items()
                score, card_ranks = zip(*sorted((cnt, rank) for rank, cnt in rcountsFlush)[::-1])
                card_ranks = tuple(
                    sorted(card_ranks, reverse=True))  # ignore original sorting where pairs had influence

                # check for straight in flush
                if 12 in card_ranks and not -1 in card_ranks:  # adjust if 5 high straight
                    card_ranks += (-1,)
                for i in range(len(card_ranks) - 4):
                    straight = card_ranks[i] - card_ranks[i + 4] == 4
                    if straight:
                        break

            # no pair, straight, flush, or straight flush
            score = ([(1,), (3, 1, 2)], [(3, 1, 3), (5,)])[flush][straight]

        if score == (1,) and potential_threeofakind:
            score = (3, 1)
        elif score == (1,) and potential_twopair:
            score = (2, 2, 1)
        elif score == (1,) and potential_pair:
            score = (2, 1, 1)

        if score[0] == 5:
            hand_type = "StraightFlush"
            # crdRanks=crdRanks[:5] # five card rule makes no difference {:5] would be incorrect
        elif score[0] == 4:
            hand_type = "FoufOfAKind"
            # crdRanks=crdRanks[:2] # already implemented above
        elif score[0:2] == (3, 2):
            hand_type = "FullHouse"
            # crdRanks=crdRanks[:2] # already implmeneted above
        elif score[0:3] == (3, 1, 3):
            hand_type = "Flush"
            card_ranks = card_ranks[:5]
        elif score[0:3] == (3, 1, 2):
            hand_type = "Straight"
            card_ranks = card_ranks[:5]
        elif score[0:2] == (3, 1):
            hand_type = "ThreeOfAKind"
            card_ranks = card_ranks[:3]
        elif score[0:2] == (2, 2):
            hand_type = "TwoPair"
            card_ranks = card_ranks[:3]
        elif score[0] == 2:
            hand_type = "Pair"
            card_ranks = card_ranks[:4]
        elif score[0] == 1:
            hand_type = "HighCard"
            card_ranks = card_ranks[:5]
        else:
            raise Exception('Card Type error!')

        return score, card_ranks, hand_type

    def run_montecarlo(self, original_player_card_list, original_table_card_list, player_amount,
                       board_nbr_card, maxRuns, timeout):
        winner_card_type_list = list()
        wins = 0
        runs = 0
        deck = Deck()
        start_time = time.time()
        card_to_add = board_nbr_card - len(original_table_card_list)
        for m in range(maxRuns):
            runs += 1
            deck.shuffle()
            deck.remove(original_player_card_list)
            deck.remove(original_table_card_list)

            board = list(original_table_card_list)
            board += deck.draw(card_to_add)

            players = list()
            players.append(original_player_card_list)
            for n in range(0, player_amount - 1):
                players.append(deck.draw(2))

            final_cards = list()
            for hand in players:
                final_cards.append(hand + board)
            best_hand, winner_card_type = self.eval_best_hand(final_cards)
            winner = (final_cards.index(best_hand))


            CollusionPlayers = 0
            if winner < CollusionPlayers + 1:
                wins += 1
                winner_card_type_list.append(winner_card_type)

            try:
                if m % 1000 == 0:
                    if m > 999 and time.time() - start_time > timeout:
                        break
            except:
                pass

        self.equity = wins / runs
        self.winnerCardTypeList = Counter(winner_card_type_list)
        for key, value in self.winnerCardTypeList.items():
            self.winnerCardTypeList[key] = value / runs
        self.winTypesDict = self.winnerCardTypeList.items()
        self.runs = runs

        return self.equity, self.winTypesDict
