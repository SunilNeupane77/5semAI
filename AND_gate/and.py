# Write a program to implement AND gate

def and_gate_recursive(bits, A=0, B=0):
    if bits == 0:
        output = A & B
        print(f"A = {A}, B = {B} => A AND B = {output}")
        return
    
    # Recurse with reduced bits
    and_gate_recursive(bits - 1, 0, 0)
    and_gate_recursive(bits - 1, 0, 1)
    and_gate_recursive(bits - 1, 1, 0)
    and_gate_recursive(bits - 1, 1, 1)

# Display a title for clarity
print("AND Gate Truth Table (Recursive Implementation):")
print("---------------------------------------------")

# Start the recursion with bits=1 to show all combinations exactly once
and_gate_recursive(1)
