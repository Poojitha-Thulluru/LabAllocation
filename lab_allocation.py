try:
    # Get input from the user
    x = int(input("Enter the seating capacity of lab L1: "))
    y = int(input("Enter the seating capacity of lab L2: "))
    z = int(input("Enter the seating capacity of lab L3: "))
    n = int(input("Enter the number of students in the class: "))

    # Determine the lab suitable for the given number of students
    suitable_lab = None
    min_difference = 0
    if n <= x:
        suitable_lab = 'L1'
        min_difference = x - n
    if n <= y and y - n < min_difference:
        suitable_lab = 'L2'
        min_difference = y - n
    if n <= z and z - n < min_difference:
        suitable_lab = 'L3'
        min_difference = z - n

    if suitable_lab is not None:
        print(f"Lab {suitable_lab} is suitable for the class.")
    else:
        print("None of the labs can accommodate the class.")
except ValueError:
    print("Invalid input. Please enter integers only.")