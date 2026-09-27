# FREEZE CODE BEGIN
import random
# FREEZE CODE END

secret_code = []
tries = 0

# Code generation functions
def gen_seed():
  """
  Seeds the random generator.
  """
  random.seed(input("Please enter a seed:\n"))

def check_valid_code(code):
  """
  Checks the following conditions:
  -Is numeric
  -Has four unique digits
  -Each number does not appear more than once
  """
  if code.isnumeric() == True and len(code) == 4:
    for digit in str(code):
      if (str(code)).count(digit) >= 2:
        return False
    return True
  else:
    return False

#Guessing Logic
def code_check(code):
  global secret_code
  arrayed_code = [int(num) for num in code]
  bulls = 0
  cows = len(set(arrayed_code) & set(secret_code))
  for i in range(4):
    if arrayed_code[i] == secret_code[i]:
      bulls += 1
      cows -= 1
  return (bulls, cows)

# Game set up functions
def initialize_secret_code():
  """
  Asks for if code is numeric first, then checks for 1 or 2.
  """
  user_input = input()
  global secret_code
  if user_input.isnumeric() == False:
    initialize_secret_code()
  elif int(user_input) == 1: #Computer Generated Approach
    gen_seed()
    new_secret_code = []
    while len(new_secret_code) != 4:
      digit = random.randint(0,9)
      if digit not in new_secret_code:
        new_secret_code.append(digit)
    secret_code = new_secret_code
  elif int(user_input) == 2: #User Given Approach
    valid_code_given = False
    while valid_code_given == False:
      user_code = input("Type in the secret code:\n")
      if check_valid_code(user_code) == False:
        print("There was a problem processing your input. Please type exactly four unique digits.")
      else:
        new_secret_code = []
        for digit in user_code:
          new_secret_code.append(int(digit))
        secret_code = new_secret_code
        valid_code_given = True

def choose_difficulty():
  global tries
  while True:
    num = input("Choose a difficulty level:\n1. Easy (12 guesses)\n2. Medium (8 guesses)\n3. Hard (5 guesses)\n")
    if num.isnumeric() == False:
      print("There was a problem processing your input. Please type 1, 2, or 3.")
    if int(num) == 1:
      tries = 12
      break
    if int(num) == 2:
      tries = 8
      break
    if int(num) == 3:
      tries = 5
      break
    else:
      print("ERROR: choose_difficulty function does not have valid input")

def guess():
  global tries
  while tries > 0:
    user_guess = input("Guess the code (type 'give up' if you would like to quit the game):\n")
    if check_valid_code(user_guess):
      bulls, cows = code_check(user_guess)
      if bulls == 4:
        print("You win!")
        return
      else:
        tries -= 1
        print(f"Bulls: {bulls}")
        print(f"Cows: {cows}")
        print(f"You have {tries} guesses left.")
    elif user_guess.lower().strip() == "give up":
      return
    else:
      print("There was a problem processing your input. Please type exactly four unique digits.")
  string_code = ""
  for number in secret_code:
    string_code += (str(number))
  print(f"You lose; the correct answer was {string_code}")



# Game Logic and Loop
print("Welcome to Bulls and Cows!")
while True:
  print("Type '1' if you would like the computer to generate a secret code or '2' if you want to input it yourself:")
  initialize_secret_code()
  choose_difficulty()
  guess()
  play_again = input("Would you like to play again? (y/n):\n").lower().strip()
  if play_again != "y":
    break
