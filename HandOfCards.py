from enum import Enum
from random import shuffle

class HandOfCards:
    def __init__(self):
        self.deck = Deck()
        self.deal(5)

    def deal(self, size):
        self.hand = [self.deck.draw() for i in range(size)]
        self.print()

    def print(self):
        for card in self.hand:
            print(card)

class Suite(Enum):
    Hearts, Clubs, Diamonds, Spades = range(4)

class Values(Enum):
    VA, V2, V3, V4, V5, V6, V7, V8, V9, V10, VJ, VQ, VK = range(13)

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in Suite for v in Values]
        shuffle(self.cards)

    def shuffle(self):
        self.cards.shuffle()

    def draw(self):
        return self.cards.pop()

class Card:
    def __init__(self, suite, val):
        self.suite = suite
        self.val = val

    def __str__(self):
        return f"{self.val} of {self.suite}"

h = HandOfCards()

