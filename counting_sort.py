def sort(arr):

    r = max(arr)+1
    count = [0] * r

    for i in arr:
        count[i]=count[i]+1
    
    i = 0
    for j in range(len(count)):
        if(count[j]>0):
            for k in range(count[j]):
                arr[i] = j
                i+=1
    return arr

print(sort([2,4,1,6,32,77,33,33,60,876]))
