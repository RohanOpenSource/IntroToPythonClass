#program to find the Prime Factors of a number
a = int(input("Which number do you want to find the prime factors of? "))

for i in range(2, a + 1): #prime numbers start at 2
  if(a % i == 0):
    prime = True;
    for j in range(2, i): #the only two divisors prime numbers have are 1 and n so we leave them out
      if(i % j == 0):
        prime = False;
        break;
    if(prime): 
      print(i)
