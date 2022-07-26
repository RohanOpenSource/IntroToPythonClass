import random #imports random package
NUM_GUESSES = 10
number = random.randint(1, 100) #generates random integer between 1 and 100
remaining_guesses = NUM_GUESSES
guessed = False
while(remaining_guesses > 0):
  print("You have: " + str(remaining_guesses) +" guesses left")
  guess = int(input("Guess a number: "))
  if(guess > number): 
    print("Too high! ")
  elif(guess < number):
    print("Too low! ")
  else:
    guessed = True
    break
  remaining_guesses -= 1

if(guessed): 
  print("GOOD JOB! You Guessed the number!")
else:
  print("You didn't guess the number. It was " + str(number))
