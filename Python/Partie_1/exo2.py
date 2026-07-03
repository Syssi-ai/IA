number_one = int(input("Give me a number"))
number_two = int(input("Give me another number"))

if number_one > number_two:
  print("The number", number_one, "is bigger than", number_two)
elif number_one < number_two:
  print("The number", number_two, "is bigger than", number_one)
else:
  print(number_one, "and", number_two, "are equal")
