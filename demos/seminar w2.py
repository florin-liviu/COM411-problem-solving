<<<<<<< HEAD



print("Please choose from menu:\n\n1-Nice message\n2-Area of rectangle\n3-Area of triangle\n4-Times table")
option = int(input())

if option == 1:

  print("Today will be a good day!")
elif option == 2:
  print("Enter the lenght of the rectangle")
  l = int(input())
  print("Enter the width of the rectangle")
  w = int(input())
  area = w*l
  print("The area of the rectangle was {}".format(area))
elif option == 3:
  print("Enter the lenght of the triangle")
  base = int(input())
  print("Enter the width of the triangle")
  height = int(input())
  area = 0.5*base*height
  print("The area of the triangle was {:.2f}".format(area))
elif option == 4:
  print("What number would you like to see times table for?")
  n = int(input())
  for i in range(1,11,1):
    print("{}*{} = {}".format(n,i,n*i))
else:
  print("There is no such option, restart!")


=======
# while loop  (and also for loop) can be used as a repetition


print("How many times you want to print the symbol?")
x = int(input())

i = 0
# i is a counter. keeps track of how many times goes to the loop

while i < x:
  print("\u27bd", i)
  i = i + 1
print("We left the loop")



>>>>>>> d85530742e86480ec82d71c9ccac7c4748f38881





