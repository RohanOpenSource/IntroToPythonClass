import random

in_word = False

word_bank = ["red", "orange", "yellow", "green", "blue", "magenta", "turquoise", "lilac", "white", "gray"]

def pick_random_word():
  random_index = random.randint(0, len(word_bank) - 1)
  return word_bank[random_index]
  
def is_equal(arr, str):
  for i in range (0, len(arr)):
    if(arr[i] != str[i]): 
      return False
  return True

def status_update(display, num_guesses, guessed_letters):
  print(display)
  print("You have " + str(num_guesses) + " guesses left")
  print("You have guessed " + str(guessed_letters))
  
word = pick_random_word()
num_guesses = 5
display = []
guessed_letters = []
for i in range(0, len(word)):
  display.append("_")

won = False;
while num_guesses > 0:
  status_update(display, num_guesses, guessed_letters)
  
  input_letter = input("guess a letter: ")

  in_word = False

  guessed_letters.append(input_letter)
  
  for i in range(0, len(display)):
    if(word[i] == input_letter):
      in_word = True
      display[i] = input_letter

  if(is_equal(display, word)):
    won = True
    break

  if(not in_word):
    num_guesses -= 1

if won:
  print("You Guessed The Word " + word + " good job!")

else:
  print("You were close! The word was: " + word)
