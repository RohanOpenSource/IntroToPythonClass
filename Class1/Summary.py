
weather = input("Enter weather: (Today is a warm/cold day): ") # Summarizing everything we learned  today
temprature = weather[11:15] #indexing the list from the 11th index to the 14th inclusive

age = input("How old are you: (I am x years old)")
age = int(age[5])
years_left = 21 - age

pet = input("Which pet do you own, and how many? (I own x dogs/cats)")
number_of_pets = int(pet[6])
pet_type = pet[8:]

name = input("What is your name? (My name is (Atharv))")
name = name[11:]

print("Hello " + name + "\n you need: " + str(years_left) + " years to drive.")
print("You have " + str(number_of_pets) + " " + pet_type + " And it is " + temprature)
