# Write a program to implement and gate
def AND_gate(input1, input2):
    """
    Implements an AND gate logic
    
    Args:
        input1: First input (0 or 1)
        input2: Second input (0 or 1)
        
    Returns:
        1 if both inputs are 1, otherwise 0
    """
    if input1 == 1 and input2 == 1:
        return 
    else:
        return 0

def display_truth_table():
    """Display the truth table for AND gate"""
    print("AND Gate Truth Table:")
    print("--------------------")
    print("| Input1 | Input2 | Output |")
    print("--------------------")
    
    for input1 in [0, 1]:
        for input2 in [0, 1]:
            output = AND_gate(input1, input2)
            print(f"|   {input1}    |   {input2}    |   {output}    |")
    
    print("--------------------")

def user_interaction():
    """Allow user to test the AND gate with custom inputs"""
    try:
        print("\nTest AND gate with your inputs:")
        input1 = int(input("Enter first input (0 or 1): "))
        input2 = int(input("Enter second input (0 or 1): "))
        
        if input1 not in [0, 1] or input2 not in [0, 1]:
            print("Inputs must be either 0 or 1")
            return
        
        result = AND_gate(input1, input2)
        print(f"\nAND({input1}, {input2}) = {result}")
        
    except ValueError:
        print("Please enter valid binary values (0 or 1)")

if __name__ == "__main__":
    print("AND Gate Implementation\n")
    display_truth_table()
    user_interaction()