def binary_search(arr, target):
    length = len(arr)  # Fixed typo
    start = 0
    end = length - 1

    while start <= end:
        mid = (start + end) // 2  # Recalculate mid in each iteration
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1  # Move the start pointer
        else:
            end = mid - 1  # Move the end pointer
    return -1  # Target not found

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
sortd = binary_search(array, target)  # Fixed variable name
print(sortd)  # Print the correct variable