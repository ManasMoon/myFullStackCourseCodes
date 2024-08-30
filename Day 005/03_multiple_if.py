a = int(input("Enter your age: "))

# If statement no. 1
if(a%2 == 0):
          print("a is Even")
#End of statement 1

# If statement no. 2
if(a>=18):
          print("You can vote")
elif(a==17):
          print("One more year to vote")
elif(a<0):
          print("Please give valid age")
else:
          print("You cannot vote")
# End of statement 2

print("Thank you")



