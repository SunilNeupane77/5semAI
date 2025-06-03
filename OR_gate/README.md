# OR Gate Implementation

This project demonstrates the logical operation of an OR gate using recursion to generate all possible input combinations.

## Solution Technique

The solution uses recursion to:

1. Generate all possible combinations of binary inputs (0,0), (0,1), (1,0), and (1,1)
2. Apply the OR logic operation to each pair of inputs
3. Display the truth table output

The OR operation returns 0 only when both inputs are 0, otherwise it returns 1.

## Logic Implementation

The program uses the bitwise OR operator (`|`) to implement the OR gate logic.

## How to Run

```bash
python or.py
```

The program will automatically display the truth table for the OR operation.

## Educational Value

This implementation helps in understanding:
1. Truth tables and Boolean logic
2. How recursion can be used to generate combinations
3. Basic digital logic gates functioning
