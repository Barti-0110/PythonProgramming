print("+ add")
print("- subtract")
print("* multiplication")
print("/division")
print("** exponentiation")

simbol = input("Select one of the available calculator options. ")
a = float(input("Enter the first number. "))
b = float(input("Enter the second number. "))

if simbol == "+":
    print(a + b)
elif simbol == "-":
    print(a - b)
elif simbol  == "*":
    print(a * b)
elif simbol == "/":
    print(a / b)
elif simbol  == "**":
    print(a ** b)
else:
    print("Simbol isnt correct
