arr = [1,3,4,5,-1 ,6,]
def search_element_unsorted(arr: list,search_element: int):
    found = False
    for element in arr:
        if element == search_element:
            found = True
            break
    return found

print(search_element_unsorted(arr, 4))

arr_sorted = [i for i in range(20)]

def binary_search(arr:list, number: int):
    top = len(arr)
    bottom = 0
    while top >= bottom:
        mid = (bottom + top)//2
        if arr[mid] > number:
            top = mid -1
        elif arr[mid] < number:
            bottom = mid + 1
        else:
            return True

    return False


print(binary_search(arr_sorted, 130))
