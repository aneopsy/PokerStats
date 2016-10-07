class Card(object):

    STR_RANKS = '23456789TJQKA'
    INT_RANKS = range(13)
    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

    CHAR_RANK_TO_INT_RANK = dict(zip(list(STR_RANKS), INT_RANKS))
    CHAR_SUIT_TO_INT_SUIT = {
        's' : 1, # spades
        'h' : 2, # hearts
        'd' : 4, # diamonds
        'c' : 8, # clubs
    }
    INT_SUIT_TO_CHAR_SUIT = 'xshxdxxxc'

    PRETTY_SUITS = {
        1 : u"\u2660".encode('utf-8'),
        2 : u"\u2764".encode('utf-8'),
        4 : u"\u2666".encode('utf-8'),
        8 : u"\u2663".encode('utf-8')
    }

    PRETTY_REDS = [2, 4]
    STRING = None

    def __init__(self, string):
        self.string = string
        self.rank = string[0]
        self.suit = string[1]
        self.bin = self.get_bin()

    def get_bin(self):
        rank_char = self.string[0]
        suit_char = self.string[1]
        rank_int = Card.CHAR_RANK_TO_INT_RANK[rank_char]
        suit_int = Card.CHAR_SUIT_TO_INT_SUIT[suit_char]
        rank_prime = Card.PRIMES[rank_int]

        bitrank = 1 << rank_int << 16
        suit = suit_int << 12
        rank = rank_int << 8

        return bitrank | suit | rank | rank_prime

    @staticmethod
    def int_to_str(card_int):
        rank_int = Card.get_rank_int(card_int)
        suit_int = Card.get_suit_int(card_int)
        return Card.STR_RANKS[rank_int] + Card.INT_SUIT_TO_CHAR_SUIT[suit_int]

    @staticmethod
    def get_rank_int(card_int):
        return (card_int.bin >> 8) & 0xF

    @staticmethod
    def get_suit_int(card_int):
        return (card_int.bin >> 12) & 0xF

    @staticmethod
    def get_bitrank_int(card_int):
        return (card_int.bin >> 16) & 0x1FFF

    @staticmethod
    def get_prime(card_int):
        return card_int & 0x3F

    @staticmethod
    def hand_to_binary(card_strs):
        bhand = []
        for c in card_strs:
            bhand.append(Card.new(c))
        return bhand

    @staticmethod
    def prime_product_from_hand(card_ints):
        product = 1
        for c in card_ints:
            product *= (c.bin & 0xFF)

        return product

    @staticmethod
    def prime_product_from_rankbits(rankbits):
        product = 1
        for i in Card.INT_RANKS:
            if rankbits & (1 << i):
                product *= Card.PRIMES[i]

        return product

    @staticmethod
    def int_to_binary(card_int):
        bstr = bin(card_int)[2:][::-1]
        output = list("".join(["0000" +"\t"] * 7) +"0000")

        for i in range(len(bstr)):
            output[i + int(i/4)] = bstr[i]

        # output the string to console
        output.reverse()
        return "".join(output)

    @staticmethod
    def int_to_pretty_str(card_int):
        """
        Prints a single card 
        """
        
        color = False
        try:
            from termcolor import colored
            color = True
        except ImportError: 
            pass

        # suit and rank
        suit_int = Card.get_suit_int(card_int)
        rank_int = Card.get_rank_int(card_int)

        # if we need to color red
        s = Card.PRETTY_SUITS[suit_int]
        if color and suit_int in Card.PRETTY_REDS:
            s = colored(s, "red")

        r = Card.STR_RANKS[rank_int]

        return " [ " + str(r) + " " + s.decode("utf-8") + " ] "

    @staticmethod
    def print_pretty_card(card_int):
        """
        Expects a single integer as input
        """
        print(Card.int_to_pretty_str(card_int))

    @staticmethod
    def print_pretty_cards(card_ints):
        """
        Expects a list of cards in integer form.
        """
        output = " "
        card_ints = [x for x in card_ints if x is not None]
        for i in range(len(card_ints)):
            c = card_ints[i]
            if i != len(card_ints) - 1:
                output += Card.int_to_pretty_str(c) + ","
            else:
                output += Card.int_to_pretty_str(c) + " "

        return output
