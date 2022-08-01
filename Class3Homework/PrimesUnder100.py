primes = [] #Store as an empty list, we will use the append() method to add elements to it
for i in range(1, 101):
    is_prime = True # Assume the current value of i is prime
    for j in range(2, i): #Notice j will only ever be between 2 and i-1, since it wont include i: (Primes will always be divisible by themselves and 1)
        if(i % j == 0):
            is_prime = False # If we find a single divisor of i (between 2 and i-1), then its not prime
            break # If we know its not prime, there is no need to continue looping through possible divisors
    if(is_prime): 
        primes.append(i) # this will only run when we never find any values j in range(2, i) such that j divides i. 

print(primes)
