# Inputs lots of data about the user and summarize it for them
# Summarizing everything we learned today with inputs, data types, strings, and type conversions!

weather = input("Enter weather: (Today is a warm/cold day): ")
temprature = weather[11:15] #indexing the list from the 11th index to the 14th inclusive

age = input("How old are you: (I am x years old)") # read input in string form
age = int(age[5]) # parse out age and type cast to integer
years_left = 16 - age # calculate years until you can drive

pet = input("Which pet do you own, and how many? (I own x dogs/cats)") # read input in string form
number_of_pets = int(pet[6]) # parse out number of pets and cast to integer
pet_type = pet[8:] #use indexing from the 8th element (inclusive) all the way to the end of the string to get the type of pet

name = input("What is your name? (My name is (Atharv))")
name = name[11:] #index from 11th element to end of string to get name

print("Hello " + name + "\n you need: " + str(years_left) + " years to drive.") # concatenate strings, type cast integers, and use new line characters
print("You have " + str(number_of_pets) + " " + pet_type + " And it is " + temprature + " near you today")
