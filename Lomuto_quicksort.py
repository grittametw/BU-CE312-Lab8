num = [29,10,14,37,14,20,7,16,12]
print("Lomuto Quicksort")
print("List =", num)

def partition(arr, low, high):
     
    pivot = arr[high]
    i = (low - 1)

    for s in range(low, high):
        if (arr[s] <= pivot):
            i += 1
            arr[i], arr[s] = arr[s], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quicksort(arr, low, high):

	if (low < high):
		pv = partition(arr, low, high)
		quicksort(arr, low, pv - 1)
		quicksort(arr, pv + 1, high)

n = len(num)
quicksort(num, 0, n - 1)
print("Result =", num)