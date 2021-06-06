from object_oriented_design.card import Card
from object_oriented_design.rank import Rank


class BlackJackCard(Card):

    def __init__(self, rank, suite):
        super().__init__(rank, suite)

    def value(self):
        if self.rank == Rank.Ace:
            return 1
        elif self.rank == Rank.King or self.rank == Rank.Queen or self.rank == Rank.Jack:
            return 10
        else:
            return self.rank.value

    def is_ace(self):
        return self._rank == Rank.Ace
