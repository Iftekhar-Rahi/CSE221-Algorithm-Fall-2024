def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    first_index = -1  # Initialize to -1 to indicate "not found"

    while low <= high:
        mid = (low + high) // 2

        # If the target is found, update first_index and move left
        if arr[mid] == target:
            first_index = mid  # Save the current index as a potential first occurrence
            high = mid - 1     # Continue searching on the left side
        elif arr[mid] < target:
            low = mid + 1      # Move to the right side
        else:
            high = mid - 1     # Move to the left side

    return first_index

# Example usage
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
result = find_first_occurrence(arr, target)
print("First occurrence of", target, "is at index:", result)
