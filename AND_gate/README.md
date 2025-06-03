# AND Gate Implementation

This project demonstrates the logical operation of an AND gate using recursion to generate all possible input combinations.

## Solution Technique

The solution uses recursion to:

1. Generate all possible combinations of binary inputs (0,0), (0,1), (1,0), and (1,1)
2. Apply the AND logic operation to each pair of inputs
3. Display the truth table output

The AND operation returns 1 only when both inputs are 1, otherwise it returns 0.

## Logic Implementation

The program uses the bitwise AND operator (`&`) to implement the AND gate logic.

## How to Run

```bash
python and.py
```

The program will automatically display the truth table for the AND operation.

## Educational Value

This implementation helps in understanding:
1. Truth tables and Boolean logic
2. How recursion can be used to generate combinations
3. Basic digital logic gates functioning
