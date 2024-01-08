print("+ add")
print("- subtract")
print("* multiplication")
print("/ division")
print("** exponentiation")

operator = input("Select one of the available calculator options. ")
a = float(input("Enter the first number. "))
b = float(input("Enter the second number. "))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator  == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
elif operator  == "**":
    print(a ** b)
else:
    print("Operator isnt correct.")
