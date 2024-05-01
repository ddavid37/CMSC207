print("Welcome to the greatest common divisor calculator!")

answer = "y"

while answer == "y":
    print("Please enter two numbers and the program will calculate the greatest common divisor of the two numbers.\n")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    print("The greatest common divisor of", num1, "and", num2, "is:", gcd(num1, num2))
    print("Thank you for using the greatest common divisor calculator!\n")
    print("Would you like to continue? (y/n): ")
    answer = input()
    if answer == "n":
        print("Goodbye!")
        exit()
    elif answer != "y" and answer != "n":
        print("Invalid input. Please enter 'y' to continue or 'n' to exit.")
        answer = input()