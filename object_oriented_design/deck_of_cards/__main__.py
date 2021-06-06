"""
design  the datta structures for generic deck of cards. Explain how you would subclass the data structures to
implement blackjack.
"""
from object_oriented_design.deck_of_cards.black_jack_hand import BlackJackHand
from object_oriented_design.deck_of_cards.deck import Deck
from object_oriented_design.deck_of_cards.black_jack_card import BlackJackCard
from object_oriented_design.deck_of_cards.rank import Rank
from object_oriented_design.deck_of_cards.suite import Suite


cards = []

for suite in Suite:
    for rank in Rank:
        cards.append(BlackJackCard(rank, suite))

deck = Deck(cards)

assert deck.remaining_cards() == 52

# hand1 = BlackJackHand([deck.draw(), deck.draw()])
# hand2 = BlackJackHand([deck.draw(), deck.draw()])

hand1 = BlackJackHand()
hand2 = BlackJackHand()

hand1.add_card(deck.draw())
hand2.add_card(deck.draw())

hand1.add_card(deck.draw())
hand2.add_card(deck.draw())

print(hand1.score())
print(hand2.score())
