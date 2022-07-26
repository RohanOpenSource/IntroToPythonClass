query = input("Do you like programming? ")
answers = ["Yes", "yes", "yeah", "certainly", "Certainly", "Yeah", "yES"]
half_credit_answers = ["Kind of", "kinda", "maybe", "partially"]
negative_credit_answers = ["No", "no way", "A non"]
score = 0
if(query in answers):
  score += 2
elif(query in half_credit_answers):
  score += 1
elif(query in negative_credit_answers):
  score -= 1
else:
  query = input("Wrong Answer! Do you like programming? ")
  if(query in answers):
    score += 1
  else:
    print("You got the wrong answer again! The answer is " + answers[0])

print("Your current score is: " + str(score))
