# Water Jug Problem

This project implements the solution to the classic Water Jug problem using recursive search.

## Problem Description

Given two jugs with capacities A and B, and no measuring marks on them, find a sequence of steps to get exactly T units of water in one of the jugs.

Operations allowed:
1. Fill a jug completely
2. Empty a jug completely
3. Pour water from one jug into another until the destination jug is full or the source jug is empty

## Solution Technique

The solution uses recursive depth-first search with backtracking:

1. Maintain a set of visited states to avoid cycles
2. For each state (amount in jug A, amount in jug B), try all possible operations
3. Recursively explore each new state
4. Backtrack if a path doesn't lead to the solution
5. Return the sequence of states that leads to the target

## How to Run

```bash
python waterjug.py
```

The program uses default jug capacities (4L and 3L) and a target amount (2L).

## Algorithmic Approach

This is an application of the state-space search method, where:
- States are represented as (amount in jug A, amount in jug B)
- Transitions are the allowed operations
- The goal is to reach a state where either jug contains exactly the target amount

## Time and Space Complexity

Both time and space complexity are O(A×B) in the worst case, where A and B are the capacities of the jugs, as we might need to explore all possible states.
