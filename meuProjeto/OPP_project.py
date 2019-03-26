from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

mycards = [(s, r) for s in SUITE for r in RANKS]


class Deck:
    def __init__(self):
        print("Creating New OrderedDeck!")
        self.all_cards = mycards

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.all_cards)

    def split_in_half(self):
        return (self.all_cards[:26], self.all_cards[26:])


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []

        if len(self.hand.cards) < 3:
            return self.hand.cards

        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())

            return war_cards

    def still_has_cards(self):
        """
        :return: True if player still have cards left

        """
        return len(self.hand.cards) !=0


# GAME PLAY

print("Welcome to War, let's begin...\n")

d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

comp_player = Player("computer", Hand(half1))

name = input("What is your name?")
user = Player(name, Hand(half2))

total_rouds = 0

war_count = 0

while user.still_has_cards() and comp_player.still_has_cards():
    total_rouds += 1
    print("Time for a new round!")
    print("here are the current standings")
    print(user.name+", has the count"+str(len(user.hand.cards)))
    print(comp_player.name + ", has the count" + str(len(user.hand.cards)))
    print("play a card!")
    print("\n")

    table_cards = []
    c_card = comp_player.play_card()
    u_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(u_card)

    if c_card[1] == u_card[1]:
        war_count += 1
        print("war!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp_player.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp_player.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
            user.hand.add(table_cards)
        else:
            comp_player.hand.add(table_cards)

print("game over, number of rounds:"+str(total_rouds))
print("a war happened "+str(war_count)+" times")
print("Does the computer still have cards? ")
print(str(comp_player.still_has_cards()))
print("Does the {} still have cards? ".format(name))
print(str(user.still_has_cards()))
