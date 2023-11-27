import random 
liczba_min = 1
liczba_max = 100
liczba_losowana = random.randint(liczba_min, liczba_max)

liczba = None

while liczba != liczba_losowana:
    liczba = int(input("Wpisz liczbe:" ))
    if liczba_losowana < liczba:
        print("za dużo")
    elif liczba_losowana > liczba:
        print("za mało")
    else:
        print("zgadłeś liczbe")
        break