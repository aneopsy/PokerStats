from random import shuffle
from .card import Card

class Deck:

    _DECK = []

    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        self.cards = self.get_full_deck()
        shuffle(self.cards)

    def get_cards(self):
        return list(self.cards)

    def draw(self, n=1):
        if n == 1:
            return self.cards.pop(0)

        cards = []
        for i in range(n):
            cards.append(self.draw())
        return cards

    @staticmethod
    def convert_card_to_string(deck):
        cards = []
        for i in deck:
            cards.append(i.string)
        return cards

    def remove(self, deck):
        #self.cards.pop([i for i, j in enumerate(self.cards) if j.string == rm])
        for rm in deck:
            for i, o in enumerate(self.cards):
                if o.string == rm.string:
                    del self.cards[i]
                    break

    def delete(self, deck):
        #self.cards.pop([i for i, j in enumerate(self.cards) if j.string == rm])
        for i, o in enumerate(self.cards):
            if o.string == rm.string:
                del self.cards[i]
                break

    def __str__(self):
        return Card.print_pretty_cards(self.cards)

    def get_full_deck(self):
        if Deck._DECK:
            return list(Deck._DECK)
        return list(Deck.set_full_deck())

    def set_full_deck():

        [Deck._DECK.append(Card(x + y)) for x in Card.STR_RANKS for y, a in Card.CHAR_SUIT_TO_INT_SUIT.items()]

        return Deck._DECK