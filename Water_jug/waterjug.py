# Write  a program to implement water jug problem using recursion
def water_jug_recursive(cap_a, cap_b, target, curr_a=0, curr_b=0, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    # If already visited this state, skip to avoid infinite loop
    if (curr_a, curr_b) in visited:
        return None

    # Add this state to path and visited
    visited.add((curr_a, curr_b))
    path.append((curr_a, curr_b))

    # Check if target is reached in either jug
    if curr_a == target or curr_b == target:
        return path.copy()

    # List possible next moves (states)
    possible_moves = [
        (cap_a, curr_b),            # Fill Jug A
        (curr_a, cap_b),            # Fill Jug B
        (0, curr_b),                # Empty Jug A
        (curr_a, 0),                # Empty Jug B
        # Pour A -> B
        (curr_a - min(curr_a, cap_b - curr_b), curr_b + min(curr_a, cap_b - curr_b)),
        # Pour B -> A
        (curr_a + min(curr_b, cap_a - curr_a), curr_b - min(curr_b, cap_a - curr_a)),
    ]

    for next_a, next_b in possible_moves:
        result = water_jug_recursive(cap_a, cap_b, target, next_a, next_b, visited.copy(), path.copy())
        if result:
            return result

    return None

# Example usage:
if __name__ == "__main__":
    cap_a = 4
    cap_b = 3
    target = 2
    solution = water_jug_recursive(cap_a, cap_b, target)
    if solution:
        print("Steps to get", target, "liters:")
        for state in solution:
            print("Jug A:", state[0], "Jug B:", state[1])
    else:
        print("No solution found.")