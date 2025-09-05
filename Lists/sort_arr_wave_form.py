arr = [i for i in range(16)]
arr2 = [1, 2, 3, 4, 5]
def sort_wave_form(arr: list):
    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)
sort_wave_form(arr)
print(arr)