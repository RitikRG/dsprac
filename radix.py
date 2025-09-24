def count_sort(arr,place):
    output = [0]*len(arr)
    count = [0]*10
    k = 0

    for i in arr:
        count[(i//place) % 10] +=1

    for i in range(10):
        if(count[i]>0):
            while count[i]>0:
                for j in range(len(arr)):
                    if(arr[j]//place%10 == i):
                        output[k] = arr[j]
                        k+=1
                        arr[j] = -1
                        break
                count[i]-=1
    print(output)
    return output
            

# The above approach worked fine but made the time complexity n^2 here's the optimised 

def cSort(arr, place):
    output=[0]*len(arr)
    count=[0]*10

    for i in arr:
        index = (i//place) %10
        count[index]+=1

    # Making it cumulative count
    for i in range(1,len(count)):
        count[i] += count[i-1]
    
    l = len(arr)-1
    while l>=0:
        index = (arr[l]//place)%10
        output[count[index]-1]=arr[l]
        count[index]-=1
        l-=1
    
    for i in range(len(arr)):
        arr[i]=output[i]


def radixSort(arr):
    max_value = max(arr)
    place = 1

    while(max_value//place > 0):
        cSort(arr,place)
        place*=10

    return arr

print(radixSort([2,4,1,63,32,77,33,60,876]))