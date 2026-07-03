# A function that returns a value
def square(number):
    result = number * number
    return result

z = int(input("Enter a number to square: "))

print(square(z))    # 16  

# You can also store the return value
my_answer = square(10)
print("10 squared is", my_answer)