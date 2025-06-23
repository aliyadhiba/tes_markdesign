def manual_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def sort_even_index(arr):
    even = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    even = manual_sort(even)

    result = []
    even_index = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            result.append(even[even_index])
            even_index += 1
        else:
            result.append(arr[i])
    return result

print(sort_even_index([5, 3, 2, 8, 1, 4]))  # Output: [1, 3, 2, 8, 5, 4]
