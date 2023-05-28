from cardv1 import cardlib

class Player:
    # Args:  deck: Deck object, dealer: boolean
    def __init__(self, deck, dealer):
        self.deck = deck
        self.dealer = dealer

    def set_Dealer(self):
        self.dealer = True

    def check_if_dealer(self):
        return self.dealer


    # Args:  placed_is_red: boolean, trump_is_red: boolean
    # Returns: bool (if True, trump. if False, pass.)
    def check_Jacks(self, placed_is_red, trump_is_red, reds):
        jack_same_as_trump = []
        reason_to_trump = False
        temp_deck = self.deck.reveal_cards(False)
        for card in temp_deck:
            if placed_is_red and trump_is_red:
                # Player more inclined to pass if their jack is already the same color as trump
                # Statement checks for any jacks that are the same color as the trump
                if card.show_card()[0] in reds and card.show_card()[1] == 'Jack':
                    jack_same_as_trump.append(False)
                
                # Statement checks for any jacks that aren't the same color as the trump
                if card.show_card()[0] not in reds and card.show_card()[1] == 'Jack':
                    jack_same_as_trump.append(True)

        for jack in jack_same_as_trump:
            # If there is a jack with the same color as the trump, pass.
            # Otherwise, there is reason to trump
            if jack:
                reason_to_trump = True
        return reason_to_trump

        
    # Args:  current_card_color: string, current_card_value: string, current_trump: string
    def call_trump(self, current_card_color, current_card_value, current_trump):
        reds = ('Hearts', 'Diamonds')
        blacks = ('Spades', 'Clubs')
        placed_isRed = False
        trump_isRed = False
        trump = False

        # Checks if card is red or not
        if current_card_color in reds:
            placed_isRed = True
        if current_trump in reds:
            trump_isRed = True

        trump = self.check_Jacks(placed_isRed, trump_isRed, reds)

        return trump


    # Args:  current_deck: Card object array, current_card: Card object, current_trump: string, first_round: boolean,
    #           player_choice: int
    # Returns: boolean
    def check_forCard(self, current_card, current_trump, first_round, is_player = 0):
        # Used to guide certain instances
        current_card_color = current_card.show_card()[0]
        current_card_value = current_card.show_card()[1]
        trump = False

        # If is_player is 1, trump. If is_player is 2, pass. If is_player is 0, CPU option
        if first_round:
            if is_player == 0:
                if self.call_trump(current_card_color, current_card_value, current_trump):
                    return True
                return False
            if is_player == 1:
                return True
            if is_player == 2:
                return False
            else:
                print("Invalid play. Turn skipped.")
                return False

    def reveal_cards(self):
        self.deck.reveal_cards(True)

    def swap_cards(self, player_card_index, other_deck, other_card_index):
        self.deck.swap_card(player_card_index, other_deck, other_card_index)


    