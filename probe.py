"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import random

"""
WARNING: this program contains a NASTY bug.  I put
it there on purpose as a debugging exercise, but
you DO NOT want to emulate this example!
"""


class Kangaroo:
    """A Kangaroo is a marsupial."""

    def __init__(self, name, contents=None):
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.
        item: object to be added
        # """
        if isinstance(item, Kangaroo):
            for obj in item.pouch_contents:
                self.pouch_contents.append(obj)
        else:
            self.pouch_contents.append(item)


# kanga = Kangaroo('Kanga')
# roo = Kangaroo('Roo', ['1', '2'])
# kanga.put_in_pouch('wallet')
# kanga.put_in_pouch('car keys')
# kanga.put_in_pouch(roo)
#
#
# print(kanga)
# print(roo)
# If you run this program as is, it seems to work.
# To see the problem, trying printing roo.

# Hint: to find the problem try running pylint.
#

# Пики → 3
# Червы → 2
# Бубны → 1
# Трефы → 0
# Туз → 1
# Валет → 11
# Дама → 12
# Король → 13
class Card:
    """Определяет обычную игральную карту."""
    suit_names = ['Трефы', 'Бубны', 'Червы', 'Пики']
    rank_names = [None, 'Туз', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Валет', 'Дама', 'Король']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s масти %s' % (Card.rank_names[self.rank],
                                Card.suit_names[self.suit])

    def __lt__(self, other):
        # проверка масти
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False
        # Масти одинаковые, проверить ранги
        return self.rank < other.rank


queen_of_diamonds = Card(1, 12)
# print(queen_of_diamonds)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        if len(self.cards) == 52:
            self.cards = []
            for suit in range(4):
                for rank in range(1, 14):
                    card = Card(suit, rank)
                    self.cards.append(card)
        else:
            for i in range(len(self.cards)):
                for j in range(0, len(self.cards)-i-1):
                    if self.cards[i] < self.cards[i+1]:
                        self.cards[j], self.cards[j+1] = self.cards[j+1], self.cards[j]

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, number_of_players, number_of_cards):
        list_of_players = []
        players = []
        try:
            for k in range(1, number_of_players+1):
                players.append(str(k))
            self.shuffle()
            for i in players:
                list_of_players.append(Hand(("player" + i)))
            # print(list_of_players)
            for j in list_of_players:
                self.move_cards(j, number_of_cards)
            return list_of_players
        except IndexError:
            list_of_players = []
            for i in players:
                list_of_players.append(Hand(("player" + i)))
            print("Not enough cards")
            return list_of_players


deck = Deck()
# print(len(deck.cards))
# Deck.pop_card(deck)
# print(len(deck.cards))
# Deck.sort(deck)


class Hand(Deck):
    """Определяет игральные карты в руке."""
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def __str__(self):
        res = []
        res.append(self.label)
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)



hand = Hand('new hand')
# print(hand.label)
list_of_players1 = Deck.deal_hands(deck, 3, 25)
# print(Deck.deal_hands(deck, 3, 6))
for i in list_of_players1:
    print(i)

