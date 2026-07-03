def average(scores):
    total = 0
    for score in scores:          # loop through the list
        total = total + score     # add each score
    return total / len(scores)    # divide by number of scores

my_scores = [88, 72, 95, 60, 83]
result = average(my_scores)

print("Scores:", my_scores)
print("Average:", result)
my_scores.append(50)
print("Scores:", my_scores)
print("Average:", average(my_scores))