class PokerStars(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.value_converter = {
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: 'T',
            11: 'J',
            12: 'Q',
            13: 'K',
            14: 'A',
        }

        self.boardCardList = [None, None, None, None, None]
        self.handCardList = [None, None]
        self.round = 0
        self.maxTablePlayers = 0
        self.nbrPlayers = 0
        self.nbrPlayersTmp = 0
        self.dealerFlag = False
        self.action = None

    def reset_info(self):
        self.boardCardList = [None, None, None, None, None]
        self.handCardList = [None, None]
        self.round = 0
        self.maxTablePlayers = 0
        self.nbrPlayers = 0
        self.nbrPlayersTmp = 0

    def get_info(self):
        self.get_log()
        for line in self.file:
            if 'Game #' in line:
                self.reset_info()
            if 'OnTableData() round' in line:
                    self.round = int(line.split(' ')[2])
            if 'USR ACT box' in line:
                self.action = line.split('\'')[1]
            if 'maxTablePlayers' in line:
                self.maxTablePlayers = int(line.split('=')[1])
            if 'dealerPos' in line:
                self.dealerFlag != self.dealerFlag
                self.nbrPlayers = self.nbrPlayersTmp
                self.nbrPlayersTmp = 0
            if 'sit' in line and self.dealerFlag:
                self.nbrPlayersTmp += 1

    def get_log(self):
        with open(self.file_path, 'r') as fd_file:
            self.file = fd_file.readlines()
        fd_file.close()
        return self.file

    def get_my_card(self):
        self.get_log()
        for line in self.file:
            if 'Game #' in line:
                self.handCardList = [None, None]
            if 'UpdateMyCard' in line:
                id = int(line.split(' ')[1].split(':')[0])
                if line.split(' ')[2][0] is not '0':
                    self.handCardList[id] = self.card_converter(line.split(' ')[2])
        return self.handCardList

    def get_player_card(self):
        self.get_log()
        for line in self.file:
            if 'Game #' in line:
                self.boardCardList = [None, None, None, None, None]
            if ':::TableViewImpl::updateBoard() ' in line:
                id = int(line.split('(')[2].split(')')[0])
                self.boardCardList[id] = self.card_converter(line.split(' ')[1])
        return self.boardCardList

    def get_cards(self):
        return self.get_my_card() + self.get_player_card()

    def card_converter(self, card):
        suit = card[-1]
        rank = int(card[:-1])
        rank_converted = self.value_converter[rank]
        return str(rank_converted + suit)