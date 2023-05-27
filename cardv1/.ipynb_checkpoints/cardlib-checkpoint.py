import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    
    def show_card(self):
         return self.suit, self.value


class Deck:
    def __init__(self, game):
        self.deck = []
        self.game = game

    # Creates the actual deck
    def create_deck(self):
        if self.game.lower() == "euchre":
            suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
            values = ["King", "Queen", "Jack", "10", "9", "Ace"]
            for i in range(len(suits)):
                for j in range(len(values)):
                    new_card = Card(suits[i], values[j])
                    self.deck.append(new_card)
                    
        return self.deck

    # Returns a shuffled deck
    def shuffle(self):
        if len(self.deck) == 0:
            self.deck = Deck(self.game).create_deck()
        temp_deck = self.deck.copy()
        self.deck = []

        while(len(temp_deck) != 0):
            shuffle_index = random.randint(0,len(temp_deck)-1)
            
            self.deck.append(temp_deck[shuffle_index])
            temp_deck.pop(shuffle_index)

        return self.deck
        
    # Used for dealing cards to players
    def add_card(self, card):
        self.deck.append(card)

    # Deals out all cards in deck to 4 different players
    def deal_cards(self):
        deck1 = Deck(self.game)
        deck2 = Deck(self.game)
        deck3 = Deck(self.game)
        deck4 = Deck(self.game)
        anti_card_count = Deck(self.game)
        decks = [deck1, deck2, deck3, deck4]
        
        self.deck = Deck(self.game).shuffle()

        while(len(self.deck) != 4):
            for i in range(len(decks)):
                decks[i].add_card(self.deck[0])
                self.deck.pop(0)

        # 4 cards discarded in order to prevent card counting
        # First card is flipped
        while(len(self.deck) != 0):
            anti_card_count.add_card(self.deck[0])
            self.deck.pop(0)

        return deck1, deck2, deck3, deck4, anti_card_count
        
            
    # Used to print out all the user's cards
    def reveal_cards(self):
        count = 1
        for card in self.deck:
            suit, value = card.show_card()
            print(f"{count}. {suit}\t{value}")
            count+=1

    # Allows user to put down a card and discards it from deck
    def place_card(self, index):
        try:
            print(self.deck[index].show_card())
            self.deck.pop(index)
        except Exception as e:
            print(e.args[0])