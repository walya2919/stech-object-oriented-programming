import random


NUM_CARDS_PER_SHAPE = 13
NUM_SHAPES = 4
NUM_CARDS = NUM_SHAPES * NUM_CARDS_PER_SHAPE


class Card:
    def __init__(self, index):
        self.shape = index / 13
        self.value = index % 13 + 1


class Deck:
    def __init__(self, num_sets=1):
        self.cards = [Card(i) for i in range(NUM_CARDS)] * num_sets
        self.shuffle()
        self.next = 0

    def draw(self):
        card = self.cards[self.next]
        self.next = self.next + 1
        if self.next == len(self.cards):
            self.next = 0
            self.shuffle()
        return card

    def shuffle(self):
        random.shuffle(self.cards)



