def deck_game():
    def user_menu():
        choice = int(input("\nMENU:\n"
                           "1. Show deck card\n"
                           "2. Riffle shuffling \n"
                           "3. Random shuffling\n"
                           "4. Save deck and close\n"
                           "Please make your selection: "))
        return choice

    def deck_cards():
        cards_type = ["♦", "♣", "♥", "♠"]
        num = ["A", *range(2, 11), "J", "Q", "K"]
        deck = [(str(x) + y) for y in cards_type for x in num]
        return deck

    # Display deck without any brackets, comas or parentheses
    def display(deck):
        for item in range(len(deck)):
            if item % 10 == 0 and item != 0:
                print(f'\n{deck[item]}  ', end="")
            else:
                print(f'{deck[item]}  ', end="")
        return

    def riffle_shuffling(deck):
        
        # Split deck into 2 deck
        half_deck1 = deck[0:26]
        half_deck2 = deck[26:52]
        deck_shuffled_riffle = []

        for i in range(26):
            deck_shuffled_riffle.append(half_deck1[i])
            deck_shuffled_riffle.append(half_deck2[i])
        deck = deck_shuffled_riffle
        return deck

    def shuffle_deck(deck):

        # Split into 13 with 4 cards each
        deck1 = deck[0:4]
        deck2 = deck[4:8]
        deck3 = deck[8:12]
        deck4 = deck[12:16]
        deck5 = deck[16:20]
        deck6 = deck[20:24]
        deck7 = deck[24:28]
        deck8 = deck[28:32]
        deck9 = deck[32:36]
        deck10 = deck[36:40]
        deck11 = deck[40:44]
        deck12 = deck[44:48]
        deck13 = deck[48:52]

        deck = deck7 + deck1 + deck3 + deck13 + \
               deck2 + deck4 + deck11 + deck6 + \
               deck8 + deck5 + deck12 + deck10 + \
               deck9
        return deck

    def save(deck):
        f = open("cards.txt", "w", encoding='utf8')
        # When displaying the deck, it will change line every 10 cards
        for item in range(len(deck)):
            if item % 10 == 0 and item != 0:
                f.write(f'\n{deck[item]}  ')
            else:
                f.write(f'{deck[item]}  ')
        f.close()

    choix = user_menu()
    deck = deck_cards()

    while choix != 4:
        if choix == 1:
            display(deck)
        if choix == 2:
            deck = riffle_shuffling(deck)
        if choix == 3:
            deck = shuffle_deck(deck)
        choix = user_menu()

    save(deck)


deck_game()
