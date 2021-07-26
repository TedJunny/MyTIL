import black_jack_classes as black_jack


playing = True
chips_counted = 100


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("\nHow many chips would you like to bet? "))
        except ValueError:
            print("Sorry, a bet must be an integer number!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed ", chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("\nWould you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == "h":
            hit(deck, hand)
        elif x[0].lower() == "s":
            print("\nPlayer stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep="\n ")


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("\nDealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("\nPlayer's Hand =", player.value)


def player_busts(chips):
    print("\nPlayer busts!")
    chips.lose_bet()


def player_wins(chips):
    print("\nPlayer wins!")
    chips.win_bet()


def dealer_busts(chips):
    print("\nDealer busts!")
    chips.win_bet()


def dealer_wins(chips):
    print("\nDealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("\nDealer and Player tie! It's a push.")


while True:
    print(
        "\nWelcome to BlackJack! Get as close to 21 as you can without going over!"
        + "\nDealer hits until she reaches 17. Aces count as 1 or 11."
    )

    deck = black_jack.Deck()
    deck.shuffle()

    player_hand = black_jack.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = black_jack.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = black_jack.Chips(chips_counted)
    take_bet(player_chips)
    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push(player_hand, dealer_hand)

    print("\nPlayer's winnings stand at", player_chips.total)
    chips_counted = player_chips.total
    new_game = input("\nWould you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
