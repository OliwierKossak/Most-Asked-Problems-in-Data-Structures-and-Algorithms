# arr = [1,5,2,6,-2,11,8]
arr = [6, 8, 0, 1, 3]

def next_greater_element(arr):
    greater_elements = []

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                greater_elements.append(arr[j])
                break
        else:
            greater_elements.append(-1)

    return greater_elements

print(next_greater_element(arr))