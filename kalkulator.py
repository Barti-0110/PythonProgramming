print("+ dodawanie")
print("- odejmowanie")
print("* mnożenie")
print("/ dzielenie")
print("** potęgowanie")

symbol_działania = input("Wybierz jedną z dostępnych opcji kalkulatora. ")
a = float(input("Wprowadź pierwszą liczbę. "))
b = float(input("Wprowadź drugą liczbę. "))

if symbol_działania == "+":
    print(a + b)
elif symbol_działania == "-":
    print(a - b)
elif symbol_działania == "*":
    print(a * b)
elif symbol_działania == "/":
    print(a / b)
elif symbol_działania == "**":
    print(a ** b)
else:
    print("Ten znak nie jest poprawny.")