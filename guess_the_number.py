import random
def play_game(lower_bound, upper_bound):
  # Generate a random number
  secret_number = random.randint(lower_bound, upper_bound)
  # Keep track of the number of attempts
  attempts = 0
  # Start the game loop
  while True:
    attempts += 1
    # Get a guess from the user
    while True:
      try:
        guess = int(input(f"Guess a number between {lower_bound} and {upper_bound} (attempt {attempts}): "))
        if lower_bound <= guess <= upper_bound:
          break
        else:
          print("Invalid input. Please enter a number within the specified range.")
      except ValueError:
        print("Invalid input. Please enter a valid number.")
    # Check the guess
    if guess == secret_number:
      print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
      break
    elif guess < secret_number:
      print("Too low, try again!")
    else:
      print("Too high, try again!")
# Default game settings
lower_bound = 1
upper_bound = 100
# Play the game
play_game(lower_bound, upper_bound)