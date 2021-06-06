from abc import ABC, abstractmethod


class Hand(ABC):

    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self._cards = cards

    def add_card(self, card):
        self._cards.append(card)

    def remove_card(self, rank, suite):
        for card in self._cards:
            if card.rank == rank and card.suite == suite:
                return  self._cards.remove(card)

    def score(self):
        score = 0
        for card in self._cards:
            score += card.value()
        return score
