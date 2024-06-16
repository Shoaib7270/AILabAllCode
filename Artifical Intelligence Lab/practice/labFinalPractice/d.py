num1= int(input("Enter first number= "))
num2= int(input("Enter second number= "))
num3= int(input("Enter third number= "))

if num1 > num2:
    if num1 > num3:
        print("Number 1 is greatest")
    else:
        print("Number 3 is greatest")
elif num2 > num1 :
    if num2 > num3 :
        print("Number 2 is greatest")
    else:
        print("Number 3 is greatest")