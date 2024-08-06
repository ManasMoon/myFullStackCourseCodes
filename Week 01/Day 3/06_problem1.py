# Write a python program to display a user entered name followed by Good Afternoon using input () function.

name = input("Naam daal lavde: ")
message = "Good Afternoon, " + name + "!"
print(message) 
#Output: Good Afternoon, Manas! (Using Concatenation)

# new method in python update : f strings
print(f"Good Afternoon {name}!!") 
#Output: Good Afternoon Manas!! (Using f strings)