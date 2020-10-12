from random import randint
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🔴", "🟢", "🟡", "🔵"]


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def ___str___(self):
        return f"{self.color} {self.number}"


class Player:

    def __init__(self, name):
        self.name = name


class Deck:
    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = (color, number)
                self.cards.append(card)

    def shuffle(self, cards):
        deck_copy = self.cards
        random_deck = []
        while len(deck_copy) > 0:
            random_card = deck_copy[randint(0, len(deck_copy) - 1)]
            random_deck.append(random_card)
            deck_copy.remove(random_card)
        return random_deck


class Game:
    pass
