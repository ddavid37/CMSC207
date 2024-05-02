import math

def calculate_combinations(n, r):
    return math.comb(n, r)

def calculate_permutations(n, r):
    return math.perm(n, r)

print("Welcome to the combinations and permutations calculator!")
print("This program will calculate the number of combinations and permutations of n items taken r at a time.")

while True:
    n = int(input("Enter the value of n: "))
    r = int(input("Enter the value of r: "))
    
    combinations = calculate_combinations(n, r)
    permutations = calculate_permutations(n, r)
    
    print(f"\nCombinations: {combinations}")
    print(f"Permutations: {permutations}\n")
    
    repit = input("Would you like to calculate again? (Y/N): ").upper()
    while repit not in ['Y', 'N']:
        print("Invalid input. Please enter 'Y' to continue or 'N' to exit.")
        repit = input().upper()
    
    if repit == 'N':
        print("Goodbye!\n")
        break
