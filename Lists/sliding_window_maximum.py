arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]


def sliding_window(arr: list, k: int = 3):
    max_subarray = []
    for i in range(0, len(arr)-k +1):
        subarray = arr[i:i + k]
        max_value = max(subarray)
        max_subarray.append(max_value)

    return max_subarray

print(sliding_window(arr))
