cars = []
while True:
   values = input("Enter values: ")
   if values == "stop":
     break
   cars.append(values)
   cars.sort()
   print(cars)

# Print the total number of values
print("Total number of values: ", len(cars))