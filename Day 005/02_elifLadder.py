a = int(input("Enter your age: "))

# if-elif-else ladder.
if(a>=18):
          print("You can vote")
elif(a==17):
          print("One more year to vote")
elif(a<0):
          print("Please give valid age")
else:
          print("You cannot vote")

print("Thank you")