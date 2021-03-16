<<<<<<< HEAD
fruits = []

vegetables = ["Carrot", "Peas"]

fruits.append("Apple")
fruits.append("Banana")
fruits.append("Tomatoe")
fruits.append("Banana")

print(fruits)

fruits.remove("Banana")

print(fruits)

del fruits[1]

print(fruits)

fruits.insert(1, "Pineapple")

print(fruits)



def get_fruits():
  fruits = []
  for i in range(4):
    print("Tyoe in the next fruit:")
    fruits.append(input())
  print("Your fruits are {}".format(fruits))

get_fruits()
=======

def  identify():
  print ("what lies before us?")
  answer = input()
  if answer == "a large boulder":
    print("it's time to run")
  else:
    print("we well be fine!")
identify() 

# Define a function for calculate the area of triangle
def calculate_area(h = 10,b = 5):
 
  area = 0.5*h*b
  return area

def run():
  x = calculate_area(4)
  x += 1
  print(f"The area of triangle is {x}")
 
run()
#print(calculate_area())
#x = calculate_area(12,5)
#print(x+1)


#Call the function
#calculate_area(h,b)

#calculate_area()
#calculate_area(5)
#calculate_area(b=20)
#calculate_area(13,7)





#Parameter  - a valuw you plug into a function

>>>>>>> 0fcfeb8cbf5fac02a74d5d41e1efd10600a65db7
