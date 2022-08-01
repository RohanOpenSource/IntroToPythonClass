list = [1, 3, 4, 7 , 2, 3, 10 , 8]

#max of all the values of the list
val = 0
for i in list: 
    if(i > val)
      val = i
    # val = max(val, i)
  
print(val)

# first 100 integers
for i in range(1, 101):
  print(i)

# evens until 100
for i in range(1, 101, 2):
  print(i)

l = 50, r= 100
range_sum = 0
for i in range(l, r + 1):
  range_sum += i
print(range_sum)

i = 1
while (i <= 100):
  print(i)
  i += 1

print("done")

while(True):
  stop = input("Type 0 to stop: ")
  if(stop == "0"):
    break

print("done")


fruits = ["apples", "cherries", "bananas"]
adj = ["red", "big", "tasty"]

done = False
for fruit in fruits:
  for a in adj:
    likes = input("do you like " + a + " " + fruit + ": ")
    if(likes == "1"):
      print("have some: " + a + " " + fruit)
      done = True
      break
  if(done):
    break
print("Done")
