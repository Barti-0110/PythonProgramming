import random 
number_min = float(input("Choose Min Number: "))
number_max = float(input("Choose Max Number: "))
random_number = random.randint(number_min, number_max)

guess_number = None
Attempts = 0
while guess_number != random_number:
    guess_number = int(input("Enter number:" ))
    Attempts += 1
    if random_number < guess_number:
        print("Too much")
    elif random_number > guess_number:
        print("Too low")
    else:
        print(f"Number of attempts {Attempts}")
        print("You guessed the number")
        break
