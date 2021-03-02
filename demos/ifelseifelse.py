print ("What is your name?")
n = input()

# print ("Do you have a dog")
# dog = bool(input())


if len(n) >= 9: 
  print("You  have a very long name")
  print("Your name contains {} letters".format(len(n)))
elif len(n) > 6:
  print("Your name is a bit long, consider a nickname")
elif len(n) <3:
  print("Your name is very short")
else:
  print("You name is quite okay")

print("This is the end of program!")




