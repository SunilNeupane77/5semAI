# Write a program to illustrate tower of hanoi using recursion

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
        
    # Move n-1 disks from source to auxiliary using destination as temporary
    tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination using source as temporary
    tower_of_hanoi(n-1, auxiliary, source, destination)

def run_tower_of_hanoi():
    """Execute the Tower of Hanoi algorithm with user input"""
    try:
        num_disks = int(input("Enter number of disks: "))
        if num_disks <= 0:
            print("Please enter a positive integer")
            return
            
        print(f"\nSolving Tower of Hanoi with {num_disks} disks:")
        print(f"Rods are labeled: A (source), B (auxiliary), C (destination)\n")
        
        tower_of_hanoi(num_disks, 'A', 'B', 'C')
        
        # Calculate total moves
        total_moves = (2**num_disks) - 1
        print(f"\nTotal moves required: {total_moves}")
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    run_tower_of_hanoi()
