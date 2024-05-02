def get_group():
    group = set()
    while True:
        num = input("Enter an integer (or 'q' to quit): ")
        if num == 'q':
            break
        try:
            num = int(num)
            group.add(num)
        except ValueError:
            print("Invalid input. Please enter an integer or 'q' to quit.")
    return group

# Get up to 3 groups of integers
groups = []
for i in range(3):
    print(f"Enter integers for group {i+1}:")
    group = get_group()
    groups.append(group)

# Display the union and intersection of each pair/three groups
for i in range(len(groups)):
    for j in range(i+1, len(groups)):
        union = groups[i].union(groups[j])
        intersection = groups[i].intersection(groups[j])
        print(f"Union of group {i+1} and group {j+1}: {union}")
        print(f"Intersection of group {i+1} and group {j+1}: {intersection}")