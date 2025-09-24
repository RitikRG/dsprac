def sort(arr):
    last = len(arr)
    while(last>0):
        for i in range(last-1):
            if(arr[i]>arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
        last -=1
    return arr

print(sort([2,4,1,6,32,-4,77,33,33,60,876,-8747]))