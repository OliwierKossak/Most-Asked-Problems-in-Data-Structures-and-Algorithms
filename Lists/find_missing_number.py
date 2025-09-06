
arr = [8, 2, 4, 5, 3, 7, 1]

def find_missing_number(arr: list[int]):
    arr_sum = sum(arr)
    arr2_sum= (len(arr)+1) * (len(arr)+2) //2
    if arr2_sum != arr_sum:
        return abs(arr2_sum - arr_sum)
    return -1

print(find_missing_number(arr))