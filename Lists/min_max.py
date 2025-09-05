
def find_min(arr: list):
    min_value = float('inf')
    for value in arr:
        if min_value > value:
            min_value = value
    return min_value

def find_max(arr: list):
    max_value = float('-inf')
    for value in arr:
        if max_value < value:
            max_value = value
    return max_value

test_list = [1,4,-3,312,14, 10,11]
print(find_min(test_list))
print(find_max(test_list))
