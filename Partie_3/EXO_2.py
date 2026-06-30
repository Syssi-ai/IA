# A simple guessing game
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    if guess != secret:
        print("Nope! Try again.")
print("Correct!")