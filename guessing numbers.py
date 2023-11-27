import random 
number_min = 1
number_max = 100
random_number = random.randint(number_min, number_max)

guess_number = None

while guess_number != random_number:
    gues_number = int(input("Wpisz liczbe:" ))
    if random_number < guess_number:
        print("Too much")
    elif random_number > guess_number:
        print("Too low")
    else:
        print("You guessed the number")
        break
