name = input("What's your name? ") #il faut mettre input pour attendre uen réponse de l'utilisateur
birth_year = int(input("What year were you born? ")) #il faut le mettre car il s'attend à un entier de l'utilisateur
age = 2026 - birth_year
print("Hi", name + "! You are", age, "years old.")