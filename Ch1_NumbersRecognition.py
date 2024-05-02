print("Welcome to the Number Recognition Program!")

repeat = True

while repeat:
    number = input("Enter a number: ")

    if number.isdigit():
        print("It is a natural number (N).")
    elif number.startswith('-') and number[1:].isdigit():
        print("It is an integer (Z).")
    elif '.' in number and all(char.isdigit() for char in number.replace('.', '', 1)):
        print("It is a rational number (Q).")
    elif '/' in number and all(char.isdigit() for char in number.split('/', 1)[0]) and all(char.isdigit() for char in number.split('/', 1)[1]):
        print("It is a rational number (Q).")
    elif number.endswith('j') and all(char.isdigit() for char in number[:-1]):
        print("It is an imaginary number (I).")
    else:
        print("It is a real number (R).")

    choice = input("Do you want to repeat? (yes/no): ")
    if choice.lower() != "yes":
        repeat = False

print("Thank you for using the Number Recognition Program!")
