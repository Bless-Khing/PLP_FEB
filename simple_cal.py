# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.


num1 = int(input("Enter the first number: "))
num2 =  int(input("Enter the second number: "))
symbol = input("Please choose Addition('A') , Subtraction('S') , Multiplication('M') or Division('D'): ")

add =  num1 + num2
subtract =  num1 - num2
multiply =  num1 * num2
divide = num1 / num2

if symbol ==  "A":
    print(f"The result of the addition is {add}")

elif symbol == "S":
    print(f"The result of the subtraction  is {subtract}")

elif symbol == "M":
    print(f"The result of the multiplication is {multiply}")

elif symbol == "D":
    print(f"The result of the division is {divide}")

else:
    print("Please enter a valid input. 'A' , 'S' , 'M' or 'D'!")
