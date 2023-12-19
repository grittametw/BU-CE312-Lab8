num = [29,10,14,37,14,20,7,16,12]
print("Merge Sort")
print("List =", num)

def mergesort(arr):
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        
        a = 0
        b = 0
        c = 0
        
        while a < len(left) and b < len(right):
            if left[a] <= right[b]:
              arr[c] = left[a]
              a += 1
            else:
                arr[c] = right[b]
                b += 1
            c += 1
        while a < len(left):
            arr[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            arr[c]=right[b]
            b += 1
            c += 1
        
    return arr
    
result = mergesort(num)
print("Result =", result)