# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.


comment = input("Enter comment: ")
if("make a lot of money" in comment):
          print("Spam")
elif("buy now" in comment):
          print("Spam")
elif("subscribe this" in comment):
          print("Spam")
elif("click this" in comment):
          print("Spam")
else:
          print("Not Spam")
