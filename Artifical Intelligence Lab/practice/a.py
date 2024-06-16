def find_largest_number(num1, num2):
    """
    This function takes two numbers as input and returns the largest of the two.
    """
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"

# Taking user input
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Calling the function and displaying the result
    largest_number = find_largest_number(number1, number2)
    print("The largest number is:", largest_number)
except ValueError:
    print("Invalid input! Please enter numeric values.")
