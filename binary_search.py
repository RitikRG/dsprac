def search(arr, target):
    start = 0
    end = len(arr)-1
    while (start<=end):
        mid = start + (end-start)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end=mid-1
        else:
            start=mid+1
    return -1

print(search([1,3,5,7,98,323,525,754], 754))
    
