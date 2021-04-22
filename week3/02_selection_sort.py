input = [4, 6, 2, 9, 1]



def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_su = i
        for j in range(n - i):
            if array[j+i] < array[min_su]:
                array[min_su], array[j+i] = array[j+i], array[min_su]

    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!