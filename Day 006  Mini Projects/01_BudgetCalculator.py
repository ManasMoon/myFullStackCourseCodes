'''
Create a budget calculator using input function
We need to calculate
1. Your Snacks & Tiffin charges
2. Your share of rent & electricity bill
'''

tiffin = int(input("Enter your tiffin amount: "))
snacks = int(input("Enter your snacks amount: "))
rent = int(input("Enter total rent amount: "))
electricity = int(input("Enter total electricity bill amount: "))

personal = tiffin + snacks
share = (rent+ electricity)/4
your_total = personal + share

print("Your share of rent & bill is: ", share)
print("Your personal amount is: ", personal)
print("Your budget for this month is: ", your_total, "in total")