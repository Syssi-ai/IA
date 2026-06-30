age = int(input("How old are you? "))

if age >= 18:
    print("You can watch this movie!")
elif age >= 13:
    print("You can watch with a parent.")
else:
    print("This movie isn't for you yet.")