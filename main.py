### Setup Section ###

# Loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

      
# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):
  secret = ""
  
  # Loop through each index/position 
  for index in range(6):
    
    # Grab the letter from the guess
    letter = guess[index]
    secret = actual
    
    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in secret):

      # Check if the letter is also at the current index in the secret word
      if(letter == secret[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)
       
      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
               
        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)
          
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
      
    # Handles the transition between colors
    print(Style.RESET_ALL + " ", end="")

    
# A Function that takes in a six-lettered word from the user
def getSixLetterInput(guess):
  guessUser = ""
  while(len(guessUser) != 6):
    guessUser = input("Enter a six letter word: ")
    print()
  return guessUser.lower()

# End of the function definitions
  

### Main Program ###

# Display a friendly title and a welcome message
# Display title of quiz show in ASCII art
print(r"""

__        _____  ____  ____       _   _    _    _   _  ____ 
 \ \      / / _ \|  _ \|  _ \     | | | |  / \  | \ | |/ ___|
  \ \ /\ / / | | | |_) | | | |    | |_| | / _ \ |  \| | |  _ 
   \ V  V /| |_| |  _ <| |_| |    |  _  |/ ___ \| |\  | |_| |
    \_/\_/  \___/|_| \_\____/     |_| |_/_/   \_\_| \_|\____|
                                                             

""")
print("-   -   -   -   -   -")
print("Welcome to Word Hang!")
print("-   -   -   -   -   -")
print()
print("====={ Rules }=======")
print()

# Write the logic of the game here!
print("You have six tries to get the word correct")
print("The word is SIX CHARACTERS long, and you must enter a guess of this length")
print("If a letter is in the correct place, it will be green")
print("If a letter is in the word but NOT in the correct place, it will be yellow")
print("If the letter is NOT in the word, it will be red")
print("=====================")
print()
print("Ok, time to start! When you are ready,")
print()

actual = "secret"
guess = ""
count = 0


# Repeat the user's turn until they either run out of tries or guess the word correctly
while(count < 6 and guess != actual):
  guess = getSixLetterInput(guess)
  
# On each turn, take in a word, and show them how accurate it is using color-coded background
  printGuessAccuracy(guess, actual)
  count += 1

  if(count == 6):
    print()
    print()
    print("You are out of tries.")
    
    
# When user is finished, tell them if they won or lost
if(guess == actual):
  print()
  print()
  print("You win!")
else:
  print()
  print("You lost!")
