from neoEval import Card, Evaluator, Deck
from neoPS import PokerStars

__version__ = '0.1'
__author__ = 'AneoPsy'


class NeoOdds (object):

    def __init__(self):
        self.evaluator = Evaluator()
        self.deck = Deck()
        self.file = None
        self.cards = []
        self.my_class = None
        self.my_score = None
        self.my_percentage = 0

    def config(self, file_path):
        if file_path is not None:
            self.file_path = file_path
            self.pokerstars = PokerStars(self.file_path)
            self.file = self.pokerstars.get_log()

    def evaluate(self):
        self.my_score = self.evaluator.evaluate(self.cards[1], self.cards[0])
        self.my_class = self.evaluator.class_to_string(self.evaluator.get_rank_class(self.my_score))
        self.my_percentage = 100 * (1.0 - self.evaluator.get_five_card_rank_percentage(self.my_score))
        return self.my_score, self.my_class, self.my_percentage

    def setup(self, n_gen, nbr_player, cards, n_board):
        boards = []
        hands = []

        for i in range(n_gen):
            self.deck.remove(cards[0])
            self.deck.remove(cards[1])
            if len(cards[1]) == (n_board - 1):
                a = list(cards[1])
                a.append(self.deck.draw())
                boards.append(a)
            else:
                boards.append(cards[1] + self.deck.draw(n_board - len(cards[1])))
            hands.append([])
            hands[i].append(cards[0])
            for x in range(nbr_player):
                hands[i].append(self.deck.draw(2))
            self.deck.shuffle()

        return boards, hands

    def check(self):
        for rm in neo.pokerstars.get_my_card():
            for i, o in enumerate(self.deck.cards):
                if o.string == rm.string:
                    print(o.string)
                    break

    def equity(self, n_gen, n_board):

        boards, c = self.setup(n_gen, self.pokerstars.nbrPlayers - 1, self.cards, n_board)
        percentage = 0
        if not self.cards:
            return "No Hand Found!"
        for i in range(len(boards)):
            percentage += (1.0 - self.evaluator.get_five_card_rank_percentage(self.evaluator.evaluate(boards[i],
                                                                                                      self.cards[0])))

        return (percentage / n_gen) * 100

    @staticmethod
    def card_converter(cards):
        r_cards = []
        cards = [x for x in cards if x is not None]
        for i in cards:
            r_cards.append(Card(i))
        return r_cards

    def get_poker_cards(self):
        self.cards = []
        self.cards.append(self.card_converter(self.pokerstars.get_my_card()))
        self.cards.append(self.card_converter(self.pokerstars.get_player_card()))
        return self.cards

    def calculate(self):
        self.p_score = self.eval.evaluate(self.cards[1], self.cards[0])
        self.p_class = self.eval.get_rank_class(self.p_score)

    def odds(self, nbr_gen, nbr_player):
        self.get_poker_cards()
        boards, hands = self.setup(nbr_gen, nbr_player - 1, self.cards, 5)
        flop = 0
        turn = 0
        river = 0

        for i in range(len(boards)):
            a, b, c = self.evaluator.hand_equity(boards[i], hands[i])
            for i in a:
                if i == 0:
                    flop += 1
            for i in b:
                if i == 0:
                    turn += 1
            for i in c:
                if i == 0:
                    river += 1

        return flop / nbr_gen * 100, turn / nbr_gen * 100, river / nbr_gen * 100
