import os
import time
from threading import Thread


class PokerStars(Thread):

    def __init__(self, file_path):
        Thread.__init__(self)
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
        self.reset = 0
        self.up = False

    def card_converter(self, card):
        suit = card[-1]
        rank = int(card[:-1])
        rank_converted = self.value_converter[rank]
        return str(rank_converted + suit)

    def stream(self):
        current = open(self.file_path, "r")
        curino = os.fstat(current.fileno()).st_ino
        while True:
            while True:
                file = current.readline()
                if not file:
                    self.up = False
                    break
                yield file

            try:
                if os.stat(self.file_path).st_ino != curino:
                    new = open(self.file_path, "r")
                    current.close()
                    current = new
                    curino = os.fstat(current.fileno()).st_ino
                    self.up = False
                    continue
            except IOError:
                pass
            time.sleep(1)

    def reset_info(self):
        self.boardCardList = [None, None, None, None, None]
        self.handCardList = [None, None]
        self.round = 0
        self.maxTablePlayers = 0
        self.nbrPlayers = 0
        self.nbrPlayersTmp = 0

    def run(self):
        for line in self.stream():
            if 'Game #' in line:
                self.reset_info()
                self.up = True
                continue

            if 'UpdateMyCard' in line:
                id = int(line.split(' ')[1].split(':')[0])
                if line.split(' ')[2][0] is not '0':
                    self.handCardList[id] = self.card_converter(line.split(' ')[2])
                    self.up = True
                continue

            if 'OnTableData() round' in line:
                self.round = int(line.split(' ')[2])
                self.up = True
                continue

            if 'USR ACT box' in line:
                self.action = line.split('\'')[1]
                self.up = True
                continue

            if 'maxTablePlayers' in line:
                self.maxTablePlayers = int(line.split('=')[1])
                self.up = True
                continue

            if 'dealerPos=' in line:
                if self.nbrPlayersTmp != 0:
                    self.nbrPlayers = self.nbrPlayersTmp
                self.nbrPlayersTmp = 0
                self.up = True
                continue

            if 'sit' in line:
                self.nbrPlayersTmp += 1
                self.up = True
                continue

            if ':::TableViewImpl::updateBoard() ' in line:
                id = int(line.split('(')[2].split(')')[0])
                self.boardCardList[id] = self.card_converter(line.split(' ')[1])
                self.up = True
                continue

if __name__ == '__main__':
    neo = PokerStars('C:\\Users\\theis_p\\AppData\\Local\\PokerStars.FR\\PokerStars.log.0')
    neo.start()
    while True:
        if neo.up:
            print(neo.handCardList)
            print(neo.boardCardList)
