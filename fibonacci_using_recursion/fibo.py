# write a program to display Fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def display_fibonacci_series(terms):
    if terms <= 0:
        print("Please enter a positive integer")
        return
    
    print(f"Fibonacci series (first {terms} terms):")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()

if __name__ == "__main__":
    try:
        num_terms = int(input("How many terms of Fibonacci series do you want to display? "))
        display_fibonacci_series(num_terms)
    except ValueError:
        print("Please enter a valid integer")