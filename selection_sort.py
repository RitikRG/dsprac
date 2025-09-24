def sort(arr):
    for i in range(len(arr)):
        min_idx = i
        min = arr[i]
        for j in range(i+1,len(arr)):
            if(arr[j]<min):
                min_idx=j
                min = arr[j]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(sort([2,4,1,6,32,-4,77,33,33,60,876,-8747]))
