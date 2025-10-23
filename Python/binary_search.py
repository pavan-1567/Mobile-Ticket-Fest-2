# Binary Search Algorithm
# Time Complexity: O(log n)
# Space Complexity: O(1) for iterative approach

def binary_search_iterative(arr, target):
    """
    Perform binary search on a sorted array using iterative approach.
    
    Parameters:
    arr (list): A sorted list of elements
    target: The element to search for
    
    Returns:
    int: Index of the target element if found, -1 otherwise
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target not found
    return -1


def binary_search_recursive(arr, target, left, right):
    """
    Perform binary search on a sorted array using recursive approach.
    
    Parameters:
    arr (list): A sorted list of elements
    target: The element to search for
    left (int): Starting index
    right (int): Ending index
    
    Returns:
    int: Index of the target element if found, -1 otherwise
    """
    # Base case: element not found
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    # Check if target is present at mid
    if arr[mid] == target:
        return mid
    
    # If target is greater, search in right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    
    # If target is smaller, search in left half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == "__main__":
    # Test array (must be sorted for binary search)
    arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    
    print("Array:", arr)
    print()
    
    # Test case 1: Element exists in array
    target1 = 23
    result1 = binary_search_iterative(arr, target1)
    if result1 != -1:
        print(f"Iterative Search: Element {target1} found at index {result1}")
    else:
        print(f"Iterative Search: Element {target1} not found in array")
    
    # Test case 2: Element doesn't exist in array
    target2 = 50
    result2 = binary_search_iterative(arr, target2)
    if result2 != -1:
        print(f"Iterative Search: Element {target2} found at index {result2}")
    else:
        print(f"Iterative Search: Element {target2} not found in array")
    
    print()
    
    # Test recursive approach
    target3 = 67
    result3 = binary_search_recursive(arr, target3, 0, len(arr) - 1)
    if result3 != -1:
        print(f"Recursive Search: Element {target3} found at index {result3}")
    else:
        print(f"Recursive Search: Element {target3} not found in array")
    
    # Test case 4: First element
    target4 = 2
    result4 = binary_search_recursive(arr, target4, 0, len(arr) - 1)
    if result4 != -1:
        print(f"Recursive Search: Element {target4} found at index {result4}")
    else:
        print(f"Recursive Search: Element {target4} not found in array")

