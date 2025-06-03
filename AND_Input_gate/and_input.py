# write a program to implement AND gate by user input
def get_binary_input(prompt):
    val = input(prompt)
    if val not in ('0', '1'):
        print("Invalid input. Please enter 0 or 1.")
        return get_binary_input(prompt)  # Recursive call
    return int(val)

# Main function to simulate AND gate
def and_gate():
    A = get_binary_input("Enter first input (0 or 1): ")
    B = get_binary_input("Enter second input (0 or 1): ")
    output = A & B
    print(f"A = {A}, B = {B} => A AND B = {output}")

# Run the AND gate function
and_gate()