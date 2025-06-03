# write a program to implement  OR gate by user input
# Recursive function to get valid binary input
def get_binary_input(prompt):
    val = input(prompt)
    if val not in ('0', '1'):
        print("Invalid input. Please enter 0 or 1.")
        return get_binary_input(prompt)  # Recursive call
    return int(val)

# Main function to simulate OR gate
def or_gate():
    A = get_binary_input("Enter first input (0 or 1): ")
    B = get_binary_input("Enter second input (0 or 1): ")
    output = A | B  # Bitwise OR
    print(f"A = {A}, B = {B} => A OR B = {output}")

# Run the OR gate function
or_gate()
