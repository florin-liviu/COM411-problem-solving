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