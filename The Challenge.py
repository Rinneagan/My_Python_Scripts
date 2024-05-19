def get_player_number(player_number):
  """Gets a valid integer input from the player."""
  while True:
    try:
      number = int(input(f"Player {player_number}, enter your number: "))
      if number >= 1:
        return number
      else:
        print("Number must be greater than or equal to 1.")
    except ValueError:
      print("Enter a valid integer.")

def calculate_points(player1_number, player2_number):
  """Calculates points based on the chosen numbers."""
  if player1_number == player2_number:
    return 0, 0  # No points for either player
  elif player1_number < player2_number:
    if player2_number - player1_number == 1:
      return 0, 2  # Player 2 gets 2 points
    if player1_number - player2_number == 1:
      return 2, 0  # Player 1 gets 2 points
    else:
      return 1, 0  # Player 1 gets 1 point
  else:
    return 0, 1  # Player 2 gets 1 point

def play_game():
  """Plays the game loop."""
  player1_points = 0
  player2_points = 0

  while player1_points < 5 and player2_points < 5:
    player1_number = get_player_number(1)
    player2_number = get_player_number(2)

    player1_point, player2_point = calculate_points(player1_number, player2_number)

    player1_points += player1_point
    player2_points += player2_point

    print(f"Player 1: {player1_number}, Player 2: {player2_number}")

    if player1_point > 0:
      print(f"Player 1 gets {player1_point} point(s).")
    elif player2_point > 0:
      print(f"Player 2 gets {player2_point} point(s).")

    print(f"Current score: Player 1 : {player1_points}, Player 2 : {player2_points}")

  if player1_points == 5:
    print("Player 1 wins!")
  else:
    print("Player 2 wins!")

# Start the game
play_game()
