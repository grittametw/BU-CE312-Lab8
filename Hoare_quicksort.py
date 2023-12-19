num = [29,10,14,37,14,20,7,16,12]
print("Hoare Quicksort")
print("List =", num)

def partition(arr, low, high):
 
    pivot = arr[(high + low) // 2]
    i = low - 1
    s = high + 1
 
    while (True):
        i += 1

        while (arr[i] < pivot):
            i += 1
        s -= 1
        while (arr[s] > pivot):
            s -= 1
        if (i >= s):
            return s

        arr[i], arr[s] = arr[s], arr[i]
 
def quicksort(arr, low, high):

    if (low < high):
        pv = partition(arr, low, high)
        quicksort(arr, low, pv)
        quicksort(arr, pv + 1, high)

n = len(num)
quicksort(num, 0, n - 1)
print("Result =", num)