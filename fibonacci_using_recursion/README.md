# Fibonacci Sequence Using Recursion

This project implements the Fibonacci sequence calculator using recursion.

## Solution Technique

The solution uses pure recursion to calculate Fibonacci numbers. In this approach:

1. **Base Cases**: 
   - If n = 0, return 0
   - If n = 1, return 1

2. **Recursive Case**:
   - For n > 1, return fibonacci(n-1) + fibonacci(n-2)

This directly implements the mathematical definition of the Fibonacci sequence.

## How to Run

```bash
python fibo.py
```

When prompted, enter the number of Fibonacci terms you want to display.

## Time Complexity

This recursive implementation has O(2^n) time complexity due to repeated calculations, making it inefficient for large values of n.

## Potential Improvements

For better performance, techniques like memoization or dynamic programming could be used to avoid recalculating values.
