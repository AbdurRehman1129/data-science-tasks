first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
op = input("Enter operation +, -, *, /, %: ")
if op == '+':
    print(f"Sum of {first_number} and {
          second_number} is {first_number+second_number}")
elif op == '-':
    print(f"Difference of {first_number} and {
          second_number} is {first_number-second_number}")
elif op == '*':
    print(f"Multiplication of {first_number} and {
          second_number} is {first_number*second_number}")
elif op == '/':
    print(f"Division of {first_number} and {
          second_number} is {first_number/second_number}")
elif op == '%':
    print(f"Modulus of {first_number} and {
          second_number} is {first_number % second_number}")
else:
    print("Invalid input")
