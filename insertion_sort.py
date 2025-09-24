def sort(arr):
    for i in range(1,len(arr)):
        unsorted = arr[i]
        sorted = i-1

        while (sorted>=0) and (unsorted<arr[sorted]):
            arr[sorted+1] = arr[sorted]
            sorted -= 1
        arr[sorted+1] = unsorted
    return arr

print(sort([2,4,1,6,32,-4,77,33,33,60,876,-8747]))
