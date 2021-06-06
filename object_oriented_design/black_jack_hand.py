from object_oriented_design.hand import Hand


class BlackJackHand(Hand):

    def __init__(self, cards=None):
        super().__init__(cards)

    def score(self):
        score = 0
        for card in self._cards:
            if not card.is_ace():
                score += card.value()
        for card in self._cards:
            if card.is_ace() and score < 21:
                score += 11
            else:
                score += 1
        return score
