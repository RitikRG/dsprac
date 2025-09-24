# Linear search

def search(arr,target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i
    return -1

print(search([1,4,23,5,25,324,46,236,463,277], 277))