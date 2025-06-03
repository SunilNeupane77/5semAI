# Write a program to implement OR gate

def or_gate_recursive(bits, A=0, B=0):
    if bits == 0:
        output = A | B  # Bitwise OR
        print(f"A = {A}, B = {B} => A OR B = {output}")
        return
    
    # Recurse through all combinations of A and B
    or_gate_recursive(bits - 1, 0, 0)
    or_gate_recursive(bits - 1, 0, 1)
    or_gate_recursive(bits - 1, 1, 0)
    or_gate_recursive(bits - 1, 1, 1)

# Display a title for clarity
print("OR Gate Truth Table (Recursive Implementation):")
print("---------------------------------------------")

# Start the recursion with bits=1 to show all combinations exactly once
or_gate_recursive(1)