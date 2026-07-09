def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for x in range(0, n - i - 1):
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]
    return array

array = [73,12,65,90,32]
sorted_array = bubble_sort(array)
print(sorted_array)