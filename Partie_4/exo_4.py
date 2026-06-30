#  Your turn!
def find_max(numbers):
    biggest = numbers[0]    # start by assuming the first is biggest

    for number in numbers:
        if number > biggest:
            biggest = number

    return biggest

# Test it!
print(find_max([3, 7, 2, 9, 1]))    # should print 9
print(find_max([100, 50, 75]))       # should print 100