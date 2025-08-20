from d.binary_search_tree import BinarySearchTree

def demonstrate_tree_creation():
    """
    Demonstrates the creation of a Binary Search Tree with a specific
    insertion pattern and prints the resulting tree structure.
    """
    bst = BinarySearchTree()
    print("Building tree with approximately 100 elements using the specified pattern...")

    # A starting range large enough to accommodate the insertions
    value_range = list(range(100))
    insertions = 0
    
    # Loop to insert elements using the average, lower, greater pattern
    while insertions < 100:
        # Ensure the range is large enough to pull 3 values
        if len(value_range) < 3:
            break

        avg = (value_range[0] + value_range[-1]) // 2
        
        # Insert the average, then the smallest, then the largest from the current range
        bst.insert(avg)
        bst.insert(value_range[0])
        bst.insert(value_range[-1])
        
        insertions += 3
        
        # Shrink the range for the next iteration
        value_range.pop(0)
        value_range.pop(-1)

    print(f"\nTotal actual insertions: {insertions}")
    print("--- Resulting ASCII Tree ---")
    bst.print_tree()
    print("--------------------------")

if __name__ == "__main__":
    demonstrate_tree_creation()
