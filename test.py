from neoEval import Card, Evaluator, Deck


deck = Deck()
evaluator = Evaluator()


def setup(n_gen, nbr_player, hand, board):
    boards = []
    hands = []

    for i in range(n_gen):
        deck.remove(hand)
        deck.remove(board)
        boards.append(board + deck.draw(5 - len(board)))
        hands.append([])
        hands[i].append(hand)
        for x in range(nbr_player):
            hands[i].append(deck.draw(2))
        deck.shuffle()

    return boards, hands

def odds(nbr_gen, nbr_player, player, board):

    boards, hands = setup(nbr_gen, nbr_player - 1, player, board)
    flop = 0
    turn = 0
    river = 0

    for i in range(len(boards)):
        a, b, c = evaluator.hand_equity(boards[i], hands[i])
        for i in a:
            if i == 0:
                flop +=1
        for i in b:
            if i == 0:
                turn +=1
        for i in c:
            if i == 0:
                river +=1
    return flop/nbr_gen*100, turn/nbr_gen*100, river/nbr_gen*100

if __name__ == '__main__':
    my_cards = [Card('As'), Card('Ah')]
    my_board = []
    print(odds(1000, 6, my_cards, my_board))