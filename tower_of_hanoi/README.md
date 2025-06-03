# Tower of Hanoi

This project implements the solution to the classic Tower of Hanoi puzzle using recursion.

## Solution Technique

The Tower of Hanoi is a perfect demonstration of recursive problem-solving. The solution follows these steps:

1. **Base Case**:
   - If only one disk, move it directly from source to destination

2. **Recursive Steps**:
   - Move n-1 disks from source to auxiliary rod
   - Move the largest disk from source to destination
   - Move the n-1 disks from auxiliary to destination

## How to Run

```bash
python tower.py
```

When prompted, enter the number of disks you want to solve for.

## Time Complexity

The time complexity is O(2^n), where n is the number of disks. The minimum number of moves required is 2^n - 1.

## Mathematical Background

The Tower of Hanoi demonstrates an exponential relationship between the number of disks and the number of moves required, making it an excellent example of how recursive solutions can elegantly solve seemingly complex problems.
