# while loop  (and also for loop) can be used as a repetition


print("How many times you want to print the symbol?")
x = int(input())

i = 0
# i is a counter. keeps track of how many times goes to the loop

while i < x:
  print("\u27bd", i)
  i = i + 1
print("We left the loop")
