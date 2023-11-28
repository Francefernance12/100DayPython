from BlackJackArt import logo
from random import randint
import sys


def calculate_score(cards):
    score = sum(cards)
    return score


def game_over():
    retry = input("Do you want to retry? Type 'y' or 'n': ").lower()
    if retry == "y":
        blackjack()
    else:
        print("Thanks for playing!")
        sys.exit()


def hit():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = cards[randint(0, len(cards) - 1)]

    return new_card


def winners(player_score, computer_score):
    # chooses winner
    print(f"Player score is, {player_score}")
    print(f"Computer score is, {computer_score}")
    if player_score > computer_score:
        print("Player wins!")
        game_over()
    elif player_score < computer_score:
        print("Computer wins!")
        game_over()         # special rule for blackjack
    elif player_score == 21 and computer_score == 21:
        blackjack_draw = input("WOW! Two BlackJack! Do you want to push? Type 'y' or 'n': ")
        if blackjack_draw == "y":
            print("Push!")
            push(player_score, computer_score)
        else:
            print("it's a draw!")
            game_over()
    else:
        print("It's a draw!")
        game_over()


def push(player_score, computer_score):
    print("You and the computer have decided pushed.")
    # player_score
    new_player_card = hit()
    player_score += new_player_card
    print(f"Your new score is, {player_score}")

    # new computer score
    new_computer_card = hit()
    computer_score += new_computer_card
    print(f"Computer new score is, {computer_score}")

    # decides winner again
    if player_score == computer_score:
        retry = input("You both somehow looped back to the same score! Want to keep trying? type 'y' or 'n': ").lower()
        if retry == "y":
            push(player_score, computer_score)
        elif retry == "n":
            game_over()
    else:
        winners(player_score, computer_score)


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == 'y':
        print(logo)
        # player
        player_cards = [cards[randint(0, len(cards) - 1)], cards[randint(0, len(cards) - 1)]]
        player_score = calculate_score(player_cards)

        if player_cards == 11 and player_cards == 10:
            player_score = 21
            print(f"Computer got a blackjack!")

        print(f"Your cards: {player_cards}. your current score {player_score}")

        # computer
        computer_cards = [cards[randint(0, len(cards) - 1)]]
        computer_score = sum(computer_cards)
        print(f"Computer's cards: {computer_cards}")

        bust = False
        while not bust:
            # will player choose to draw another card or not
            hit_pass = input("type 'hit' for another card or 'pass': ").lower()
            # if player hits, it will add another card to player list
            if hit_pass == "hit":
                new_card = hit()
                player_cards.append(new_card)
                player_score = calculate_score(player_cards)

                print(f"Your cards: {player_cards}. your score {player_score}")
                if player_score > 21:
                    print(f"Busted! You went over 21! Your score: {player_score}. Computer Won!")
                    game_over()
            elif hit_pass == "pass":    # pass
                bust = True
        # after the player is done drawing cards, it will add the computer cards
        # computer score can't be less than 17
        while computer_score < 17:
            if computer_score < 17:
                new_computer_card = hit()
                computer_cards.append(new_computer_card)
                computer_score = calculate_score(computer_cards)
                if computer_score > 21:
                    print(f"Busted! Computer Lost! Player won! Computer score {computer_score} and cards {computer_cards}.")
                    game_over()
                elif computer_cards == 11 and computer_cards == 10:
                    computer_score = 21
                    print(f"Computer has blackJack!")

            else:
                break

        winners(player_score, computer_score)
    # player chooses pass
    else:
        print("Goodbye!")


blackjack()
