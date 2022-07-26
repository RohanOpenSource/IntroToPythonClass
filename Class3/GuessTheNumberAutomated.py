import random
NUM_GUESSES = 10
number = random.randint(1, 100)
remaining_guesses = NUM_GUESSES
guessed = False
low = 1
high = 100
while(remaining_guesses > 0):
  print("You have: " + str(remaining_guesses) +" guesses left")
  guess = round((low + high) / 2)
  print(guess)
  if(guess > number): 
    print("Too high! ")
    high = guess
  elif(guess < number):
    print("Too low! ")
    low = guess
  else:
    guessed = True
    break
  remaining_guesses -= 1

if(guessed): 
  print("GOOD JOB! You Guessed the number!")
else:
  print("You didn't guess the number. It was " + str(number))
