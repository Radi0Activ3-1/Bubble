def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                swapped = True
        if not swapped:
            break  # If no swaps occur, the list is already sorted

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Sorted list:", numbers)
