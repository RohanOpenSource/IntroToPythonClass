print("Hello World") #prints the value of the string inside
text = "Hello World" # this is a variable. It is currently being assigned a string value
print(text) # we are now printing that string value
#What if we wanted to print out only hello?
print(text[0:5]) # the first index we want is 0 (since all lists start with the index 0. The last index we want is 4 so we put 5 as are endpoint since the endpoint is excluded

a = 5 # these variables are being assigned integer values (aka numbers)
b = 10
sum = a + b #add numbers using the addition operator
product = a * b;
quotient = a / b;
difference = a - b;
remainder = a % b; #modulo operator takes remainder
print("Sum: " + str(sum)) # str operator converts a variable of any type to a string
print("Product: " + str(product)) # only strings can be printed
print("Quotient: " + str(quotient)) # when the plus operator is used on strings
print("Difference: " + str(difference)) # the two strings are concatinated (merged)
print("Remainder: " + str(remainder))

over_16 = True # these variables are being assigned boolean values (aka True or False)
passed_driving_test = False

not_over_16 = not over_16 # not operator gives the opposite of a boolean value (True -> False and False -> True)
print("Under 16: " + str(not_over_16))
can_drive = (over_16 and passed_driving_test)
print("Can Drive: " + str(can_drive))

#lets make this interactive
first_number_string = input("Enter a number: ") # input takes in a string from the console. The program stops until a string is entered. I am then assigning this string to the variable first_number
first_number = int(first_number_string) #this converts the string into an integer which we can then use to add. If we did not do this, our two numbers would be concatenated and not added. You can do the same thing with the bool() method to convert to a boolean
second_number = int(input("Enter another number: ")) # we can also convert before storing a variable to save memory and our time

sum = first_number + second_number

print("The sum of the two numbers is: " + str(sum)) # again to concatenate our result with the placeholder text, we need to convert it into a string with the str method
