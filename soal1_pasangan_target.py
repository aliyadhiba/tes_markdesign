def find_pairs(arr, target):
    seen = set()
    output = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            output.add(pair)
        seen.add(num)

    return list(output)

arr = [1, 3, 2, 2, 4, 5]
target = 5
print(find_pairs(arr, target))  # Output: [(1, 4), (2, 3)]
