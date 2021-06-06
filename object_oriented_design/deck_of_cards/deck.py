from random import shuffle


class Deck:
    def __init__(self, cards):
        self._cards = cards
        self._dealtIndex = 0
        self.shuffle()

    def remaining_cards(self):
        return len(self._cards) - self._dealtIndex

    def shuffle(self):
        shuffle(self._cards)

    def __str__(self):
        return f'[{", ".join(str(card) for card in self._cards)}]'

    def draw(self):
        if self.remaining_cards() == 0:
            raise Exception("No card available.")
        self._dealtIndex += 1
        return self._cards[self._dealtIndex - 1]
