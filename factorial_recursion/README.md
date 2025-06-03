# Factorial Calculation Using Recursion

This project implements factorial calculation using recursion.

## Solution Technique

Factorial is calculated using the recursive formula:

1. **Base Case**:
   - 0! = 1
   - 1! = 1

2. **Recursive Case**:
   - n! = n × (n-1)!

The solution uses direct recursion to implement this mathematical definition.

## How to Run

```bash
python facto.py
```

When prompted, enter a non-negative integer for which you want to calculate the factorial.

## Time Complexity

The time complexity is O(n) where n is the input number. The algorithm makes exactly n recursive calls.

## Space Complexity

The space complexity is also O(n) due to the recursion stack.

## Limitations

Due to Python's recursion depth limit and integer size limitations, very large factorials may cause:
1. RecursionError (can be mitigated with `sys.setrecursionlimit()`)
2. Memory issues for extremely large values
