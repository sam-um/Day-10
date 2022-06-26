
import random
import art

def get_card():
  selected_card = cards[random.randint(0, len(cards) - 1)]
  cards.remove(selected_card)
  return(selected_card)

def get_next_card():
  next_card = input("Type 'y' to get another card, type 'n' to pass: ")
  if next_card == "y":
    player_cards.append(get_card())
    if sum(player_cards) > 21 and 11 in player_cards:
      player_cards.remove(11)
      player_cards.append(1)
      print(f"  Your cards: {player_cards}, current score: {sum(player_cards)}")
      get_next_card()
    elif sum(player_cards) > 21:
      print(f"  Your final cards: {player_cards}, final score: {sum(player_cards)}")
      print("  You lose.")
    else:
      print(f"  Your cards: {player_cards}, current score: {sum(player_cards)}")
      get_next_card()
  else:
    get_result()

def get_result():
  print(f"  Your final cards: {player_cards}, final score: {sum(player_cards)}")
  while sum(computer_cards) < 16:
    computer_cards.append(get_card())
  print(f"  Computer's final cards: {computer_cards}, final score: {sum(computer_cards)}")
  if sum(computer_cards) > 21 or sum(player_cards) > sum(computer_cards):
    print(f"  You win!")
  elif sum(player_cards) == sum(computer_cards):
    print(f"  Draw")
  else:
    print(f"  You lose.")

def play():
  print(art.logo)
  player_cards.append(get_card())
  computer_cards.append(get_card())
  player_cards.append(get_card())
  print(f"  Your cards: {player_cards}, current score: {sum(player_cards)}")
  print(f"  Computer's first card: {computer_cards}")
  get_next_card()
  play_again()

def play_again():
  clear()
  play_again_input = input("Do you want to play again? Type 'y' or 'n': ")
  if play_again_input == "y":
    player_cards.clear()
    computer_cards.clear()
    play()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
player_cards = []
computer_cards = []

play_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_input == "y":
  play()