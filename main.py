print ("What is your name?")
n = input()

print ("Do you have a dog")
dog = bool(input())


if len(n) > 9 and dog == "True" :

  print("You  have a very long name")
  print("Your name contains {} letters".format(len(n)))
else:
  print("You name is short")



print("This is the end of program!")




