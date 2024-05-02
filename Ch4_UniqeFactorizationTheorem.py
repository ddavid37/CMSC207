def unique_factorization_theorem():
    print("Welcome!")
    while True:
        num = int(input("Please enter a number: "))
        factors = []
        divisor = 2

        while num > 1:
            if num % divisor == 0:
                factors.append(divisor)
                num = num // divisor  # Changed to integer division
            else:
                divisor += 1

        print("The unique factorization theorem for", num, "is:")
        print(factors)

        choice = input("Do you want to display factor degrees? (y/n): ")  # Updated prompt
        while choice.lower() not in ["y", "n"]:
            choice = input("Invalid input. Please enter 'y' or 'n': ")

        if choice.lower() == "n":
            print("Goodbye!")
            factor_degrees = {}
            for factor in factors:
                if factor in factor_degrees:
                    factor_degrees[factor] += 1
                else:
                    factor_degrees[factor] = 1
            
            print("The degrees of the factors are:")
            for factor, degree in factor_degrees.items():
                print(factor, ":", degree)
            break

unique_factorization_theorem()
