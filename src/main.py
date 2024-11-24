from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_card():
    return input("Type 'y' to get another card, type 'n' to pass: ")

def draw_a_card(card_list):
    random_card = random.choice(cards)
    card_list.append(random_card)
    return

def draw_hand(card_list):
    for initial_cards in range(2):
        random_card = random.choice(cards)
        card_list.append(random_card)
    return

def win_lose(score, player_cards, dealer_cards):
    if 11 in player_cards and score > 21:
        ace = player_cards.index(11)
        player_cards[ace] = 1
        score = sum(player_cards)
    print(f"Your cards: {player_cards}, current score: {score}")
    print(f"Computer's first card: {dealer_cards[0]}")
    if score > 21:
        print(f"Your final hand: {player_cards}, final score: {score}")
        print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
        print("You went over. You lose 😭")
    elif score == 21:
        print(f"Your final hand: {player_cards}, final score: {score}")
        print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
        print("You made 21! You win! 😆")
    return

def blackjack():
    play_blackjack = True
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":
        print("\n" *100)
        print(logo)
        while play_blackjack == True:
            hand_cards = []
            computer_cards = []
            current_score = 0
            computer_score = 0
            draw_hand(hand_cards)
            draw_hand(computer_cards)
            current_score = sum(hand_cards)
            computer_score = sum(computer_cards)
            print(f"Your cards: {hand_cards}, current score: {current_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if current_score == 21:
                print(f"Your final hand: {hand_cards}, final score: {current_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print("Win with a Blackjack 😎")
                print(play)
                blackjack()
            while current_score < 21:
                card = get_card()
                if card == "y":
                    draw_a_card(hand_cards)
                    current_score = sum(hand_cards)
                    win_lose(current_score,hand_cards,computer_cards)
                    current_score = sum(hand_cards)
                elif card == "n":
                    while computer_score < 17:
                        draw_a_card(computer_cards)
                        computer_score = sum(computer_cards)
                    print(f"Your final hand{hand_cards}, final score: {current_score}")
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                    if computer_score == 21:
                        print("Lose, opponent has Blackjack 😱")
                    elif computer_score > 21:
                        print("Opponent went over. You win 😆")
                    elif computer_score > current_score:
                        print("You lose 😤")
                    elif computer_score == current_score:
                        print("Draw 🙃")
                    else:
                        print("You win 😆")
                    current_score = 21
            play_blackjack = False
        blackjack()

blackjack()