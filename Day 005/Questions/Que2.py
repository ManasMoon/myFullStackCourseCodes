# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.


sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
total = sub1+sub2+sub3
avg = total/3
if(avg>=40 and sub1>=33 and sub2>=33 and sub3>=33):
          print("Passed")
else:
          print("Failed")
          print("Average: ",avg)