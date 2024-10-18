def binary_search_recursive(arr, target, low, high):
    # Base case: if the range is valid
    if high >= low:
        mid = (low + high) // 2
        
        # Check if the target is at the middle
        if arr[mid] == target:
            return True
        
        # If target is smaller than mid, search the left subarray
        elif arr[mid] > target:
            return binary_search_recursive(arr, target, low, mid - 1)
        
        # If target is larger than mid, search the right subarray
        else:
            return binary_search_recursive(arr, target, mid + 1, high)
    
    # Target is not in the array
    else:
        return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")