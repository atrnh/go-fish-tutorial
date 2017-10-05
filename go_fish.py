import random
from collections import defaultdict


def print_card(card):
    """Print out the rank and suit of a card tuple."""

    print "|{} of {}|".format(*card)


def print_cards(cards):
    """Print a collection of card tuples."""

    map(lambda card: print_card(card), cards)


class Player(object):
    """Go Fish player base class."""

    def __init__(self, name):
        self.name = name
        self.hand = defaultdict(list)

    def __repr__(self):
        return "<Player name={}>".format(self.name)

    def print_hand(self):
        print_cards([(rank, suit)
                     for rank in self.hand
                     for suit in self.hand[rank]
                     ])
        print

    def update_hand(self, cards):
        for card in cards:
            print card
            rank, suit = card
            if rank in self.hand:
                self.hand[rank].append(suit)
            else:
                self.hand[rank] = [suit]

    def get_cards_by_rank(self, rank):
        if rank in self.hand:
            return [(rank, suit) for suit in self.hand[rank]]
        else:
            return None

    def del_cards_by_rank(self, rank):
        del self.hand[rank]

    def ask_for_rank(self, rank, player_to_ask):
        print "{name}:".format(name=self.name)
        print ("{other_player}, do you have any " +
               "{rank}s?\n").format(other_player=player_to_ask.name,
                                    rank=rank)

        return player_to_ask.ans_for_rank(rank)

    def ans_for_rank(self, rank):
        print "{name}:".format(name=self.name)

        cards_of_rank = self.get_cards_by_rank(rank)

        if cards_of_rank:
            self.del_cards_by_rank(rank)
            print "Yup, here are my {rank}s.\n".format(rank=rank)
            print_cards(cards_of_rank)
            print
        else:
            print "Nope. Go fish."

        print 'debug'
        print cards_of_rank

        return cards_of_rank


class Computer(Player):
    def ask_for_rank(self, player_to_ask):
        """Ask if a player has a randomly chosen rank."""

        # Remember:
        # - dict.keys() gives you a list of all the keys in a dict.
        # - random.choice() returns a random object from a sequence.
        # - lists are sequences so we can use the list we got from
        #   self.hand.keys() to get a randomly chosen rank
        rank = random.choice(self.hand.keys())

        super(Computer, self).ask_for_rank(rank, player_to_ask)


class User(Player):
    def print_hand(self):
        print "Your hand:"
        super(User, self).print_hand()

    def ask_for_rank(self, rank, player_to_ask):
        if rank in self.hand:
            return super(User, self).ask_for_rank(rank, player_to_ask)


def make_deck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = range(2, 11) + ['A', 'J', 'Q', 'K']

    # deck = []
    #
    # for rank in ranks:
    #     for suit in suits:
    #         deck.append((rank, suit))
    #
    # return deck

    return [ (str(rank), suit) for rank in ranks for suit in suits ]


def deal_cards(deck, players):
    random.shuffle(deck)

    for player in players:
        player.update_hand(deck[0:5])

        deck = deck[5:]

    return deck


def draw_card_for_player(deck, player):
    player.update_hand([deck.pop()])

    return deck






deck = [('7', 'hearts'), ('2', 'clubs'), ('A', 'spades')]
user = User(raw_input('What\'s your name?\n>'))
player_1 = Computer('Al')
player_1.hand = {'A': ['hearts', 'diamonds']}
user.hand = {'A': ['clubs'], '2': ['diamonds']}

user.print_hand()
print "\nChoose a rank from your hand:"
rank = raw_input("rank > ")
print
cards = user.ask_for_rank(rank, player_1)
print

print 'debug'
print cards
print cards == True
print

if cards is not None:
    print "if statement"
    print cards
    user.update_hand(cards)

print "You put the cards into your hand \n"
user.print_hand()
print
print "The computer's hand:\n"
player_1.print_hand()
print
user.ask_for_rank('2', player_1)
print
