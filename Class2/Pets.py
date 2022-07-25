x = input("Enter the number of pets you have: ")
x = int(x)

# x > 10 -> you are crazy
# 10 >= x > 7 -> you are still pretty crazy
# 7 >= x> 4 -> somewhat reasonable
# x <= 4 You are sensible 
if(x > 10) :
  print("You are crazy")
elif(x >7):
  print("you are still crazy")
elif(x > 4):
  print("You are somewhat reasonable")
else: 
  print("You sensible")
  
print("Done")
