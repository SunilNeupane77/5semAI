# Write a program to disolay factorial number using recursion

def factorial(n):
    """
    Calculate factorial of n using recursion
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n-1)

def display_factorial():
    """Get user input and display the factorial"""
    try:
        num = int(input("Enter a non-negative integer: "))
        
        if num < 0:
            print("Factorial is not defined for negative numbers.")
            return
        
        result = factorial(num)
        print(f"Factorial of {num} is: {result}")
        
        # Display the calculation steps
        print(f"\nCalculation steps:")
        print(f"{num}! = ", end="")
        for i in range(num, 0, -1):
            if i == 1:
                print(f"{i} = {result}")
            else:
                print(f"{i} × ", end="")
    
    except ValueError:
        print("Please enter a valid integer")
    except RecursionError:
        print("Number too large for recursion depth. Try a smaller number.")

if __name__ == "__main__":
    display_factorial()
